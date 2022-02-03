from app import app




@app.route('/client/registration')
def client_registration():
    return 'Hello World!'


@app.route('/client/login')
def client_login():
    return 'Hello World!'


@app.route('/client/edit_profile')
def client_profile():
    return 'Hello World!'


@app.route('/client/get_profile')
def client_profile():
    return 'Hello World!'