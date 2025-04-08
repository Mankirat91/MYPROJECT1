from services.query import insertQuery,getOneQuery
from helper import handle_bad_request
import os
from helper import encrypt

def userMigation(mysql,cursor):
    try:
        sql_check="SELECT email from  users WHERE email = %s"
        values=(os.getenv('EMAIL'))
        data=getOneQuery(mysql,cursor,sql_check,values)
        if  data == None:
             sql2='INSERT into  users  (email,password) VALUES (%s,%s)'
             values=(os.getenv('UUID'),os.getenv('FIRST_NAME'),os.getenv('LAST_NAME'),os.getenv('EMAIL'), encrypt(os.getenv('PASSWORD'),os.getenv('CRYPTO_KEY')))
             insertQuery(mysql,cursor,sql2,values)
             print("User migration done successfully") 
        else:
             print("User migration already done") 
    except Exception as e:
        print(e)
        return handle_bad_request(e)