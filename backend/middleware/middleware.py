from helper import sendResponse, handle_bad_request,sendResponseByStatus,getMessage
from flask import Flask ,request ,jsonify
from helper import set_cookie_value,get_cookie_value

def isUserLoggedIn(roles,data,message):
     try:
        cookie= get_cookie_value(request,'loggedIn')
        if(int(cookie) == 1):
           return checkRole(roles,message,data)
        else:
           return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
     except Exception as e:
        return handle_bad_request(e)

def checkRole(roles,message,data):
    try:
        cookie= get_cookie_value(request,'role')
        if int(cookie) in roles:
            return sendResponse(message,data)
        else:
            return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
    except Exception as e:
        return handle_bad_request(e)


#next response sending