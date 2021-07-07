from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
################################################
class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        #self.url = str(input("enter url : "))
        #options = webdriver.ChromeOptions()
        #options.add_argument("headless")
        #self.driver = webdriver.Chrome()#chrome_options=options)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        sleep(2)
        #############
        
        self.login()
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?")
        sleep(2)
        username_botton=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.NAME, "username")))
        for usern in self.username:
            username_botton.send_keys(usern)
            sleep(random.randint(2,8)/10)
        sleep(1)
        password_botton=self.driver.find_element_by_name('password')
        for passw in self.password:
            password_botton.send_keys(passw)
            sleep(random.randint(2,8)/10)
        sleep(2)
        password_botton.send_keys(Keys.ENTER)
        sleep(7)
    def Make_Comments(self,username,num_post):
        self.driver.get(f"https://www.instagram.com/{username}")
        sleep(5)
        posts_= lambda: self.driver.find_elements_by_class_name('v1Nh3')
        posts=posts_()
        if len(posts) < num_post:
            for i in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(random.randint(2,8)/10)
            posts=posts_()
        self.driver.execute_script("window.scrollTo(0,0);")
        sleep(random.randint(1,5))
        pic_href = [elem.find_element_by_tag_name("a").get_attribute('href') for elem in posts[0:num_post] ]
        
        comment = "Hi! I am a Bot."
        sleep(random.randint(1,3))
        for ele in pic_href:
            self.driver.get(ele)
            sleep(random.randint(5,9))
            entry = lambda: self.driver.find_element_by_class_name('Ypffh')
            #entry = self.driver.find_element_by_class_name('Ypffh')
            entry().click()
            entry().clear()

            for i in comment:
                entry().send_keys(i)
                sleep(random.randint(4,10)/10)

            entry().send_keys(Keys.ENTER)
            sleep(random.randint(5,10))

        sleep(random.randint(10,15))
            



users=['mosalah','tamerhosny','chhc']

if __name__ == "__main__":
    my_bot = InstaBot(username='shakermouty@gmail.com',password='ammar2020')
    for user in users:
        my_bot.Make_Comments(user,3)
        sleep(random.randint(5,10))
