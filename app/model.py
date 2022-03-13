from app import db
import enum
from app import security as scr
import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120))
    dadsName = db.Column(db.String(120))
    phone = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index = True, unique=True)
    dateOfBurn = db.Column(db.Date)
    sitizenshipOfRussia=db.Column(db.Boolean)
    animals = db.Column(db.Integer)
    photo = db.Column(db.String(120))
    qr = db.Column(db.String(120))
    dateOfRegistration = db.Column(db.Date)
    token = db.Column(db.String(120))
    checkCode = db.Column(db.String(120))
    isVerified = db.Column(db.Boolean)
    rating = db.Column(db.Float)
    child = db.Column(db.Float)
    passwordHash = db.Column(db.String(120))
    passportId = db.Column(db.Integer)
    

    def setData(self, json):
        '''
        Вручную вбивать нужно _passport, dateOfRegistration, token
        '''    
        for el in json:
            if el=='_passport': continue
            if el=='photo':
                if self.photo==None:
                    setattr(self, 'photo', scr.sendImageToMediaServer(json[el]))
                    continue
                else:
                    remImageFromMediaServer(json[el])
                    setattr(self, 'photo', scr.sendImageToMediaServer(json[el]))
                    continue
            if el == 'password': 
                setattr(self, 'passwordHash', scr.generatePasswordHash(json[el]))
                continue
            if el == 'dateOfBurn':
                self.dateOfBurn = datetime.datetime.strptime(json[el], "%Y-%m-%d").date()
                continue
            setattr(self, el, json[el])

    def getData(self):
        fieldsOfClass = list(filter(lambda x: x.find('_')==-1, dir(self)))
        myDict={}
        for el in fieldsOfClass:
            if el=='metadata' or el=='getData' or el=='setData' or el=='query' or el=='passwordHash' or el=='registry':
                continue
            if el=='dateOfBurn': 
                myDict[el]=getattr(self, el[0:16])
                continue
            myDict[el]=getattr(self, el)
        return myDict
    


class Owner(db.Model):
    '''
    – фамилия, имя отчество;
    – паспортные данные (серия, номер, место и дата выдачи, место регистрации) + сканы первой страницы и страницы с регистрацией (проверка в паспортном столе);
    – данные документов, подтверждающие право на квартиру + сканы документов (зеленка, выписка из ЕГРН, договор купли продажи, договор аренды) (проверка через МФЦ, БТИ…);
    – адрес эл. почты (проверка путем отправки ссылки);
    – сотовый телефон (проверка путем отправки кода в смс);
    – пароль (подтверждение пароля);
    – регистрационные данные (с отметкой подтверждено или нет);
    – история сдачи жилого помещения (одного или нескольких) – заполняется автоматически при сдаче жилых помещений и регистрации договора (риелторские компании (при сдаче через посредника)) или физически арендаторами по результатам аренды (при сдаче без посредника) при условии использования нашей системы;
    – срок нахождения в системе;
    – рейтинг (по 10 бальной шкале);
    – отзывы о собственнике;
    – возможность редактирования всех регистрационных данных (добавление фото) с их повторной проверкой;
    – возможность добавления нового жилого помещения;
    – поиск арендатора в системе «Safe rent»по ID-номеру или QR-коду.
    '''
    id = db.Column(db.Integer, primary_key=True) 
    firstName = db.Column(db.String(120), index = True, unique = False)
    lastname = db.Column(db.String(120), index = True, unique = False)
    dadName = db.Column(db.String(120), index = True, unique = False)
    phone = db.Column(db.String(120), index = True, unique=False)
    email = db.Column(db.String(120), index = True)
    dateOfBurn = db.Column(db.DateTime, index = True)
    qr = db.Column(db.String(120), index = True)
    token = db.Column(db.String(120), index = True)
    dateOfRegistration = db.Column(db.DateTime, index = True)
    isVerified = db.Column(db.Boolean, index = True)
    passport = db.relationship("Passport", backref="owner_id", lazy="dynamic")
    photo = db.relationship("Photos", backref="owner_id", lazy="dynamic")



