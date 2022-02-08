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

class Owner(db.Model):
    pass



class Realtor(db.Model):
    id = db.Column(db.Integer, primary_key=True)                        #– название организации;
    inn = db.Column(db.String(120), index = True, unique = True)        #– ИНН (проверка в налоговой);
    address = db.Column(db.String(120), index = True, unique = False)   #– юр. адрес;                                                              
    contact = db.Column(db.String(120), index = True, unique = False)   #– контактное лицо;
    manager = b.Column(db.String(120), index = True, unique = False)    #-
    name = db.Column(db.String(120), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = False)     #– адрес эл. почты (проверка путем отправки ссылки);
    phone = db.Column(db.String(120), index = True, unique = False)     #– сотовый телефон (проверка путем отправки кода в смс);
    password_hash = db.Column(db.String(120), index = True, unique = False)    #– пароль (подтверждение пароля);
    date_of_registration = db.Column(db.DateTime(120), index = True, unique = True)
    qr = db.Column(db.String(120), index = True, unique = True)
    token = db.Column(db.String(120), index = True, unique = True)
    
    pass





– регистрационные данные (название организации, ф.и.о. директора, ИНН, адрес юр. лица, сколько лет зарегистрирована в системе);
– количество сдаваемого жилья (кол-во квартир, сдаваемых за год);
– срок нахождения в системе;
– рейтинг риелтора, составленный в стороннем сервисе;
– рейтинг риелтора, составленный на основе оценок арендаторов (8-10 – зеленый, 5-7 – желтый, 0-4 – красный);
– история сдачи жилого помещения (одного или нескольких) – заполняется автоматически при сдаче жилых помещений и регистрации договора;
– срок нахождения в системе;
– рейтинг (по 10 бальной шкале);
– отзывы о риелторе;
– возможность редактирования всех регистрационных данных (добавление фото) с их повторной проверкой;


   
    
    
