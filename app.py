#!/usr/bin/env python
# -*- coding: utf-8 -*-

from website import create_app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask import Flask, request

db = SQLAlchemy()

DB_NAME = "medicode.db"

# initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey?'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

response = ""

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    name = ""
    id_number = ""

    print(text)

    if text == '':
        response = "CON welcome to medicode \n"
        response += "1. Register"
    elif text == '1':
        response = "CON Please enter your name\n" 
        name = request.values.get("text", "")
        response += 
    elif text == "1*{}".format(name):
        response = "CON Please enter your ID\n"    
        id_number = request.values.get("text", "")
    elif text == "1*{}*{}".format(name, id_number):
        response = "CON Registration successful!\n"
        response += "Name: {}\n".format(name)
        response += "ID: {}\n".format(id_number)

   

    return response


if __name__ == '__main__':
    app.run(debug=True)
