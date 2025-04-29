from helper import getMessage,sendResponse,handle_bad_request
from flask import Flask ,request ,jsonify
import os

def addProduct(token,name,qty):
    try:
        print(token)
    except Exception as e:
        return handle_bad_request(e)
