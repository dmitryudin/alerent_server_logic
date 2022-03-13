
#   fieldsOfClass = list(filter(lambda x: x.find('_')==-1, dir(self)))

import io
import base64
import hashlib
import datetime
 
salt = b'\x1c\xc5\xc1\xee\t\r\'\xff\xf2\xf4\x12\x1c\xa2\xc9\x98\xa1\xb7\xff}\x05k"A]3\xe18\'\xd6\xb2[P' 



def generatePasswordHash(password):
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128) 
	return key


def checkPasswordHash(password, hash):
	current_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128) 
	if current_key==hash: return True
	else: return False
	
print(dir(datetime.datetime.strptime('2022-08-08', "%Y-%m-%d").date()))
print(dir(datetime.datetime.now().date()))
'''
import qrcode
# пример данных
data = 1
# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
buffer = io.BytesIO()
img.save(buffer, format="PNG")
qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")
imgdata = base64.b64decode(qr_code)
with open('myqr.png', 'wb') as f:
    f.write(imgdata)
'''