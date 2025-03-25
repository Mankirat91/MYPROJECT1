from flask import Flask ,request ,json
from werkzeug.exceptions import Conflict, BadRequest
import os
from helper import getMessage,sendResponseByStatus,handle_bad_request
from controller.user import userLogin
from controller.product import addProduct
from model.user import userSchema
from db import getConnection
from migration import userMigation

app=Flask(__name__)
connect=getConnection(os.getenv('DB_HOST'),os.getenv('DB_USER'),os.getenv('DB_PASSWORD'),os.getenv('DB_NAME'))
userMigation(connect)

def createServer():
    print("Server")
    
@app.route('/auth/login', methods=['POST'])


def auth_login():
    try:
        if request.method == "POST":
            data =json.loads(request.data)
            result = userSchema.load(data)
            return userLogin(result,connect)
    except Exception as e:
        return handle_bad_request(e)

@app.route('/product/add', methods=['POST'])

def add_product():
    try:

        if request.method == "POST":
            json = request.get_json()
            header=dict(request.headers)
            if 'Authorization' not in header:
               return sendResponseByStatus(getMessage('UNAUTHORIZED'),401)
            return addProduct(header['Authorization'],json['name'],json['qty'])
    except Exception as e:
        return handle_bad_request(e)




