import os
import traceback
import uuid
from datetime import datetime
import getpass
import requests
import jwt
import base64
import json


class Active:
    def __init__(self, app):
        self.app = app
        self.mac = str(uuid.getnode())
        self.user = getpass.getuser()

    def file_path(self):
        return os.path.isfile(self.path_file)

    def decode(self, serial):
        try:
            key_ = '.'.join(serial.split('.')[::-1])
            key_ = jwt.decode(key_, key=self.key, algorithms=[self.algorithm])
            host_ = base64.b64decode(key_['host']).decode('UTF-8')
            key_ = key_['serial']
            return host_, key_
        except:
            return None, None

    def encoding_(self, serial):
        data = {'serial': serial, 'app': self.app}
        encoding_data = jwt.encode(data, key=self.internal_key, algorithm=self.algorithm)
        return '.'.join(encoding_data.split('.')[::-1])

    def decode_(self, serial):
        try:
            serial = '.'.join(serial.split('.')[::-1])
            data = jwt.decode(serial, key=self.internal_key, algorithms=[self.algorithm])
            return data.get('serial'), data.get('app')
        except Exception as e:
            print(e)
            return None, None

    def open_file(self):
        try:
            with open(self.path_file, 'r') as f:
                text = f.read()
                text = json.loads(text)
                text = text.get(base64.b64encode(self.app.encode()).decode('ascii'))
                if text:
                    return self.check_key(text)

        except Exception as e:
            print(e)
        return None, None

    def check_key(self, key):
        try:
            key, app = self.decode_(key)
            if key and app == self.app:
                host, _ = self.decode(key)
                if host:
                    r = requests.post(f'{host}api/check-key?key={key}&mac={self.mac}')
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

    def to_file(self, data):
        with open(self.path_file, 'a+') as f:
            try:
                old = json.loads(f.read())
            except Exception as e:
                old = dict()
            old[base64.b64encode(self.app.encode()).decode('ascii')] = self.encoding_(data)
            f.write(json.dumps(old))

    def hidden_file(self):
        try:
            os.popen('attrib +h ' + self.path_file)
        except Exception as e:
            with open('log.log', 'a+', encoding="utf-8") as f:
                f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')

    def add_new(self, key):
        try:
            host, _ = self.decode(key)
            if host:
                r = requests.put(f'{host}api/update-key?key={key}&mac={self.mac}&user={self.user}')
                if r.ok and not r.json()['error']:
                    self.to_file(key)
                    self.hidden_file()
                    return True
        except Exception as e:
            with open('log.log', 'a+', encoding="utf-8") as f:
                f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')
        return None
