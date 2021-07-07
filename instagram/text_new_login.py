import requests,json
from datetime import datetime


def login(username, password):
    session = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
               'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    session.headers.update(headers)
    session.get('https://www.instagram.com/web/__mid/')
    csrf_token = session.cookies.get_dict()['csrftoken']
    session.headers.update({'X-CSRFToken': csrf_token})
    enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), password)
    resp = session.post('https://www.instagram.com/accounts/login/ajax/',
                        data={'enc_password': enc_password, 'username': username},
                        allow_redirects=True)  # ,proxies=proxyDict)
    print(resp.status_code)
    ###################################################################################################
    try:
        resp_json = resp.json()
        try:
            if resp_json.get('checkpoint_url'):
                print("Login: Checkpoint required. Point your browser to "
                      "https://www.instagram.com{} - "
                      "follow the instructions, then retry.".format(resp_json.get('checkpoint_url')))
            if resp_json['status'] != 'ok':
                if 'message' in resp_json:
                    print("Login error: \"{}\" status, message \"{}\".".format(resp_json['status'],
                                                                               resp_json['message']))
                else:
                    print("Login error: \"{}\" status.".format(resp_json['status']))
            if 'authenticated' not in resp_json:
                if 'message' in resp_json:
                    print("Login error: Unexpected response, \"{}\".".format(resp_json['message']))
                else:
                    print("Login error: Unexpected response, this might indicate a blocked IP.")
            if not resp_json['authenticated']:
                if resp_json['user']:
                    print('Login error: Wrong password.')
                else:
                    print('Login error: User {} does not exist.'.format(username))
        except:
            pass
        return session

    except Exception as e:
        print("Login error: JSON decode fail, {} - {}.".format(resp.status_code, resp.reason))


session = login(username='201028946519', password='ammar2020')
input('asdfghjk')
print(session.get('https://i.instagram.com/api/v1/users/2027050887/info/').json())
headers = {
    'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
    'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
    'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
    'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger'}

print(session.get('https://i.instagram.com/api/v1/users/2027050887/info/', headers=headers).json())