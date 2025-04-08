from helper import sendResponse, handle_bad_request,sendResponseByStatus,getMessage
from flask import Flask ,request ,jsonify
from functools import wraps
from services.query import getOneQuery 
from helper import set_cookie_value,get_cookie_value,verifyToken
import os
def is_user_logged_in(roles,data,message):
        try:
            cookie= get_cookie_value(request,'loggedIn')
            if(int(cookie) == 1):
                return check_role(roles,message,data)
            else:
                return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
        except Exception as e:
            return handle_bad_request(e)
            

def check_role(role=None,cursor=None):
    def decrorate_role(func):
        @wraps(func)
        def wrapper(args,**kwargs):
             sql_check="SELECT * from  users WHERE pubic_id = %s AND role = %s"
             values=(args['public_id'],role)
             data=getOneQuery(cursor,sql_check,values)
             if not data:
                return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
             return func(**kwargs)
        return wrapper
    return decrorate_role
        


def require_authentication(func):
    @wraps(func)
    def wrapper(**kwargs):
        print(request.headers)
        if "Authorization" not in request.headers:
            return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
        obj= verifyToken(request.headers['Authorization'])
        if not obj:
            return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
        return func(obj, **kwargs)
    return wrapper

def validateUserToken(token):
    # basic placeholder logic
    if token == "valid_token":
        return {"userid": 123}
    raise Exception("Invalid token")
