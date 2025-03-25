from helper import getMessage,sendResponse,handle_bad_request
from flask import Flask ,request ,jsonify
from middleware.middleware import validateUserToken
import os

def addProduct(token,name,qty):
    try:
        print(token)
        return validateUserToken(token,{"name":name,"qty":qty},"product added")
    except Exception as e:
        return handle_bad_request(e)
