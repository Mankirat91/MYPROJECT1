from services.query import executeQuery,getOneQuery
from helper import handle_bad_request
import os
from helper import encrypt

def userMigation(connect):
    try:
        sql1='SELECT email from  users WHERE email = "{email}"'.format(email=os.getenv('EMAIL'))
        data=getOneQuery(connect,sql1)
        if  data == None:
             sql='INSERT into  users  (email,password) VALUES ("{email}" ,"{password}")'.format(email=os.getenv('EMAIL'), password=encrypt(os.getenv('PASSWORD'),os.getenv('CRYPTO_KEY')))
             print(sql)
             executeQuery(connect,sql)
             print("User migration done successfully") 
        else:
             print("User migration already done") 
    except Exception as e:
        return handle_bad_request(e)