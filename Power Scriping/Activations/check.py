from datetime import datetime

import requests

from .constant import PATH_FILE, INTERNAL_KEY, ALGORITHM, KEY, mac
import base64
import json
import jwt


class Check:
    old = dict()
    key = None
    host = None
    is_app = False

    def __init__(self, app):
        self.app = app

    def start(self):
        text = self.open_file()
        if text:
            self.load_old(text)
            key = self.get_key_file()
            if key:
                self.Is_App(key)
                if self.is_app and self.key:
                    self.decode()
                    if self.host and self.key:
                        return self.check_api()
        return None, None

    @staticmethod
    def open_file():
        try:
            with open(PATH_FILE, 'r') as f:
                return f.read()
        except:
            pass
        return None

    def load_old(self, text):
        try:
            self.old = json.loads(text)
        except:
            pass

    def get_key_file(self):
        return self.old.get(base64.b64encode(self.app.encode()).decode('ascii'), None)

    def Is_App(self, serial):
        try:
            serial = '.'.join(serial.split('.')[::-1])
            data = jwt.decode(serial, key=INTERNAL_KEY, algorithms=[ALGORITHM])
            self.key = data.get('serial')
            self.is_app = data.get('app') == self.app
        except Exception as e:
            print(e)

    def decode(self):
        try:
            key = '.'.join(self.key.split('.')[::-1])
            key = jwt.decode(key, key=KEY, algorithms=[ALGORITHM])
            self.host = base64.b64decode(key['host']).decode('UTF-8')
        except:
            pass

    def check_api(self):
        try:
            r = requests.post(f'{self.host}api/check-key?key={self.key}&mac={mac}')
            if r.ok and not r.json()['error']:
                date = datetime.strptime(r.json()['time'], '%a, %d %b %Y %H:%M:%S GMT') - datetime.now()
                if date.days > 0:
                    time_end = datetime.strptime(r.json()['time'], '%a, %d %b %Y %H:%M:%S GMT')
                    return time_end, True
                else:
                    return False, True
        except:
            pass

        return None, False
