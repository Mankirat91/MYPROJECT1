from helper import getMessage,sendResponse,handle_bad_request,set_cookie_value,decrypt,generateToken
from flask import render_template,session,redirect,flash
import os
import uuid
from helper import encrypt
from services.query import getOneQuery,insertQuery ,getAllQueryWithCondition,execQuery


def addCategory(mysql,cursor,data,category,page,action,method):
    try:
        result=getOneQuery(cursor,'SELECT name from categories WHERE name=%s',(data['name']))
        if not result:
             qry='INSERT into  categories  (name,link,image) VALUES (%s,%s,%s)'
             values=(data['name'],data['link'],data['image'])
             insertQuery(mysql,cursor,qry,values)
             result=getOneQuery(cursor,'SELECT name from categories WHERE name=%s',(data['name']))
             flash(getMessage('CATEGORY_ADDED_SUCCESSFULLY') )
             return redirect('/app/categories')
        return render_template('/app/category/add_category.html',message=getMessage('CATEGORY_ALREADY_EXISTS') , success=False,category=category,data='',page=page,action=action,method=method)
    except Exception as e:
        return handle_bad_request(e)
    

def updateCategory(mysql,cursor,data,category_id):
    try:
        print(data)
        if "email" in data:
            result=getOneQuery(cursor,'SELECT name from categories WHERE name=%s AND id != %s',(data['name'],category_id))
            if  result:
                return render_template('/app/category/add_category.html',message=getMessage('EMAIL_ALREADY_EXISTS') , success=False )
        fields=''
        for k, v in data.items():
            if k == 'password':
                v = encrypt(v,os.getenv('CRYPTO_KEY'))
            fields += k + '="'+v+'",'
        result=execQuery(mysql,cursor,'UPDATE  categories  SET '+fields.rstrip(',')+' WHERE id=%s',(category_id))
        flash(getMessage('CATEGORY_UPDATED_SUCCESSFULLY') )
        return redirect('/app/categories')
    except Exception as e:
        return handle_bad_request(e)
    

def activeDeativeCategory(mysql,cursor,category_id,is_active):
    try:
        result=getOneQuery(cursor,'SELECT name from categories WHERE id = %s',(category_id))
        if  result:   
            result=execQuery(mysql,cursor,'UPDATE  categories  SET is_active=%s WHERE id=%s',(is_active,category_id))
            flash(getMessage('CATEGORY_UPDATED_SUCCESSFULLY'))
            return {"updated":True }
        flash(getMessage('CATEGORY_NOT_FOUND') )
        return {"updated":False }
    except Exception as e:
        return handle_bad_request(e)
    

def deleteCategory(mysql,cursor,data):
    try:
        exist=getOneQuery(cursor,'SELECT name from categories WHERE id=%s',(data['category_id']))
        if exist:
             exist=execQuery(mysql,cursor,'DELETE from categories WHERE id=%s',(data['category_id']))
             flash(getMessage('CATEGORY_DELETED_SUCCESSFULLY') )
             return redirect('/app/categories')
        raise Exception(getMessage('CATEGORY_NOT_FOUND'))
    except Exception as e:
        return handle_bad_request(e)    
    

def getCategory(cursor,categoryid):
    try:
        result=getOneQuery(cursor,'SELECT id,name,image,link from categories WHERE id=%s',(categoryid))
        if not result:
            raise Exception(getMessage('CATEGORY_NOT_FOUND'))
        return result
    except Exception as e:
        return handle_bad_request(e)
    

def getCategorysWithPagination(limit,page,cursor):
    try:
        if limit == None:
           limit = 10
        if page == None:
           page = 1
        offset=int(limit)*int(page)-int(limit)
        print(offset)
        total=getAllQueryWithCondition(cursor,'SELECT COUNT(*) from categories',(""))
        print(total)
        data=getAllQueryWithCondition(cursor,'SELECT id,name,link,image , is_active from categories  LIMIT %s OFFSET %s',(int(limit),int(offset)))
        print(data)
        if not data:
            message=getMessage('CATEGORY_NOT_FOUND')
            return message
        result = { "data":data,"page":page,"limit":limit,"total":total[0]['COUNT(*)'],"totalPages":offset}
        return result
    except Exception as e:
        return handle_bad_request(e)
    
def getCurrentCategory(cursor):
    public_id=session.get("public_id")
    user=getOneQuery(cursor,'SELECT * from categories WHERE pubic_id=%s',(public_id))
    return user
    

    
