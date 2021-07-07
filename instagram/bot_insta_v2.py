from datetime import datetime
from time import sleep
from itertools import cycle
import requests, json, re

# important headers to extract phone number and email
headers_and = {
    'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
    'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
    'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
    'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger'}

# extract id user or media
def Get_Id(user):
    url = f'https://www.instagram.com/{user}/?__a=1'
    r = requests.get(url)
    try:
        data = json.loads(r.text)
        return data['graphql']['user']['id']

    except (json.decoder.JSONDecodeError, KeyError):
        return None


class Insta:
    def __init__(self):
        self.number = []
        self.mail = []
    # Not main
    # def Login(self):
    #     session_list = set()
    #     accounts = [('201028946519', 'ammar2020'),
    #                 ('ebrahemelmorsy22001@gmail.com', 'ammar2020'),
    #                 ('ebrahemelmorsy22002@gmail.com', 'ammar2020'),
    #                 ('moduhondu@gmail.com', 'ammar2020'),
    #                 ('uhiotyui6@gmail.com', 'ammar2020'),
    #                 ('uiuyhjyy@gmail.com', 'ammar2020'),
    #                 ('jvbjyhg@gmail.com', 'ammar2020'),
    #                 ('shakermouty@gmail.com', 'ammar2020')]
    #     for username, password in accounts:
    #         res = self.login(username=username, password=password)
    #         if res:
    #             session_list.add(res)
    #     print(len(session_list))
    #     self.session = cycle(session_list)

    # login def
    def login(self, username, password):
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
        if resp.status_code == 200:
            return session
        else:
            try:
                resp_json = resp.json()

                if resp_json.get('checkpoint_url'):
                    print("Login: Checkpoint required. Point your browser to "
                          "https://www.instagram.com{} - "
                          "follow the instructions, then retry.".format(resp_json.get('checkpoint_url')))
                elif resp_json['status'] != 'ok':
                    if 'message' in resp_json:
                        print("Login error: \"{}\" status, message \"{}\".".format(resp_json['status'],
                                                                                   resp_json['message']))
                    else:
                        print("Login error: \"{}\" status.".format(resp_json['status']))
                elif 'authenticated' not in resp_json:
                    if 'message' in resp_json:
                        print("Login error: Unexpected response, \"{}\".".format(resp_json['message']))
                    else:
                        print("Login error: Unexpected response, this might indicate a blocked IP.")
                elif not resp_json['authenticated']:
                    if resp_json['user']:
                        print('Login error: Wrong password.')
                    else:
                        print('Login error: User {} does not exist.'.format(username))
                else:
                    return session
            except Exception as e:
                print("Login error: JSON decode fail, {} - {}.".format(resp.status_code, resp.reason))

    # not main
    def get_followers(self):
        while True:
            url = input(' put username  ( example:- chhc  ) : ')  # chhc
            if url != '':
                break
            else:
                pass
        if url.find('instagram.com/') > -1:
            username = url.split('com/')[1].split('/')[0]
        else:
            username = url

        now1 = datetime.now()
        try:
            print('getting followers')
            p = 1
            u = True
            end_cursor = None
            #####################################################################
            session = next(self.session)
            user_id = session.get(f"https://www.instagram.com/{username}/?__a=1").json()['graphql']['user']['id']
            resp = self.gf(user_id)
            while u:
                try:
                    if resp != 'error':
                        if len(resp['data']['user']['edge_followed_by']['edges']) != 0:
                            u = resp['data']['user']['edge_followed_by']['page_info']['has_next_page']
                            end_cursor = resp['data']['user']['edge_followed_by']['page_info']['end_cursor']
                            for i in resp['data']['user']['edge_followed_by']['edges']:
                                user = i['node']['username']
                                Id = i['node']['id']

                                self.user_info(Id)
                                print(f'{p} : {user}')
                                p += 1
                        else:
                            print('- Please Wait....')
                            sleep(5)

                        sleep(1.5)
                        resp = self.gf(user_id=user_id, end_cursor=end_cursor)
                    else:
                        print('- Error, Please Wait....')
                        sleep(40)
                        resp = self.gf(user_id=user_id, end_cursor=end_cursor)
                except Exception as e:
                    print(e)

                except:
                    pass

            print('Number of Followers {0}'.format(resp['data']['user']['edge_followed_by']['count']))
        except Exception as e:
            print(e)
        end_time = datetime.now() - now1
        print(end_time)
        print('--Done--')

    def gf(self, user_id, end_cursor=None):
        session = next(self.session)
        if end_cursor is None:
            strHtml = session.get(
                f"https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={user_id}&first=100")
        else:
            strHtml = session.get(
                f"https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={user_id}&first=100&after={end_cursor}")
        if strHtml.ok:
            resp = json.loads(strHtml.text)
            return resp
        else:
            print(strHtml.status_code)
            return 'error'

    # not main
    def get_following(self):
        while True:
            url = input('put username  ( example:- chhc  ) : ')
            if url != '':
                break
            else:
                pass
        if url.find('instagram.com/') > -1:
            username = url.split('com/')[1].split('/')[0]
        else:
            username = url
        now1 = datetime.now()
        print(' getting following ')
        p = 1
        u = True
        end_cursor = None
        #####################################################################
        session = next(self.session)
        user_id = session.get(f"https://www.instagram.com/{username}/?__a=1").json()['graphql']['user']['id']
        resp = self.gfing(user_id)
        print('Number of Following {}'.format(resp['data']['user']['edge_follow']['count']))
        #####################################################################

        while u:
            try:
                if resp != 'error':
                    if len(resp['data']['user']['edge_follow']['edges']) != 0:
                        u = resp['data']['user']['edge_follow']['page_info']['has_next_page']
                        end_cursor = resp['data']['user']['edge_follow']['page_info']['end_cursor']
                        for i in resp['data']['user']['edge_follow']['edges']:
                            user = i['node']['username']
                            Id = i['node']['id']
                            self.user_info(Id)
                            print(f'{p} : {user}')
                            p += 1
                    else:
                        print('- Please Wait....')
                        sleep(5)

                    sleep(1.5)
                    resp = self.gfing(user_id=user_id, end_cursor=end_cursor)
                else:
                    print('- Error, Please Wait....')
                    sleep(40)
                    resp = self.gfing(user_id=user_id, end_cursor=end_cursor)
            except Exception as e:
                print(e)

            except:
                pass
        print('--Done--')
        end_time = datetime.now()-now1
        print(end_time)
        print('Number of Following {}'.format(resp['data']['user']['edge_follow']['count']))

    def gfing(self, user_id, end_cursor=None):
        session = next(self.session)
        if end_cursor is None:
            strHtml = session.get(
                f'https://www.instagram.com/graphql/query/?query_id=17874545323001329&id={user_id}&first=100')
        else:
            strHtml = session.get(
                f'https://www.instagram.com/graphql/query/?query_id=17874545323001329&id={user_id}&first=100&after={end_cursor}')
        #########################
        if strHtml.ok:
            resp = json.loads(strHtml.text)
            return resp
        else:
            print(strHtml.status_code)
            return 'erorr'

    def user_info(self, user_id):
        session = next(self.session)
        r = session.get(f'https://i.instagram.com/api/v1/users/{user_id}/info/', headers=headers_and).json()
        if r.get('status') == 'ok':
            public_email = r.get('user').get('public_email')
            public_phone_number = r.get('user').get('public_phone_number')
            contact_phone_number = r.get('user').get('contact_phone_number')
            bio = r.get('user').get('biography')
            full_name = r.get('user').get('full_name')
            username = r.get('user').get('username')
            userid = r.get('user').get('pk')
            is_business = r.get('user').get('is_business')
            if not public_email or public_email == '':
                if re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', bio):
                    self.mail += re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', bio)
                elif re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', full_name):
                    self.mail += re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', full_name)
            else:
                if public_email != '':
                    self.mail.append(public_email)

            if not public_phone_number and not contact_phone_number or contact_phone_number == '':
                if re.findall(r'\d{8,15}', bio):
                    self.number += re.findall(r'\d{8,15}', bio)
                elif re.findall(r'\d{8,15}', full_name):
                    self.number += re.findall(r'\d{8,15}', full_name)
            else:
                if public_phone_number != '':
                    self.number.append(public_phone_number)
                if contact_phone_number != '':
                    self.number.append(contact_phone_number)

            print(
                f'username:{username} is_business_account:{is_business} email:{public_email}  number : {public_phone_number}, {contact_phone_number}')
            print(len(self.number))
            print(self.number)
            print(len(self.mail))
            print(self.mail)
            sleep(1)


if __name__ == '__main__':  # 10:48-->
    inst = Insta()
    inst.Login()
    inst.get_followers()
    # inst.get_following()
