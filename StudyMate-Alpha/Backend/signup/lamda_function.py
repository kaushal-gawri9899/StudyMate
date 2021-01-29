import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json

USER_POOL_ID = 'ap-south-1_JH23M6rlh'
CLIENT_ID = '6hm3sm57aquuqgtckfb8l7ld9q'
CLIENT_SECRET = 'jl7kkkcpm1e3vah4qbgkv9drrucovmkqlvhiq82v23kgrb42jls'

def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

def lambda_handler(event, context):     
    for field in ["username", "email", "password", "name","phone_number"]:
        if not event.get(field):
            return {
                "error": False, 
                "success": True, 
                'message': field+ " is not present", 
                "data": None}
    
    username = event['username']
    email = event['email']
    password = event['password']
    name = event['name']   
    phone_number = event['phone_number']
    university = event['university']
    organization = event['organization']
    #university = ""
    #organization = ""
    client = boto3.client('cognito-idp')    
    
    try:
        resp = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password, 
            UserAttributes=[
            {
                'Name': "name",
                'Value': name
            },
            {
                'Name': "email",
                'Value': email
            },
            {
                'Name': "phone_number",
                'Value': phone_number
            },
            {
                'Name': "custom:university",
                'Value': university
            },
            {
                'Name': "custom:organization",
                'Value': organization
            }
            
            ],
            ValidationData=[
                {
                'Name': "email",
                'Value': email
                },
                {
                'Name': "custom:username",
                'Value': username
                },
                {
                'Name': "phone_number",
                'Value': phone_number
                },
                {
                'Name': "custom:university",
                'Value': university
                },
                {
                'Name': "custom:organization",
                'Value': organization
                }

            ])
    
    
    except client.exceptions.UsernameExistsException as e:
        return {"error": False, "success": True, 
        "message": "This username already exists", 
              "data": None}   
               
    except client.exceptions.InvalidPasswordException as e:
        
        return {"error": False, 
              "success": True, 
              "message": "Password should have Caps,\
                          Special chars, Numbers", 
              "data": None}    
    
    except client.exceptions.UserLambdaValidationException as e:
        return {"error": False,"success": True,"message": "Email already exists","data": None}
    
    except Exception as e:
        return {"error": False, 
              "success": True, 
              "message": str(e), 
              "data": None}
    
    return {"error": False, 
           "success": True, 
           "message": "Please confirm your signup, \
                        check Email for validation code", 
           "data": None}