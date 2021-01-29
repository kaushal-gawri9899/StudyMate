import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('StudyMate')
    
    response = table.get_item(
        Key={
            'email': event["email"]
        })
    
    item = response['Item']
    # print(item)
    
    return {
        "error": False,
        "success": True,
        "data": response["Item"],
        "message": "Call Successful",
        
    } 
    