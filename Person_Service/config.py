import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myApp = Flask(__name__)
myApp.config['HOST'] = '0.0.0.0'
myApp.config['PORT']=8000
myApp.config['DEBUG'] = True
myApp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myApp.db"
myApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# mysql://<username>:<password>@<host>/<db_name>

db = SQLAlchemy(myApp)