from datetime import datetime
from time import sleep
import requests
import json
import random


class Insta:
    def __init__(self):
        print('''- please wait while starting........''')
        self.session = self.login(username='ebrahemelmorsy22001@gmail.com', password='ammar2020')

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
        try:
            resp_json = resp.json()
        except Exception as e:
            print("Login error: JSON decode fail, {} - {}.".format(resp.status_code, resp.reason))
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

    def get_likes(self):
        while True:
            dict_l = dict()
            url = input('- put url  ( example:-https://www.instagram.com/p/code/ ) : ')  # chhc
            if url != '':
                break
            else:
                pass
        if url.find('instagram.com/p/') > -1:
            code = url.split('/p/')[1].split('/')[0]
        else:
            print('- wrong url')
            return False

        u = True

        print('- getting Likes ')
        resp = self.get_like(code=code)
        num = resp['data']['shortcode_media']['edge_liked_by']['count']
        print('- Number of Likes {}'.format(num))
        p = 1
        end_cursor = ''
        while u:
            if resp != 'errors':
                u = resp['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
                end_cursor = resp['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
                for i in resp['data']['shortcode_media']['edge_liked_by']['edges']:
                    user = i['node']['username']
                    full_name = i['node']['full_name']
                    id = i['node']['id']
                    profile_pic_url = i['node']['profile_pic_url']
                    pr = f'ID: {id} ,username: {user} ,Full Name: {full_name}'
                    dict_l[id] = {'name': full_name, 'user': user, 'img': profile_pic_url}
                    p += 1
                    self.print_percent_done(p, num, data=pr)


                sleep(2)
                resp = self.get_like(code=code, end_cursor=end_cursor)
            else:
                print('- please wait...')
                sleep(15)
                resp = self.get_like(code=code, end_cursor=end_cursor)
            if p >= 700:
                break
        winner = dict_l[random.choice(list(dict_l.keys()))]
        print()
        print(f'- Winner Is (name: {winner["name"]}, username: {winner["user"]}, img: {winner["img"]} )')

    def get_like(self, code, end_cursor=None):
        if end_cursor is None:
            url = 'https://www.instagram.com/graphql/query/?query_id=17864450716183058&{}'.format(
                'variables={"shortcode":"%s","first":50}') % code
            str_html = self.session.get(url)
        else:
            url = 'https://www.instagram.com/graphql/query/?query_id=17864450716183058&{}'.format(
                'variables={"shortcode":"%s","first":50,"after":"%s"}') % (code, end_cursor)
            str_html = self.session.get(url)

        if str_html.ok:
            resp = json.loads(str_html.text)
            return resp
        else:
            print(str_html.status_code)
            return 'errors'

    @staticmethod
    def print_percent_done(index, total, data, bar_len=50):
        percent_done = (index - 1) / total * 100
        percent_done = round(percent_done, 1)

        done = round(percent_done / (100 / bar_len))
        togo = bar_len - done

        done_str = '█' * int(done)
        togo_str = '░' * int(togo)

        print(f'- ⏳ {total}\\{index - 1} - [{done_str}{togo_str}] {data} ({percent_done} %)', end='\r')


if __name__ == '__main__':
    inst = Insta()
    inst.get_likes()
