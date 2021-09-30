import base64
import json
import os
import traceback
import jwt
import requests
from datetime import datetime
from Activations.constant import KEY, ALGORITHM, mac, user,PATH_FILE, INTERNAL_KEY


class Add:
    host = None
    old = dict()

    def __init__(self, app):
        self.app = app

    def start(self, key):
        self.decode(key)
        if self.host:
            r = requests.put(f'{self.host}api/update-key?key={key}&mac={mac}&user={user}')
            if r.ok and not r.json()['error']:
                self.to_file(key)
                self.hidden_file()
                return True

    def decode(self, serial):
        try:
            key_ = jwt.decode('.'.join(serial.split('.')[::-1]), key=KEY, algorithms=[ALGORITHM])
            self.host = base64.b64decode(key_['host']).decode('UTF-8')
        except:
            pass

    def to_file(self, data):
        try:
            with open(PATH_FILE, 'r') as f:
                try:
                    self.old = json.loads(f.read())
                except:
                    pass
            os.remove(PATH_FILE)
        except:
            pass

        with open(PATH_FILE, 'w') as f:
            self.old[base64.b64encode(self.app.encode()).decode('ascii')] = self.encode_data(data)
            f.write(json.dumps(self.old))

    def encode_data(self, data):
        data = {'serial': data, 'app': self.app}
        encoding_data = jwt.encode(data, key=INTERNAL_KEY, algorithm=ALGORITHM)
        return '.'.join(encoding_data.split('.')[::-1])

    @staticmethod
    def hidden_file():
        try:
            os.popen('attrib +h ' + PATH_FILE)
        except Exception as e:
            with open('log.log', 'a+', encoding="utf-8") as f:
                f.write(f'{datetime.now()}: {str(traceback.format_exc())} \n')