#!/usr/bin/env python
# coding: utf-8

# In[64]:


import requests
import json


# In[65]:


r = requests.get("https://jjcldrtx87.execute-api.us-east-2.amazonaws.com/Beta/user/test")    


# In[68]:


r.json()


# In[ ]:


p = requests.post()


# In[95]:


#import boto3
#import botocore.exceptions
import hmac
import hashlib
import base64
import json

USER_POOL_ID = ''
CLIENT_ID = ''
CLIENT_SECRET = ''

def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

def lambda_handler(event, context):     
    for field in ["username", "email", "password", "name","phone_number"]:
        if not event.get(field):
            return {"error": False, "success": True, 'message': f"{field} is not present", "data": None}
    
    username = event['username']
    email = event["email"]
    password = event['password']
    name = event["name"]   
    phone_number = event["phone number"]
    university = event["custom:university"]
    organization = event["custom:organization"]
    
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
                'Name': "phone number",
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


# In[96]:


print('abc')


# In[141]:


import json
import requests
p = requests.post("https://jjcldrtx87.execute-api.us-east-2.amazonaws.com/Beta/user/signup", data=json.dumps({"username": "kaushal@gmail.com", "password": "Kaushal@9", "email": "kaushal@gmail.com", "name": "Kaushal", "phone_number": "+919654156957", "university": "RMIT", "organization": "Student"}))


# In[142]:


p.json()


# In[144]:


# import boto3
# import botocore.exceptions
# import json
USER_POOL_ID = 'us-east-2_19db3vq92'

def error_message(msg):
    return {'message': msg, "error": True, "success": False, "data": None}
    
def lambda_handler(event, context):
    for field in ["username"]:
        if event.get(field) is None:
            return error_message("Please provide" {field} to renew tokens")
    
    client = boto3.client('cognito-idp')
    try:
        
        #$$if you want to get user from users access_token
        # response = client.get_user(
        #   AccessToken=event["access_token"])
        
        response = client.admin_get_user(
                UserPoolId=USER_POOL_ID,
                Username=event["username"]
            )
            
    except client.exceptions.UserNotFoundException as e:
        return error_message("Invalid username ")
    
    return {
        "error": False,
        "success": True,
        "data": None,
        "message": "Call Successful",
        
    }    


# In[45]:


import json
import requests
c = requests.post("https://jjcldrtx87.execute-api.us-east-2.amazonaws.com/Beta/user/signup", data=json.dumps({"username": "gawrikaushal9899@gmail.com", "password": "Kaushal@9899", "code": "588120"}))


# In[46]:


c.json()


# In[49]:


import json
import requests
c = requests.post("https://jjcldrtx87.execute-api.us-east-2.amazonaws.com/Beta/user/confirm-sign-up", data=json.dumps({"username": "gawrikaushal9899@gmail.com", "password": "Kaushal@9899", "code": "588120"}))


# In[50]:


c.json()


# In[53]:


import json
import requests
s = requests.post("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/login", data=json.dumps({"username":"gawrikaushal9899@gmail.com", "password":"Kaushal@9899"}))


# In[54]:


s.json()


# In[69]:


import json
import requests
user = requests.post("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/get-user", data=json.dumps({"username":"gawrikaushal9899@gmail.com"}))


# In[70]:


user.json()


# In[64]:


import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
USER_POOL_ID = 'ap-south-1_JH23M6rlh'
CLIENT_ID = ''
CLIENT_SECRET =''

def error_message(msg):
    return {'message': msg, "error": True, "success": False, "data": None}
    
def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    
    return d2

def lambda_handler(event, context):
    for field in ["username", "refresh_token"]:
        if event.get(field) is None:
            return error_message(f"Please provide {field} to renew tokens")
   
    client = boto3.client('cognito-idp')
    
    username = event["username"]
   
    refresh_token = event["refresh_token"]
    
    secret_hash = get_secret_hash(username)
    try:
        resp = client.initiate_auth(
           AuthParameters={
                'USERNAME': username,
                'SECRET_HASH': secret_hash,
                'REFRESH_TOKEN': refresh_token,
             
            },
            ClientId=CLIENT_ID,
            AuthFlow='REFRESH_TOKEN_AUTH',
            )       
        
        res = resp.get("AuthenticationResult")  
            
    except client.exceptions.NotAuthorizedException as e:
        return error_message("Invalid refresh token or username is incorrect or Refresh Token has been revoked")
        
    except client.exceptions.UserNotConfirmedException as e:
        return error_message("User is not confirmed")
        
    except Exception as e:
        return error_message(e.__str__())    
    
    if res:
        return {'message': "success", 
                    "error": False, 
                    "success": True, 
                    "data": {
            "id_token": res["IdToken"],
            "access_token": res["AccessToken"], 
            "expires_in": res["ExpiresIn"],
            "token_type": res["TokenType"]
        }}   
    return


# In[119]:


import json
import requests
u = requests.get("https://ikwm7ce222.execute-api.ap-south-1.amazonaws.com/StudyMate-Beta/user/get-user", data=json.dumps({"username":"gawrikaushal9899@gmail.com"}))


# In[127]:


u.json()


# In[137]:


str = json.loads(u.text)


# In[138]:


print(str)


# In[131]:


data = json.dumps(str)


# In[132]:


print(data)


# In[158]:


# class User():
#     def __init__(self,name,username):
#         self.name = name
#         self.username = username
        
# user_object = User(**str)

#uni = str['data'][0]['Value']
#org = str['data'][1]['Value']
name = str['data'][4]['Value']
ph = str['data'][6]['Value']
email = str['data'][7]['Value']


# In[162]:


print(name)
print(ph)
print(email)


# In[ ]:




