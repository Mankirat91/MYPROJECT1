from flask import Flask ,request ,json, render_template,session,redirect
import os
from helper import handle_bad_request
from controller.web.user import userLogin,addUser,getUser,getUsersWithPagination,updateUser,deleteUser,getCurrentUser
from controller.web.customer import addCustomer, getCustomers,updateCustomer

from model.user import UserSchema,UserSchemaAddUser,UserSchemaUpdateUser,UserSchemaDeleteUser
from model.customer import CustomerSchema,CustomerSchemaAddCustomer,CustomerSchemaUpdateCustomer,CustomerSchemaDeleteCustomer
from middleware.middleware import require_authentication,check_role,require_session_authentication,require_session_non_authentication
def UserWebRoutes(app,mysql,cursor):
        @app.route('/', methods=['GET'])
        @require_session_non_authentication
        def home():
            try:
                return
            except Exception as e:
                return handle_bad_request(e)

        @app.route('/auth/login', methods=['POST','GET'])
        @require_session_non_authentication
        def auth_login():
            try:
                if request.method == "POST":
                    data =request.form
                    result = UserSchema.load(data)
                    return userLogin(cursor,result)
                if request.method == "GET":
                    return render_template('/auth/login.html')
            except Exception as e:
                return handle_bad_request(e)
    

        @app.route('/app/dashboard', methods=['GET'])
        @require_session_authentication
        def app_dashboard():
            try:    
                    user=getCurrentUser(cursor)
                    return render_template('/app/dashboard/dashboard.html',page='dashboard',user=user)
            except Exception as e:
                return handle_bad_request(e)
            
        @app.route('/app/users', methods=['GET'])
        @require_session_authentication
        def app_users():
            try:
                    if request.method == "GET":
                         limit = request.args.get('limit')
                         page = request.args.get('page')
                         print(limit)
                         result=getUsersWithPagination(limit,page,cursor)
                         user=getCurrentUser(cursor)
                         print(result)
                         return render_template('/app/user/users.html',page='users',result=result,user=user)
            except Exception as e:
                return handle_bad_request(e)
            
            
        @app.route('/app/user/add', methods=['GET','POST'])
        @require_session_authentication
        def app_user_add():
            try:
                    if request.method == "GET":
                        return render_template('/app/user/add_user.html',page='add user',action='/app/user/add',method="POST", user="")
                    if request.method == "POST":
                        data =request.form
                        result = UserSchemaAddUser.load(data)
                        return addUser(mysql,cursor,result)
            except Exception as e:
                return handle_bad_request(e)
            

            
        @app.route('/app/logout', methods=['GET'])
        @require_session_authentication
        def app_logout():
            try:
                session['public_id']='';
                return redirect('/auth/login')
            except Exception as e:
                return handle_bad_request(e)

            

        @app.route('/app/user/edit/<user_id>', methods=['GET'])
        @require_session_authentication
        def user_get(user_id):
            try:
                if request.method == "GET":
                    user=getUser(cursor,user_id)
                    return render_template('/app/user/add_user.html',page='update user',action='/app/user/update/'+user_id,method="POST", user=user)
            except Exception as e:
                return handle_bad_request(e)
            

        @app.route('/app/user/update/<user_id>', methods=['POST'])
        @require_session_authentication
        def user_update(user_id):
            try:
                if request.method == "POST":
                    data =request.form
                    result = UserSchemaUpdateUser.load(data)
                    return updateUser(mysql,cursor,result,user_id)
            except Exception as e:
                return handle_bad_request(e)
            

        @app.route('/app/user/delete/<user_id>', methods=['POST'])
        @require_session_authentication 
        def user_delete(user_id):
            try:
                if request.method == "POST":
                    result = UserSchemaDeleteUser.load({"user_id":user_id})
                    return deleteUser(mysql,cursor,result)
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
            
def CustomerWebRoutes(app,mysql,cursor):
        @app.route('/app/customers', methods=['GET'])
        @require_session_authentication
        def app_customers():
            try:
                    data=getCustomers(cursor)
                    return render_template('/app/customer/customers.html',page='customers',data=data)
            except Exception as e:
                return handle_bad_request(e)
            
            
        @app.route('/app/customer/add', methods=['GET','POST'])
        @require_session_authentication
        def app_customer_add():
            try:
                    if request.method == "GET":
                        return render_template('/app/customer/add_customer.html',page='add customer')
                    if request.method == "POST":
                        data =request.form
                        result = CustomerSchemaAddCustomer.load(data)
                        return addCustomer(mysql,cursor,result)
            except Exception as e:
                return handle_bad_request(e)
        
        @app.route('/app/customer/update/<customer_id>', methods=['GET','POST'])
        @require_session_authentication
        def app_customer_update():
            try:
                    if request.method == "GET":
                        return render_template('/app/customer/add_customer.html',page='update customer')
                    if request.method == "POST":
                        data =request.form
                        result = CustomerSchemaUpdateCustomer.load(data)
                        return updateCustomer(mysql,cursor,result)
            except Exception as e:
                return handle_bad_request(e)



