import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('StudyMate')
    
    table.update_item(
        Key={
            'email': event['email']
        },
        UpdateExpression='SET organization = :val1',
        ExpressionAttributeValues={
            ':val1': event['new_organization']
        }
    )
    
