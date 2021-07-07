import requests,random,time
from lxml import html
import requests.packages.urllib3.exceptions
import json
from urllib3.exceptions import InsecureRequestWarning


def get_followers(account_id, count=20, page_size=20, end_cursor='',
                  delayed=True):

    index = 0
    accounts = []

    next_page = end_cursor

    if count < page_size:
        raise InstagramException(
            'Count must be greater than or equal to page size.')

    while True:
        time.sleep(1)

        variables = {
            'id': str(account_id),
            'first': str(count),
            'after': next_page
        }


        response = self.__req.get(
            endpoints.get_followers_json_link(variables),
            headers=headers)

        if not response.status_code == Instagram.HTTP_OK:
            raise InstagramException.default(response.text,
                                             response.status_code)

        jsonResponse = response.json()

        if jsonResponse['data']['user']['edge_followed_by']['count'] == 0:
            return accounts

        edgesArray = jsonResponse['data']['user']['edge_followed_by']['edges']
        if len(edgesArray) == 0:
            InstagramException(
                f'Failed to get followers of account id {account_id}.'
                f' The account is private.',
                Instagram.HTTP_FORBIDDEN)

        pageInfo = jsonResponse['data']['user']['edge_followed_by']['page_info']
        if pageInfo['has_next_page']:
            next_page = pageInfo['end_cursor']

        for edge in edgesArray:

            accounts.append(Account(edge['node']))
            index += 1

            if index >= count:
                # since break 2 not in python, looking for better solution since duplicate code
                data = {}
                data['next_page'] = next_page
                data['accounts'] = accounts

                return data

        # must be below here
        if not pageInfo['has_next_page']:
            break

        if delayed != None:
            # Random wait between 1 and 3 sec to mimic browser
            microsec = random.uniform(1.0, 3.0)
            time.sleep(microsec)

    data = {}
    data['next_page'] = next_page
    data['accounts'] = accounts

    return data









def getRequest(url):
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
    response=requests.get(url,verify=False,headers=headers)
    return response.text

def parseData(strHtml):
    strjson=strHtml[strHtml.index('window._sharedData =')+20:]
    strjson=strjson[0:strjson.index(';</script>')]
    jObject=json.loads(strjson)

    url='https://www.instagram.com' + jObject['entry_data']['ProfilePage'][0]['graphql']['user']['username']
    name=jObject['entry_data']['ProfilePage'][0]['graphql']['user']['full_name']
    username=jObject['entry_data']['ProfilePage'][0]['graphql']['user']['username']
    profileid=jObject['entry_data']['ProfilePage'][0]['graphql']['user']['id']
    followers=jObject['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']
    print(profileid,username)
    get_followers(profileid)

if __name__=="__main__":
    user='201028946519'
    session = requests.Session()
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
    'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    session.headers.update(headers)
    session.get('https://www.instagram.com/web/__mid/')
    csrf_token = session.cookies.get_dict()['csrftoken']
    session.headers.update({'X-CSRFToken': csrf_token})
    from datetime import datetime, timedelta
    enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), 'ammar2016')
    print('logining')
    login = session.post('https://www.instagram.com/accounts/login/ajax/',
                         data={'enc_password': enc_password, 'username': user}, allow_redirects=True)
    try:
        resp_json = login.json()
        print(resp_json)
        print('don')
    except Exception as e:
        print(e)
    url='https://www.instagram.com/chhc'
    strHtml=session.get(url).text
    strResult=parseData(strHtml)


#######################

'''username = 'kevin'
followers = []
account = instagram.get_account(username)
sleep(1)
followers = instagram.get_followers(account.identifier, 150, 100, delayed=True) # Get 150 followers of 'kevin', 100 a time with random delay between requests

for follower in followers['accounts']:
    print(follower)
'''































'''
    '''
