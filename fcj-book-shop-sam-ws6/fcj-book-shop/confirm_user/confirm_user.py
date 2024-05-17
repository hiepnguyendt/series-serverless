import json
import boto3
import os

client = boto3.client('cognito-idp')

def lambda_handler(event, context):
    user_infor = json.loads(event['body'])
    client_id = os.getenv("CLIENT_ID")
    user_pool_id = os.getenv("USER_POOL_ID")
    error = None
    try:
        resp = client.confirm_sign_up(
            ClientId=client_id,
            Username=user_infor['username'],
            ConfirmationCode=user_infor['code']
            )
    except Exception as e:
        error = e.__str__()
        
    if error is None:
        message = "Confirm successful!"
        statusCode = 200
    else:
        message = "Confirm fail!"
        statusCode = 400
        print(error)
        
    # TODO implement
    return {
            'statusCode': statusCode,
            'body': message,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,X-Access-Token, XKey, Authorization",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS"
            },
    }
