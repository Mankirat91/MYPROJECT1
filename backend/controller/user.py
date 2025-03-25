from helper import getMessage,sendResponse,handle_bad_request,set_cookie_value,decrypt,generateToken
from flask import Response ,jsonify,json,make_response
import os
from services.query import getOneQuery,executeQuery 

def userLogin(data,connect):
    try:
        #result=getOneQuery('SELECT email from users WHERE email={email}'.format(email=data['email']),connect)
        if data['email'] != os.getenv('EMAIL'):
             raise Exception(getMessage('EMAIL_INCORRECT'))
#        if decrypt(data['password'],os.getenv('CRYPTO_KEY')) != os.getenv('PASSWORD'):
 #           raise Exception(getMessage('PASSWORD_INCORRECT'))
        token=generateToken("mankirat")
        print(token)
        #executeQuery('UPDATE users {token} VALUES (tokens) WHERE email={email}'.format(email=data['email'],token=token),connect)
        return set_cookie_value({"message":"used is loggedIn","token":token,"status":200},200,'role',"2")
    except Exception as e:
        return handle_bad_request(e)

def validateUserPassword(json):
    return "Hello from controler "+json['username']