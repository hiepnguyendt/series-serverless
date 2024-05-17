import json
import boto3
import os

    
def lambda_handler(event, context):
    client = boto3.client("sqs")
    sns = boto3.client('sns')
    queue_name = os.getenv("QUEUE_NAME")
    status = 200
    try:
        response = client.get_queue_url(
            QueueName=queue_name
        )
        
        send_response = client.send_message(
            QueueUrl=response['QueueUrl'], 
            MessageBody=event["body"]
        )
    except Exception as e:
        status = 400
    
    try:
        response1 = sns.publish(
            TopicArn=os.environ['SNS_ARN'],    
            Message="There is a new order. Please check it!",    
        )
    except Exception as e:
        status = 400
        print(e)

    return {
        'statusCode': status,
        'body': json.dumps(response["ResponseMetadata"]),
        'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
    }
