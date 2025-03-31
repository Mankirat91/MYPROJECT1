
from services.query import executeQuery,getOneQuery
from helper import handle_bad_request , encrypt
import os
 

def userMigation(connect):
    try:
        
        sql1='SELECT email from  users WHERE email = "{email}"'.format(email=os.getenv('EMAIL'))
        data=getOneQuery(connect,sql1)
        print(data)
        if not data:
             
             password = encrypt(os.getenv('PASSWORD'),os.getenv('CRYPTO_KEY'))
             sql='INSERT into  users  (email,password) VALUES ("{email}" ,"{password}")'.format(email=os.getenv('EMAIL'), password= password)
             print(sql)
             executeQuery(connect,sql)
             print("User migration done successfully") 
        else:
             print("User migration already done") 
    except Exception as e:
        
        return handle_bad_request(e)