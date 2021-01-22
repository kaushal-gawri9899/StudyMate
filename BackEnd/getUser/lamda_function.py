import boto3
import botocore.exceptions
import json
import logging

USER_POOL_ID = 'ap-south-1_JH23M6rlh'

def error_message(msg):
    return {'message': msg, "error": True, "success": False, "data": None}
    
def lambda_handler(event, context):
    
    print("Test Logger")
    for field in ["username"]:
        if event.get(field) is None:
            return error_message("Please provide All details to renew tokens")
    
    client = boto3.client('cognito-idp')
    try:
        
        #$$if you want to get user from users access_token
        # response = client.get_user(
        #   AccessToken=event["access_token"])
        
        response = client.admin_get_user(
                UserPoolId=USER_POOL_ID,
                Username=event["username"]
            )
        
        #label = json.loads(response.text)
        print(response)
        
            
   
    
    except client.exceptions.UserNotFoundException as e:
        return error_message("Invalid username ")
    
    #print("Reached")
    # print(response["UserAttributes"])
     
    return {
        "error": False,
        "success": True,
        "data": response["UserAttributes"],
        "message": "Call Successful",
        
    }    