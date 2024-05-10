import json
import boto3
import botocore.exceptions
import os


client = boto3.client('cognito-idp')
def initiate_auth(client_id, username, password):
    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            ClientId=client_id,
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
            }
        )
        print(response)
        
    except Exception as e:
        return None, e.__str__()
        
    return response, None

def lambda_handler(event, context):
    user_infor = json.loads(event['body'])
    error = ""
    message = ""
    client_id = os.getenv("CLIENT_ID")
    
        
    resp, msg = initiate_auth(client_id, user_infor['username'], user_infor['password'])
    print(resp)
    
    if msg is not None:
        message = "Login fail!"
        statusCode = 400
    elif resp["AuthenticationResult"]:
         message = "Login sccessful!"
         statusCode = 200
    else:
        message = "Login fail!"
        statusCode = 400


    # TODO implement
    return {
            'statusCode': statusCode,
            'body': message,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,X-Access-Token, XKey, Authorization",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS"
            }
    }