class Realtor(db.Model):
    '''
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
    '''
    id = db.Column(db.Integer, primary_key=True)                        #– название организации;
    inn = db.Column(db.String(120), index = True, unique = True)        #– ИНН (проверка в налоговой);
    address = db.Column(db.String(120), index = True, unique = False)   #– юр. адрес;                                                              
    contact = db.Column(db.String(120), index = True, unique = False)   #– контактное лицо;
    manager = db.Column(db.String(120), index = True, unique = False)    #-
    name = db.Column(db.String(120), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = False)     #– адрес эл. почты (проверка путем отправки ссылки);
    phone = db.Column(db.String(120), index = True, unique = False)     #– сотовый телефон (проверка путем отправки кода в смс);
    ratingOut = db.Column(db.Float, index = True, unique = True)
    ratingReal = db.Column(db.Float, index = True, unique = True)
    passwordHash = db.Column(db.String(120), index = True, unique = False)    #– пароль (подтверждение пароля);
    dateOfRegistration = db.Column(db.DateTime, index = True, unique = True)
    qr = db.Column(db.String(120), index = True, unique = True)
    token = db.Column(db.String(120), index = True, unique = True)
    
    


class Passport(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    series = db.Column(db.String(120), index = True, unique = False)
    number = db.Column(db.String(120), index = True, unique = False)
    dateOfIssue = db.Column(db.Date, index = True, unique = False) 
    placeOfIssue = db.Column(db.String(120), index = True, unique = False)
    placeOfRegistration = db.Column(db.String(120), index = True, unique = False)
    photoOfMainPage = db.Column(db.String(120), index = True, unique = False)
    photoOfRegistrationPage = db.Column(db.String(120), index = True, unique = False)
    divisionCode = db.Column(db.String(120), index = True, unique = False)
    client = db.Column(db.Integer, db.ForeignKey('client.id'))
    owner = db.Column(db.Integer, db.ForeignKey('owner.id'))

    def setData(self, json):    
        for el in json:
            if el=='photoOfMainPage':
                if self.photoOfMainPage==None:
                    setattr(self, 'photoOfMainPage', scr.sendImageToMediaServer(json[el]))
                    continue
                else:
                    setattr(self, 'photoOfMainPage', scr.sendImageToMediaServer(json[el]))
                    continue
            if el=='photoOfRegistrationPage':
                if self.photoOfRegistrationPage==None:
                    setattr(self, 'photoOfRegistrationPage', scr.sendImageToMediaServer(json[el]))
                    continue
                else:
                    setattr(self, 'photoOfRegistrationPage', scr.sendImageToMediaServer(json[el]))
                    continue
            if el=='dateOfIssue': 
                self.dateOfIssue = datetime.datetime.strptime(json[el], "%Y-%m-%d").date()
                continue
            setattr(self, el, json[el])

'''

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    ###### этап заключения сделки
    userId = db.Column(db.Integer)
    ownerId = db.Column(db.Integer)
    realtorId = db.Column(db.Integer)
    dateOfDealRegistration = db.Column(db.DateTime)  # дата заключения
    plannedTerm = db.Column(db.Integer)  # планируемый срок, дней
    cost = db.Column(db.Float) # стоимость оплаты, руб  
    userСonfirmation = db.Column(db.Boolean)
    # Подтверждение начала сделки пользователем
    ######## Конец сделки
    #### оценка пользователя
    neatness = db.Column(db.Integer) # аккуратность
    regularityOfPayments = db.Column(db.Integer) # регулярность платежей
    relationsWithNeighbors = db.Column(db.Integer)# отношения с соседями
    markOfUser = db.Column(db.Integer)
    userFeedback = db.Column(db.String)
    # словесный отзыв, комплексная оценка
    #### оценка собственника
    qualityOfHousing = db.Column(db.Integer)
    markOfOwner = db.Column(db.Integer)
    ownerFeedback = db.Column(db.String)
    ### оценка риелтора
    markOfRealtor = db.Column(db.Integer)
    realtorFeedback = db.Column(db.String)
    # словесный отзыв
    ### блок логики
    
'''


class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    path = db.Column(db.String(120), index = True, unique = False)
    owner = db.Column(db.Integer, db.ForeignKey('owner.id'))

'''
class Apartment(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    type
    #кадастровый номер
    # фактический адрес объекта
   #ю egrn_photo = db.Column(db.Enum(Photos))
   
'''


    
