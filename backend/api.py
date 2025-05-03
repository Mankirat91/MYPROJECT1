from flask import request ,render_template,jsonify
from flask_cors import cross_origin
from helper import getMessage,sendResponseByStatus,handle_bad_request
from controller.api.customer import customerLogin,customerRegister
from controller.web.user import userLogin,addUser
from model.customer import CustomerSchema,CustomerSchemaAddCustomer
from model.user import UserSchema,UserSchemaAddUser
from middleware.middleware import require_authentication,check_role,require_session_authentication,require_session_non_authentication

def ApiRoutes(app,mysql,cursor):
    @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
    @app.route('/api/customer/login', methods=['POST'])
    def customer_login():
        try:
                data = request.get_json()
                result = CustomerSchema.load(data)
                return customerLogin(cursor,result)
        except Exception as e:
            return handle_bad_request(e)
    

    @app.route('/api/customer/register', methods=['POST'])
    def customer_register():
        try:
                data = request.get_json()
                result = CustomerSchemaAddCustomer.load(data)
                return customerRegister(mysql,cursor,result)
        except Exception as e:
            print(e)
            return handle_bad_request(e)
        
    
    @app.route('/api/user/login',methods=['POST'])
    def user_login():
         try:
              data = request.get_json()
              result = UserSchema.load(data)
              return userLogin(cursor,result)
         except Exception as e:
        # This handles cases like empty body or non-JSON requests
                return jsonify({"message": str(e)}), 400
         except Exception as e:
              print(e)
              return handle_bad_request(e)
         
    @app.route('/api/user/register',methods = ['POST'])
    def user_register():
         try:
              data = request.get_json()
              result = UserSchemaAddUser.load(data)
              return addUser(mysql,cursor,result)
         except Exception as e:
              print(e)
              return handle_bad_request(e)




