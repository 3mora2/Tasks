import json
import requests,time
from datetime import datetime
now1 = datetime.now()
start_time = now1.strftime("%H:%M:%S")
#########################################################
#https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={acountId}&first=1000&after={cursor}
def gf(user_id,end_cursor=None,b=None):
    if b==1:
        session=session1
    elif b==2:
        session=session2
    else:
        session=session3
    if end_cursor ==None:
        strHtml = session.get("https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={}&first=100".format(user_id))
    else:
        strHtml = session.get("https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={}&first=100&after={}".format(user_id,end_cursor))
    if strHtml.ok:
        resp=json.loads(strHtml.text)
        print(b)
        return resp
    else:
        print(strHtml.status_code)
        return 'erorr'

#########################################################
def login(username,password):
    session = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
               'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    session.headers.update(headers)
    session.get('https://www.instagram.com/web/__mid/')
    csrf_token = session.cookies.get_dict()['csrftoken']
    session.headers.update({'X-CSRFToken': csrf_token})
    from datetime import datetime, timedelta
    enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), password)
    print('logining')
    resp = session.post('https://www.instagram.com/accounts/login/ajax/',data={'enc_password': enc_password, 'username': username}, allow_redirects=True)#,proxies=proxyDict)
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
        print('')
    return session
###################################################################################################
#####################################################################
'''us1=input('1-username')
pa1=input('pass')
us2=input('2-username')
pa2=input('paass')
us3=input('3-username')
pa3=input('pass')'''

session1=login(username='201028946519',password='ammar2020')
print('1')
#session2=login(username='ebrahemelmorsy22001@gmail.com',password='ammar2020')
print('2')
#session3=login(username='ebrahemelmorsy22002@gmail.com',password='ammar2020')
print('3')


#####################################################################
strHtml = session1.get("https://www.instagram.com/%s" % "ammar").text
strjson = strHtml[strHtml.index('window._sharedData =') + 20:]
strjson = strjson[0:strjson.index(';</script>')]
jObject = json.loads(strjson)
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['biography'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['country_block'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['external_url'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['id'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['is_business_account'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['business_category_name'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['category_id'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['username'])
print(jObject['entry_data']['ProfilePage'][0]['graphql']['user']['connected_fb_page'])
exit()
user_id=jObject['entry_data']['ProfilePage'][0]['graphql']['user']['id']

#resp = self.query_followed_by(username, user_id)
resp=gf(user_id)
#####################################################################
lists=[]
#followers = resp['followed_by']['nodes']
#save_followed_by(followers)
p=1
b=None
u=True
end_cursor=None
err=0
while u:
    if resp != 'erorr':
        u=resp['data']['user']['edge_followed_by']['page_info']['has_next_page']
        end_cursor = resp['data']['user']['edge_followed_by']['page_info']['end_cursor']
        for i in resp['data']['user']['edge_followed_by']['edges']:
            user=i['node']['username']
            id=i['node']['id']
            full_name=i['node']['full_name']
            profile_pic_url=i['node']['profile_pic_url']
            if user in lists:
                print('*********************************in lists*******************************')
            else:
                lists.append(user)
                print(' {0}-:{1}'.format(p,user))
                p+=1
        #time.sleep(.1)
        if b== None:
            b=1
        elif b==1:
            b=2
        elif b==2:
            b=3
        elif b==3:
            b=1
        time.sleep(.4)
        resp = gf(user_id=user_id,end_cursor=end_cursor,b=b)
    else:
        err+=1
        print('phze wait')
        time.sleep(15)
        if b== None:
            b=1
        elif b==1:
            b=2
        elif b==2:
            b=3
        elif b==3:
            b=1
        resp = gf(user_id=user_id, end_cursor=end_cursor,b=b)

now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(start_time,end_time)
print(err)


##################
