import json, sys, hashlib, os, time, marshal
import requests

'''
print(a['access_token'])
with open('token.log','r') as f:
 token=f.read()
print(token)

#r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
#a = json.loads(r.text)
#print(a)
i = '100008922404114'
x = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
y = json.loads(x.text)
print(y)'''


def login(id):
    pwd = 'ammar2020'
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'

    data = {"api_key": "882a8490361da98702bf97a021ddc14d", "credentials_type": "password", "email": id,
            "format": "JSON", "generate_machine_id": "1", "generate_session_cookies": "1", "locale": "en_US",
            "method": "auth.login", "password": pwd, "return_ssl_resources": "0", "v": "1.0"}

    sig = f'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={id}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={pwd}return_ssl_resources=0v=1.0{API_SECRET}'

    x = hashlib.new('md5')
    x.update(sig.encode())
    data.update({'sig': x.hexdigest()})

    session = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
               'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    session.headers.update(headers)
    session.get('https://www.instagram.com/web/__mid/')
    csrf_token = session.cookies.get_dict()['csrftoken']
    session.headers.update({'X-CSRFToken': csrf_token})

    r = session.get('https://api.facebook.com/restserver.php', params=data)
    a = json.loads(r.text)
    print(a)
    with open('token.log', 'w') as f:
        f.write(a['access_token'])

    return a['access_token']


# token = login('100051826987427')
# print(token)

with open('token.log', 'r') as f:
    token = f.read()
print(token)

id = '100009676429300'
# x = requests.get("https://graph.facebook.com/" + i + "?access_token=" + token)
# y = json.loads(x.text)
# print(y)

# Get user photo
# user_id = 100051826987427
# x = requests.get(f"https://graph.facebook.com/{user_id}/photos?access_token={token}")

# Get birthday, email, hometown
# user_id = 100051826987427
# x = requests.get(f"https://graph.facebook.com/{user_id}?fields=birthday,email,hometown&access_token={token}")


# Post in user page
# post_id = 100051826987427
# message = 'Awesome!'
# x = requests.post(f"https://graph.facebook.com/{post_id}/feed?message={message}&access_token={token}")

# Edit post in user page
# your_page_post_id = str(100051826987427_177746200629612)
# message = 'HappyHolidays!'
# x = requests.post(f"https://graph.facebook.com/{your_page_post_id}?message={message}&access_token={token}")

# Delete post in user page
# your_page_post_id = '100051826987427_177746200629612'
# x = requests.delete(f"https://graph.facebook.com/{your_page_post_id}?access_token={token}")


# Post Comment
# your_page_post_id = '100051826987427_177755993961966'
# message = 'this comment'
# parameters = {'access_token': token, 'message': message}
# url = f"https://graph.facebook.com/{your_page_post_id}/comments"
# x = requests.post(url, data=parameters)

# Edit Comment
# comment_id = '100051826987427_177755993961966_177761837294715'
# message = 'new comment'
# x = requests.post(f"https://graph.facebook.com/{comment_id}?message={message}&access_token={token}")

# Delete Comment
# comment_id = '100051826987427_177755993961966_177757677295131'
# x = requests.delete(f'https://graph.facebook.com/{comment_id}?access_token={token}')

# Like, Unlike
# your_page_post_id = '100051826987427_177755993961966'
# reactions = ['NONE', 'LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY', 'THANKFUL', 'PRIDE', 'CARE']
# reaction = reactions[0]
# parameters = {'access_token': token, 'type': reaction}
# x = requests.post(f"https://graph.facebook.com/{your_page_post_id}/reactions", data=parameters)
y = json.loads(x.text)
print(y)

# Friends request
# still text
# x = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token)


# replies still
# id_comment = '100051826987427_177755993961966_177768613960704'
# message = 'this r'
# parameters = {'access_token': token, 'message': message}
# # url = f"https://graph.facebook.com/177768613960704/replies"#?message={message}"#&access_token={token}"
# url = f"https://graph.facebook.com/v2.12/{id_comment}/comments?message=Hello&access_token={token}"
# x = requests.post(url)#, data=parameters)
