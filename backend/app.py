from flask import Flask ,request ,jsonify
from werkzeug.exceptions import Conflict, BadRequest
from controller.user import getUser
import os
from dotenv import load_dotenv

app=Flask(__name__)

def createServer():
    print("Server")
    
@app.route('/home', methods=['POST','GET'])
def homeRoute():
    try:
        if request.method == "POST":
            json = request.get_json()
            if not json:
                raise Exception("Invalid JSON INPUT") 
            return getUser(json)
        if request.method == "GET":
            return "Hi"
    except Exception as e:
        return handle_bad_request(e)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    data =jsonify({"message":e.args[0]})
    return data , 400

app.register_error_handler(400, handle_bad_request)


#rep converts object to array
#MVC  middleware(authentication handling , token management , roles handling)
#Cookies Session Local Storage + Device Attributes(Device number , mac address , model number) 
#Device Cache Management(Queue techinque data striucture) , sockets(Chat)
#API ->Server ->Route ->(middlware validation)-> Controller ->Model
#Routing used to interact with server through a web link