import boto3
import json
import os

dynamodb_client = boto3.client('dynamodb')
sqs_client = boto3.client('sqs')


def lambda_handler(event, context):
    order_item = json.loads(event["body"])
    if order_item['receiptHandle']:
        queue_name = os.getenv("QUEUE_NAME")
        queue = sqs_client.get_queue_url(QueueName=queue_name)
        queue_url = queue['QueueUrl']
        response = sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=order_item['receiptHandle']
        )

    response = {
        'statusCode': 200,
        'body': 'successfully handle order!',
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,X-Access-Token, XKey, Authorization",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS"
        },
    }
    
    return response
