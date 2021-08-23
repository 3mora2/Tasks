import os
import traceback
import uuid
from datetime import datetime
import getpass
import requests
import jwt
import base64

mac = str(uuid.getnode())
url = 'https://ammar-alkotb.herokuapp.com'
path_file = r'accuss.pka'
user = getpass.getuser()


def decode(serial):
    try:
        key_ = '.'.join(serial.split('.')[::-1])
        key_ = jwt.decode(key_, key='9S6S7e#', algorithms=["HS256"])
        host_ = base64.b64decode(key_['host']).decode('UTF-8')
        key_ = key_['serial']
        return host_, key_
    except:
        return None, None


def open_file():
    try:
        with open(path_file, 'r') as f:
            text = f.read()
        return check_key(text)
    except:
        return None


def decoding_text(text):
    decode_text = text
    decode_hash = base64.b64decode(decode_text)
    return decode_hash.decode('UTF-8')


def check_text(text):
    try:
        token = jwt.decode(
            text,
            key=mac,
            algorithms=["HS256"])
        key = token.get('key')
        return check_key(key)
    except:
        return None


def check_key(key):
    try:
        host, _ = decode(key)
        if host:
            r = requests.post(f'{host}api/check-key?key={key}&mac={mac}')
            if r.ok and not r.json()['error']:
                date = datetime.strptime(r.json()['time'], '%a, %d %b %Y %H:%M:%S GMT') - datetime.now()
                if date.days > 0:
                    time_end = datetime.strptime(r.json()['time'], '%a, %d %b %Y %H:%M:%S GMT')
                    return time_end, True
                else:
                    return False, True

    except Exception as e:
        with open('log.log', 'a+', encoding="utf-8") as f:
            f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')

    return None, False


def add_new(key):
    try:
        host, _ = decode(key)
        if host:
            r = requests.put(f'{host}api/update-key?key={key}&mac={mac}&user={user}')
            if r.ok and not r.json()['error']:
                if os.path.isfile(path_file):
                    os.remove(path_file)

                with open(path_file, 'w') as f:
                    f.write(key)
                try:
                    os.popen('attrib +h ' + path_file)
                except Exception as e:
                    with open('log.log', 'a+', encoding="utf-8") as f:
                        f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')

                return True
    except Exception as e:
        with open('log.log', 'a+', encoding="utf-8") as f:
            f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')
    return None


# if os.path.isfile(path_file):
#     print(open_file())
# else:
#     print(add_new())







