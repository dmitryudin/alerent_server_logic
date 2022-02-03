from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(120), index = True, unique = False)
    last_name = db.Column(db.String(120), index = True, unique = False)
    phone = db.Column(db.String(120), index = True, unique = True)
   	email = db.Column(db.String(120), index = True, unique = True)
   	dateOfBurn = db.Column(db.String(120), index = True, unique = False)
   	passport = db.Column(db.String(120), index = True, unique = True)
   	password_hash = db.Column(db.String(120), index = True, unique = True)
   	rating = db.Column(db.Float(120), index = True, unique = True)
   	photo = db.Column(db.String(120), index = True, unique = True)
   	qr = db.Column(db.String(120), index = True, unique = True)
   	token = db.Column(db.String(120), index = True, unique = True)
   	date_of_registration = db.Column(db.DateTime(120), index = True, unique = True)
   	is_verified = db.Column(db.String(120), index = True, unique = True)


   
    
    
