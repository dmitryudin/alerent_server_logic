from app import app
from flask import request
import json



@app.route('/client/registration', methods=['GET', 'POST'])
def client_registration():
    d = json.loads(request.get_data().decode('utf-8'))
    print(d)
    return 'Hello World!'


@app.route('/client/login')
def client_login():
    return 'Hello World!'


@app.route('/client/edit_profile')
def client_edit_profile():
    return 'Hello World!'


@app.route('/client/get_profile', methods=['GET', 'POST'])
def client_get_profile():
    return 'Hello World!'