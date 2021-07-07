"""from datetime import datetime
from time import sleep
import urllib3

urllib3.disable_warnings()
import urllib, os, requests, json, re

API_URL = 'https://www.instagram.com/query/'
GRAPHQL_API_URL = 'https://www.instagram.com/graphql/query/'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'  # noqa
MOBILE_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'  # noqa


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


session1 = login(username='201028946519', password='ammar2020')
csrf_token = session1.cookies.get_dict()['csrftoken']

r = session1.get('https://www.instagram.com/chhc')
strHtml = r.text
strjson = strHtml[strHtml.index('window._sharedData =') + 20:]
strjson = strjson[0:strjson.index(';</script>')]
jObject = json.loads(strjson)
user_id = jObject['entry_data']['ProfilePage'][0]['graphql']['user']['id']
##########################################################################

headers = {
    'User-Agent': USER_AGENT, 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close', }
headers.update({'x-csrftoken': csrf_token, 'x-requested-with': 'XMLHttpRequest', 'x-instagram-ajax': 1,
                    'Referer': 'https://www.instagram.com', 'Authority': 'www.instagram.com',
                    'Origin': 'https://www.instagram.com', 'Content-Type': 'application/x-www-form-urlencoded'})"""

from instagram_private_api import Client
from PIL import Image
from time import sleep

user_name = '201028946519'
# user_name = 'ebrahemelmorsy22001@gmail.com'
password = 'ammar20 20'

api = Client(user_name, password)
# like/unlike
# api.post_like('2354731885442407625')
# api.delete_like('2354731885442407625')

# follow/unfollow
# api.friendships_create('5535981195')
# api.friendships_destroy('5535981195')

# comment/delete comment
# d=api.post_comment('2354731885442407625', 'i am bot')
# id_comment = d['comment']['pk']
# id_media = d['comment']['media_id']
# id_media, id_comment
# api.delete_comment('2354731885442407625','18069297061240986')


# import instabot
#
# bot = instabot.Bot()
# bot.login(username=user_name, password=password)
# send message
# bot.send_messages('36297698137', ['36493649526', '36297698137', '35452263343', '36098635831'])
# post photo
# bot.upload_photo('Screenshot_1.jpg')


# delete post
# api.delete_media('2406107358948600676')

# get followers
import instagram_private_api


# next_id = ''
# n = 1
# while True:
#     try:
#         break
#         api.user_detail_info()
#         r = api.user_followers('5535981195', api.generate_uuid(), max_id=next_id)
#         next_id = r['next_max_id']
#         for use in r['users']:
#             try:
#                 rr = api.user_info(use['pk'])
#                 print(rr.get('user').get('public_email', {}),
#                       rr.get('user').get('public_phone_number', {}),
#                       rr.get('user').get('contact_phone_number', {}),
#                       rr.get('user').get('business_contact_method', {}))
#                 print(rr['user']['whatsapp_number'])
#
#             except Exception as e:
#                 pass
#             print(n, ' - ', use['username'])
#             n += 1
#
#         if not r['big_list']:
#             break
#         sleep(10)
#     except instagram_private_api.errors.ClientThrottledError:
#         print('please wait')

import requests
import json


def Get_Id(url):
    url += '?__a=1'
    r = requests.get(url)
    try:
        data = json.loads(r.text)
        if '/p/' in url:
            return data['graphql']['shortcode_media']['id']
        else:
            return data['graphql']['user']['id']
    except (json.decoder.JSONDecodeError, KeyError):
        return None


