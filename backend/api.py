from flask import request ,render_template
from flask_cors import cross_origin
from helper import getMessage,sendResponseByStatus,handle_bad_request
from controller.api.customer import customerLogin,customerRegister
from model.customer import CustomerSchema,CustomerSchemaAddCustomer
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
        
    





