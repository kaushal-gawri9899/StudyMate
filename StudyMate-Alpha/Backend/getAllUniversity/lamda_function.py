import boto3
from boto3.dynamodb.conditions import Key, Attr 

import json

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("StudyMate")
    
    response = table.scan(
        FilterExpression=Attr('university').eq(event['university'])
        )
    
    items = response['Items']
    # print(items)

    return {
        "error": False,
        "success": True,
        "data": response['Items'],
        "message": "Call Successful",
    } 

