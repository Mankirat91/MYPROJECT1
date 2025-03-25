from db import dbQuery
import os
from marshmallow import Schema, fields
from helper import encrypt,decrypt

class UserSchema(Schema):
      email = fields.Email(required=True,error_messages={"required": "Email is required"})
      password = fields.String(required=True)


class UserModel():
      def __init__(self,email,password,first_name,last_name):
         self.first_name=first_name
         self.email=email
         self.password=password
         self.last_name=last_name

userSchema=UserSchema()
