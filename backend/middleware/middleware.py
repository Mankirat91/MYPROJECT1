from helper import sendResponse, handle_bad_request,sendResponseByStatus,getMessage
from flask import Flask ,request ,jsonify,session,redirect
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
             sql_check="SELECT * from  users WHERE  role = %s"
             values=(role)
             data=getOneQuery(cursor,sql_check,values)
             if not data:
                return redirect('/auth/login') 
             return func(args,**kwargs)
        return wrapper
    return decrorate_role
        


def require_authentication(func):
    @wraps(func)
    def wrapper(**kwargs):
        if "Authorization" not in request.headers:
            return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
        obj= verifyToken(request.headers['Authorization'])
        if not obj:
            return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
        return func(obj, **kwargs)
    return wrapper



def require_session_authentication(func):
    @wraps(func)
    def wrapper(**kwargs):
        public_id=session.get("public_id")
        if public_id:
            return func( **kwargs) 
        else:
            return redirect('/auth/login') 
    return wrapper


def require_session_non_authentication(func):
    @wraps(func)
    def wrapper(**kwargs):
        public_id=session.get("public_id")
        if public_id:
             return redirect('/app/dashboard') 
        else:
            return func( **kwargs) 
        
    return wrapper

