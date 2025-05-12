from flask import Flask ,request ,json, render_template,session,redirect
import os
from helper import handle_bad_request
from controller.web.user import userLogin,addUser,getUser,getUsersWithPagination,updateUser,deleteUser,getCurrentUser,activeDeativeUser
from controller.web.customer import addCustomer, getCustomersWithPagination,updateCustomer

from controller.web.category import getCategorysWithPagination,addCategory,deleteCategory,updateCategory,activeDeativeCategory,getCategory

from model.user import userSchema,UserSchemaAddUser,UserSchemaUpdateUser,UserSchemaDeleteUser
from model.customer import CustomerSchemaAddCustomer,CustomerSchemaUpdateCustomer
from model.category import CategorySchemaAddcategory,CategorySchemaDeletecategory,CategorySchemaUpdatecategory

from middleware.middleware import require_authentication,check_role,require_session_authentication,require_session_non_authentication
def UserWebRoutes(app,mysql,cursor):
        @app.route('/', methods=['GET'])
        @require_session_non_authentication
        def home():
            try:
                return redirect('/auth/login');
            except Exception as e:
                return handle_bad_request(e)

        @app.route('/auth/login', methods=['POST','GET'])
        @require_session_non_authentication
        def auth_login():
            try:
                if request.method == "POST":
                    data =request.form
                    result = userSchema.load(data)
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
                         result=getUsersWithPagination(limit,page,cursor)
                         user=getCurrentUser(cursor)
                         return render_template('/app/user/users.html',page='users',result=result,user=user , modal_title="Update User",modal_body="Are you sure ?")
            except Exception as e:
                return handle_bad_request(e)
            
            
        @app.route('/app/user/add', methods=['GET','POST'])
        @require_session_authentication
        def app_user_add():
            try:
                    user=getCurrentUser(cursor)
                    if request.method == "GET":
                        return render_template('/app/user/add_user.html',page='add user',action='/app/user/add',method="POST", user=user,data='')
                    if request.method == "POST":
                        data =request.form
                        result = UserSchemaAddUser.load(data)
                        return addUser(mysql,cursor,result, user=user,page='add user',action='/app/user/add',method="POST")
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
                    data=getUser(cursor,user_id)
                    user=getCurrentUser(cursor)
                    return render_template('/app/user/add_user.html',page='update user',action='/app/user/update/'+user_id,method="POST", user=user,data=data)
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
        
        @app.route('/app/user/active/<user_id>', methods=['PUT'])
        @require_session_authentication
        def user_active_deactive(user_id):
            try:
                if request.method == "PUT":
                    data =request.get_json(force=True)
                    UserSchemaUpdateUser.load(data)
                    return activeDeativeUser(mysql,cursor,user_id,data['is_active'])
            except Exception as e:
                return handle_bad_request(e)
            

        @app.route('/app/user/delete/<user_id>', methods=['DELETE'])
        @require_session_authentication 
        def user_delete(user_id):
            try:
                if request.method == "DELETE":
                    result = UserSchemaDeleteUser.load({"user_id":user_id})
                    return deleteUser(mysql,cursor,result)
            except Exception as e:
                return handle_bad_request(e)
            
        # categories routes
def CategoryWebRoutes(app,mysql,cursor):
        @app.route('/app/categories', methods=['GET'])
        @require_session_authentication
        def app_categories():
            try:
                    if request.method == "GET":
                         limit = request.args.get('limit')
                         page = request.args.get('page')
                         result=getCategorysWithPagination(limit,page,cursor)
                         user= getCurrentUser(cursor)
                         return render_template('/app/category/categories.html',page='categories',result=result,user=user , modal_title="Update Category",modal_body="Are you sure ?")
            except Exception as e:
                return handle_bad_request(e)

        @app.route('/app/category/add', methods=['GET','POST'])
        @require_session_authentication
        def app_category_add():
            try:
                    user=getCurrentUser(cursor)
                    if request.method == "GET":
                        return render_template('/app/category/add_category.html',page='add category',action='/app/category/add',method="POST", user=user,data='')
                    if request.method == "POST":
                        data =request.form
                        result = CategorySchemaAddcategory.load(data)
                        return addCategory(mysql,cursor,result,request.files, user=user,page='add category',action='/app/category/add',method="POST")
            except Exception as e:
                return handle_bad_request(e)
            
        
        @app.route('/app/category/edit/<category_id>', methods=['GET'])
        @require_session_authentication
        def category_get(category_id):
            try:
                if request.method == "GET":
                    data=getCategory(cursor,category_id)
                    user=getCurrentUser(cursor)
                    return render_template('/app/category/add_category.html',page='update category',action='/app/category/update/'+category_id,method="POST", user=user,data=data)
            except Exception as e:
                return handle_bad_request(e)
            

        @app.route('/app/category/update/<category_id>', methods=['POST'])
        @require_session_authentication
        def category_update(category_id):
            try:
                if request.method == "POST":
                    data =request.form
                    result = CategorySchemaUpdatecategory.load(data)
                    return updateCategory(mysql,cursor,result,request.files,category_id)
            except Exception as e:
                return handle_bad_request(e)
        
        @app.route('/app/category/active/<category_id>', methods=['PUT'])
        @require_session_authentication
        def category_active_deactive(category_id):
            try:
                if request.method == "PUT":
                    data =request.get_json(force=True)
                    CategorySchemaUpdatecategory.load(data)
                    return activeDeativeCategory(mysql,cursor,category_id,data['is_active'])
            except Exception as e:
                return handle_bad_request(e)
            

        @app.route('/app/category/delete/<category_id>', methods=['DELETE'])
        @require_session_authentication 
        def category_delete(category_id):
            try:
                if request.method == "DELETE":
                    result = CategorySchemaDeletecategory.load({"category_id":category_id})
                    return deleteCategory(mysql,cursor,result)
            except Exception as e:
                return handle_bad_request(e)
            

        
def CustomerWebRoutes(app,mysql,cursor):
        @app.route('/app/customers', methods=['GET'])
        @require_session_authentication
        def app_customers():
            try:
                    limit = request.args.get('limit')
                    page = request.args.get('page')
                    result=getCustomersWithPagination(cursor,limit,page)
                    user=getCurrentUser(cursor)
                    return render_template('/app/customer/customers.html',page='customers',result=result,user=user , modal_title="Update Category",modal_body="Are you sure ?")
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



