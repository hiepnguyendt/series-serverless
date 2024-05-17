import boto3
import json
import os
from boto3.dynamodb.types import TypeDeserializer

# Create SQS client
sqs_client = boto3.client('sqs')
# Create DynamoDB client
dynamodb_client = boto3.client('dynamodb')
serializer = TypeDeserializer()


def deserialize(data):
    if isinstance(data, list):
        return [deserialize(v) for v in data]

    if isinstance(data, dict):
        try:
            return serializer.deserialize(data)
        except TypeError:
            return {k: deserialize(v) for k, v in data.items()}
    else:
        return data


def format_db_data(messages, db_data):
    if 'Items' in db_data:
        format_data = deserialize(db_data["Items"])
    price = 0
    for book_item in format_data:
        price = book_item['price']
        del book_item['price']
        del book_item['id']
    messages.append({
        "receiptHandle": "",
        "books": format_data,
        "price": price,
        "status": "Processed"
    })


def get_order_from_dynamodb(messages):
    data = []
    i = 1
    while True:
        id = str(i)
        data = dynamodb_client.query(
            TableName="Orders", KeyConditionExpression="id = :id", ExpressionAttributeValues={":id": {"S": id}})
        if not data["Items"]:
            break
        format_db_data(messages, data)
        i += 1


def get_order_from_sqs(messages):
    queue_name = os.getenv("QUEUE_NAME")
    queue = sqs_client.get_queue_url(QueueName=queue_name)
    queue_url = queue['QueueUrl']
    response = sqs_client.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages']
    )

    number_of_message = int(
        response['Attributes']['ApproximateNumberOfMessages'])
    print(number_of_message)
    i = 0
    while i < number_of_message:
        msg_list = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
            VisibilityTimeout=3
        )
        if 'Messages' in msg_list:
            for m in msg_list['Messages']:
                print(json.loads(m["Body"]))
                messages.append({
                    "receiptHandle": m["ReceiptHandle"],
                    "books": json.loads(m["Body"])['books'],
                    "price": json.loads(m["Body"])['price'],
                    "status": "Unprocessed"
                })
                i += 1


def lambda_handler(event, context):
    messages = []

    get_order_from_dynamodb(messages)
    get_order_from_sqs(messages)
    print(messages)
    return{
        'statusCode': 200,
        'body': json.dumps(messages),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
