'''import instaloader
print('***welcom***')
L = instaloader.Instaloader()
L.login('201028946519', 'ammar2016')
print('login done')
profile = instaloader.Profile.from_username(L.context, 'chhc')
main_followers = profile.followers
print('number of followers {}'.format(main_followers))
i=1
for person in profile.get_followers():
    #print('{0}-{1}   ,full name : {2}  ,number of followes : {3}    ,profile pic url : {4}'.format(i,person.username,person.full_name,person.followers,person.profile_pic_url))
    print('{0}-Username : {1}   ,Full name : {2}'.format(i, person.username,person.full_name))
    i+=1




from igramscraper.instagram import Instagram
#from context import Instagram
from time import sleep

instagram = Instagram()
instagram.with_credentials(username='201028946519', password='ammar2016')
instagram.login()

username = 'kevin'
followers = []
account = instagram.get_account(username)
sleep(1)
followers = instagram.get_followers(account.identifier, 150, 100, delayed=True) # Get 150 followers of 'kevin', 100 a time with random delay between requests

for follower in followers['accounts']:
    print(follower)
'''
import json
import requests,time

session = requests.Session()
headers = {'User-Agent': 'Instagram 27.0.0.7.97 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US)'}
session.headers.update(headers)
g=session.get('https://www.instagram.com/chhc/')

    