# Id = Get_Id('https://www.instagram.com/p/CCtsCyFFJzJ/')
# Id = Get_Id('https://www.instagram.com/chhc/')
# print(Id)
# abdulaziz_tu20
'''
api_url = 'https://i.instagram.com/api/{version!s}/'
try:
    import urllib.request as compat_urllib_request
except ImportError:  # Python 2
    import urllib2 as compat_urllib_request

try:
    import urllib.error as compat_urllib_error
except ImportError:  # Python 2
    import urllib2 as compat_urllib_error

try:
    import urllib.parse as compat_urllib_parse
except ImportError:  # Python 2
    import urllib as compat_urllib_parse

try:
    import http.client as compat_http_client
except ImportError:  # Python 2
    import httplib as compat_http_client
import gzip
from io import BytesIO
handlers = []

# Allow user to override custom ssl context where possible
custom_ssl_context = None
try:
    https_handler = compat_urllib_request.HTTPSHandler(context=custom_ssl_context)
except TypeError:
    # py version < 2.7.9
    https_handler = compat_urllib_request.HTTPSHandler()
handlers.extend([
    compat_urllib_request.HTTPHandler(),
    https_handler])
opener = compat_urllib_request.build_opener(*handlers)


def _read_response(response):
    """
    Extract the response body from a http response.

    :param response:
    :return:
    """
    if response.info().get('Content-Encoding') == 'gzip':
        buf = BytesIO(response.read())
        res = gzip.GzipFile(fileobj=buf).read().decode('utf8')
    else:
        res = response.read().decode('utf8')
    return res


def _call_api(endpoint, params=None, query=None, return_response=False, unsigned=False, version='v1'):
    """
    Calls the private api.

    :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
    :param params: POST parameters
    :param query: GET url query parameters
    :param return_response: return the response instead of the parsed json object
    :param unsigned: use post params as-is without signing
    :param version: for the versioned api base url. Default 'v1'.
    :return:
    """
    url = '{0}{1}'.format(api_url.format(version=version), endpoint)

    if query:
        url += ('?' if '?' not in endpoint else '&') + compat_urllib_parse.urlencode(query)

    headers = {
        'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
        'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
        'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
        'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    data = None
    if params or params == '':
        headers['Content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        if params == '':  # force post if empty string
            data = ''.encode('ascii')
        else:
            if not unsigned:
                json_params = json.dumps(params, separators=(',', ':'))
                hash_sig = _generate_signature(json_params)
                post_params = {
                    'ig_sig_key_version': None,
                    'signed_body': hash_sig + '.' + json_params
                }

            else:
                # direct form post
                post_params = params
            data = compat_urllib_parse.urlencode(post_params).encode('ascii')

    # req = compat_urllib_request.Request(url, data, headers=headers)
    r = requests.post(url=url,data=data,headers=headers)
    print(r.text)
    try:
        response = opener.open(req, timeout=15)

    except compat_urllib_error.HTTPError as e:
        error_response = _read_response(e)
        print(e)

    except Exception as e:
        print(e)

    if return_response:
        return response

    response_content = _read_response(response)

    json_response = json.loads(response_content)

    if json_response.get('message', '') == 'login_required':
        print('login_required')

    # not from oembed or an ok response
    if not json_response.get('provider_url') and json_response.get('status', '') != 'ok':
        print('Unknown Error')

    return json_response


user_id = 2027050887
endpoint = 'users/{user_id!s}/full_detail_info/'.format(**{'user_id': user_id})
p = {'device_id': 'android-1913bf2f00e711eb', 'guid': '1913bf2e-00e7-11eb-a422-5820b17116d5', 'adid': '5b846e3a-0121-26c8-dbe4-6e71a2983aab', 'phone_id': 'ed0b70f4-ef73-c3fa-aabd-5e08ed81df75', '_csrftoken': 'gYbJlifKLoM1DLvzq15pvU7Uh8ImKaCr', 'username': '201028946519', 'password': 'ammar2020', 'login_attempt_count': '0'}
_call_api('accounts/login/', params=p, return_response=True)
# {
#     'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
#     'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
#     'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
#     'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
#     'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger',
#     'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
#
'''

import requests,json
from datetime import datetime


def login(username, password):
    session = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
               'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    header = {
    'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
    'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
    'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
    'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

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
def new_login(username, password):
    header = {
    'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
    'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate',
    'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4932kbps',
    'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}