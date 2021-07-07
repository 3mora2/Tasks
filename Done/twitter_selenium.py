from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


################################################
class Twitter_extract:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(4)
        sleep(2)
        #############

        self.login()

    def login(self):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        username_botton = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.NAME, "session[username_or_email]")))
        for usern in self.username:
            username_botton.send_keys(usern)
            sleep(random.randint(2, 8) / 10)
        sleep(1)
        password_botton = self.driver.find_element_by_name('session[password]')
        for passw in self.password:
            password_botton.send_keys(passw)
            sleep(random.randint(2, 8) / 10)
        sleep(2)
        password_botton.send_keys(Keys.ENTER)
        sleep(7)

    def Extract_followers(self, username):
        followers_list = []
        usern_info=[]
        n=1
        self.driver.get(f"https://twitter.com/{username}/followers")
        sleep(random.randint(5, 10))
        for l in range(0,1000):
            followers=self.driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div/div')
            '''url_img=[follower.find_element_by_xpath('div/div/div/div[1]/div/a/div[1]/div[2]/div/img').get_attribute('src') for follower in followers ]
            user_name=[follower.find_element_by_xpath('div/div/div/div[2]/div[1]/div[1]/a').text.split('\n')[0] for follower in followers ]
            user_tag=[follower.find_element_by_xpath('div/div/div/div[2]/div[1]/div[1]/a').text.split('\n')[1] for follower in followers ]'''
            for follower in followers:
                if follower not in followers_list:
                    try:

                        followers_list.append(follower)
                        try:
                            url_img=follower.find_element_by_xpath('div/div/div/div[1]/div/a/div[1]/div[2]/div/img').get_attribute('src')
                        except:
                            url_img=None
                        user_data=follower.find_element_by_xpath('div/div/div/div[2]/div[1]/div[1]/a').text.split()
                        user_name=user_data[0]
                        user_tag=user_data[1]
                        usern_info.append((user_name,user_tag,url_img))
                        print(n,user_name,user_tag,url_img)
                        n+=1
                    except Exception as e:
                        print(e)
                    #####################
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(random.randint(3,6))


        print(len(usern_info),len(followers_list))

if __name__ == "__main__":
    my_bot = Twitter_extract(username='ammaralkotb1@gmail.com', password='ammar2016')
    my_bot.Extract_followers('SINDOnews')
