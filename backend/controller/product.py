from helper import getMessage,sendResponse,handle_bad_request
from flask import Flask ,request ,jsonify
from middleware.middleware import isUserLoggedIn
import os

def addProduct(name,qty):
    try:
        data= {"name":name,"qty":2}
        return isUserLoggedIn([1,2],getMessage('PRODCUT_ADDED_SUCCESSFULLY'),data)
    except Exception as e:
        return handle_bad_request(e)
