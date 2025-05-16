from helper import getMessage,handle_bad_request
from flask import render_template,redirect,flash
import os
from middleware.middleware import allowed_file
from helper import encrypt,get_time_stamp,get_extension
from services.query import getOneQuery,insertQuery ,getAllQueryWithCondition

def addProduct(mysql,cursor,data,files, user,page,action,method):
    try:
        if 'thumb_image' not in files:
            flash(getMessage('CATEGORY_IMAGE_NOT_FOUND'))
        if 'full_image' not in files:
            flash(getMessage('CATEGORY_IMAGE_NOT_FOUND'))
        thumb_file = files['thumb_image']
        full_image = files['full_image']
        if thumb_file.filename == '':
            flash(getMessage('CATEGORY_IMAGE_NOT_FOUND'))
        if thumb_file and allowed_file(thumb_file.filename):
            ext=get_extension(thumb_file.filename)
            filename=get_time_stamp()
            current_dir = os.getcwd()
            thumb_file.save(os.path.join(current_dir + os.getenv('UPLOAD_FOLDER_PRODUCT')+'/thumb' ,str(filename)+'.'+ext))
        result=getOneQuery(cursor,'SELECT name from products WHERE name=%s',(data['name']))
        if not result:
             name=data['name']
             category_id=data['category_id']
             qry='INSERT into  products  (name,link,image,category_id) VALUES (%s,%s,%s,%s)'
             values=(name,name.replace(" ", "-").lower(),str(filename)+'.'+ext,category_id)
             insertQuery(mysql,cursor,qry,values)
             result=getOneQuery(cursor,'SELECT name from categories WHERE name=%s',(data['name']))
             flash(getMessage('CATEGORY_ADDED_SUCCESSFULLY') )
             return redirect('/app/categories')
        return render_template('/app/category/add_category.html',message=getMessage('CATEGORY_ALREADY_EXISTS') , success=False,user=user,data='',page=page,action=action,method=method)
    except Exception as e:
         return render_template('/app/category/add_category.html',message=e.args[0], success=False,user=user,data='',page=page,action=action,method=method)

def getProductsWithPagination(limit,page,cursor):
    try:
        if limit == None:
           limit = 10
        if page == None:
           page = 1
        offset=int(limit)*int(page)-int(limit)
        total=getAllQueryWithCondition(cursor,'SELECT COUNT(*) from products',())
        data=getAllQueryWithCondition(cursor,'SELECT * from products  LIMIT %s OFFSET %s ',(int(limit),int(offset)))
        result = { "data":data,"page":page,"limit":limit,"total":total[0]['COUNT(*)'],"totalPages":offset}
        return result
    except Exception as e:
        print(e)
        return handle_bad_request(e)