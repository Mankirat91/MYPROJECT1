from helper import getMessage,sendResponse,handle_bad_request,set_cookie_value,decrypt,generateToken
import os
import uuid
from helper import encrypt
from services.query import getOneQuery,insertQuery ,getAllQueryWithCondition,execQuery

def userLogin(cursor,data):
    try:
        values=(data['email'])
        result=getOneQuery(cursor,'SELECT * from users WHERE email=%s',values)
        if not result:
             raise Exception(getMessage('EMAIL_INCORRECT'))
        if decrypt(result['password'],os.getenv('CRYPTO_KEY')) != data['password']:
            raise Exception(getMessage('PASSWORD_INCORRECT'))
        token=generateToken(result['pubic_id'])
        return set_cookie_value({"message":"used is loggedIn","data":dict({"id":result['id'],"email":result['email']}),"token":token,"status":200},200,'role',"2")
    except Exception as e:
        return handle_bad_request(e)

def addUser(mysql,cursor,data):
    try:
        result=getOneQuery(cursor,'SELECT email from users WHERE email=%s',(data['email']))
        if not result:
             qry='INSERT into  users  (first_name,last_name,email,pubic_id,role,password) VALUES (%s,%s,%s,%s,%s,%s)'
             values=(data['first_name'],data['last_name'],data['email'],uuid.uuid4(),2, encrypt(data['password'],os.getenv('CRYPTO_KEY')))
             insertQuery(mysql,cursor,qry,values)
             result=getOneQuery(cursor,'SELECT email from users WHERE email=%s',(data['email']))
             return sendResponse(getMessage("USER_ADDED_SUCCESSFULLY"),result)
        raise Exception(getMessage('EMAIL_ALREADY_EXISTS'))
    except Exception as e:
        return handle_bad_request(e)
    

def updateUser(mysql,cursor,data,userid):
    try:
        result=getOneQuery(cursor,'SELECT email from users WHERE email=%s AND id != %s',(data['email'],userid))
        if result:
             print(data)
             # keys=
             qry='UPDATE  users set (first_name,last_name,email,pubic_id,role,password) VALUES (%s,%s,%s,%s,%s,%s)'
             values=(data['first_name'],data['last_name'],data['email'],uuid.uuid4(),2, encrypt(data['password'],os.getenv('CRYPTO_KEY')))
             insertQuery(mysql,cursor,qry,values)
             result=getOneQuery(cursor,'SELECT email from users WHERE email=%s',(data['email']))
             return sendResponse(getMessage("USER_UDATED"),result)
        raise Exception(getMessage('EMAIL_ALREADY_EXISTS'))
    except Exception as e:
        return handle_bad_request(e)
    
def delete_user(mysql,cursor,data):
 try:
    result=getOneQuery(cursor,'SELECT email from users WHERE email != %s',(data['email']))
    if not result:
        qry = 'DELETE from users where email = %s',(data['email'])
        execQuery(mysql,cursor,qry)
        return sendResponse(getMessage("USER_DELETED"))
    raise Exception(getMessage("EMAIL_DON'T_EXISTS"))    
 except Exception as e:
     handle_bad_request(e)

def getUser(cursor,userid):
    try:
        result=getOneQuery(cursor,'SELECT id,email from users WHERE id=%s',(userid))
        if not result:
            raise Exception(getMessage('USER_NOT_FOUND'))
        return sendResponse("",result)
    except Exception as e:
        return handle_bad_request(e)
    

def getUsers(cursor):
    try:
        result=getAllQueryWithCondition(cursor,'SELECT email,first_name,last_name,role from users WHERE role != %s',(os.getenv('ROLE')))
        if not result:
            raise Exception(getMessage('USER_NOT_FOUND'))
        return sendResponse("",result)
    except Exception as e:
        return handle_bad_request(e)
    

    

    
