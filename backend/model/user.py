from db import dbQuery
import os
from server import connectDb
from helper import encrypt,decrypt

class User:
    def __init__(self,email,password):
        db=connectDb()
        self.db=db
        qry = 'CREATE TABLE Users ( id int PRIMARY, email varchar(255), password varchar(2000) )'
        dbQuery(qry,self.db)   
        print("User table created succesfully")
    
    def createSuperUser(self):
        qry = 'INSERT INTO USERS SET email = {self.email} , password = {encrypt(self.password,os.getenv("CRYPTO_KEY"))}'
        dbQuery(qry,self.db)
    

user=User(os.getenv('EMAIL'),os.getenv('PASSWORD'))
user.createSuperUser()