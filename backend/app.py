from flask import Flask ,request ,json
from flaskext.mysql import MySQL
import os
from helper import getMessage,sendResponseByStatus,handle_bad_request
from controller.user import userLogin,addUser,getUser,getUsers,updateUser
from controller.product import addProduct
from model.user import userSchema,UserSchemaAddUser,UserSchemaUpdateUser
import pymysql.cursors
from migration import userMigation
from middleware.middleware import require_authentication,check_role

app=Flask(__name__)
mysql = MySQL(app,host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASSWORD'),db=os.getenv('DB_NAME'), autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql.init_app(app)
cursor =mysql.get_db().cursor()
with app.app_context():
   
    userMigation(mysql,cursor)

def createServer():
    print("Server")
    
@app.route('/auth/login', methods=['POST'])

def auth_login():
    try:
        if request.method == "POST":
            data =json.loads(request.data)
            result = userSchema.load(data)
            return userLogin(cursor,result)
    except Exception as e:
        return handle_bad_request(e)


@app.route('/user/add', methods=['POST'])
@require_authentication
@check_role(os.getenv('ROLE'),cursor)

def user_add():
    try:
        if request.method == "POST":
            data =json.loads(request.data)
            result = UserSchemaAddUser.load(data)
            return addUser(mysql,cursor,result)
    except Exception as e:
        return handle_bad_request(e)
    

@app.route('/user/<userid>', methods=['GET'])
@require_authentication
@check_role(os.getenv('ROLE'),cursor)
def user_get(userid):
    try:
        if request.method == "GET":
            return getUser(cursor,userid)
    except Exception as e:
        return handle_bad_request(e)
    

@app.route('/user/update/<userid>', methods=['PUT'])
@require_authentication
@check_role(os.getenv('ROLE'),cursor)
def user_update(userid):
    try:
        if request.method == "PUT":
            data['userid'] =userid
            data =json.loads(request.data)
            return updateUser(mysql,cursor,data,userid)
    except Exception as e:
        return handle_bad_request(e)
    
@app.route('/user/delete/:userid', methods=['DELETE'])
@require_authentication   
@check_role(os.getenv('ROLE'),cursor)
def user_delete(userid):
    try:
        if request.method == "DELETE":
            return addUser(mysql,cursor,userid)
    except Exception as e:
        return handle_bad_request(e)
    

@app.route('/users', methods=['GET'])
@require_authentication
@check_role(os.getenv('ROLE'),cursor)
def users_get():
    try:
        if request.method == "GET":
            return getUsers(cursor)
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




