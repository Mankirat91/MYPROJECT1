from flask import Flask 
from flaskext.mysql import MySQL
from migration import userMigation,countryMigation,customerMigration,categoryMigration,productMigration,reviewMigration

from flask_cors import CORS
import os
import pymysql.cursors
from web import UserWebRoutes,CustomerWebRoutes
from api import ApiRoutes

app=Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "http://127.0.0.1:5500"}})
app.secret_key = os.getenv('SESSION_SECRET_KEY')
mysql = MySQL(app,host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASSWORD'),db=os.getenv('DB_NAME'), autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql.init_app(app)
with app.test_request_context():
    cursor =mysql.get_db().cursor()
    # userMigation(mysql,cursor)
    # countryMigation(mysql,cursor)
    # customerMigration(mysql,cursor)
    # categoryMigration(mysql,cursor)
    # productMigration(mysql,cursor)
    # reviewMigration(mysql,cursor)
    UserWebRoutes(app,mysql,cursor)
    CustomerWebRoutes(app,mysql,cursor)
    ApiRoutes(app,mysql,cursor)








