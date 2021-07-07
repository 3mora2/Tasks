from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import choice
from time import sleep
import subprocess
from pafy import new #pip install youtube-dl & pip install pafy
import warnings
warnings.filterwarnings("ignore")


def DataBase():
    import sqlite3
    url1='https://www.youtube.com/watch?v=ihUI3AIv48k'
    url2='https://www.youtube.com/watch?v=6RK4gnVhgHQ'
    db = sqlite3.connect('database.db')
    db1=db.cursor()
    db1.execute('CREATE TABLE IF NOT EXISTS YOUTYBE(time TEXT,link TEXT,play ,like INT,dislike INT,comment TEXT,shara INT,subscribe INT,download INT)')
    db1.execute('CREATE TABLE IF NOT EXISTS YOUTYBEmail(mail TEXT,password TEXT)')
    db1.execute('INSERT INTO YOUTYBE(time,link,play,like,dislike,comment,shara,subscribe,download) VALUES(?,?,?,?,?,?,?,?,?)',('9:00',url1,0,1,1,'comment1,comment2,comment3,commment4',1,1,0))
    db1.execute('INSERT INTO YOUTYBE(time,link,play,like,dislike,comment,shara,subscribe,download) VALUES(?,?,?,?,?,?,?,?,?)',('8:08',url2,1,1,1,0,1,0,1))
    #db.commit()
    db.row_factory = sqlite3.Row
    db1.execute('select time,link,play,like,dislike,comment,shara,subscribe,download from YOUTYBE')
    p=db1.fetchall()
    db1.execute('select mail,password from YOUTYBEmail')
    m=db1.fetchall()
    if len(p)==0 or len(m)==0:
        db1.execute('INSERT INTO YOUTYBE(time,link,play,like,dislike,comment,shara,subscribe,download) VALUES(?,?,?,?,?,?,?,?,?)',('9:00',url1,0,1,1,'comment1,comment2,comment3,commment4',1,1,0))
        db1.execute('INSERT INTO YOUTYBEmail(mail,password) VALUES(?,?)',('your email','your pass'))
        db.commit()
        db1.execute('select time,link,play,like,dislike,comment,shara,subscribe,download from YOUTYBE')
        p = db1.fetchall()
        db1.execute('select mail,password from YOUTYBEmail')
        m = db1.fetchall()
    db1.close()
    db.close()
    return m, p
##########################################################################################################################################################
##########################################################################################################################################################
def youtube(mail,data):
    ##############################################################################################################
    url='https://accounts.google.com/signin/v2/identifier?hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    email = mail[0][0]
    password = mail[0][1]
    url1=data[1]
    plays=data[2]
    likes=data[3]
    dislikes=data[4]
    comments=data[5]
    shares=data[6]
    subscribes=data[7]
    download=data[8]
    ##############################################################################################################
    subprocess.Popen('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222')
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver =webdriver.Chrome('G:\\programing\\projects\\automation\\chromedriver.exe', chrome_options=chrome_options)
    ##############################################################################################################
    driver.maximize_window() 
    driver.get(url)
    sleep(2)
    try:
        if 'myaccount.google.com' not in  driver.current_url:
            driver.find_element_by_id('identifierId').send_keys(email)
            sleep(2)
            driver.find_element_by_id('identifierNext').click()
            sleep(3)
            driver.find_element_by_name('password').send_keys(password)
            sleep(3)
            driver.find_element_by_id('passwordNext').click()
            sleep(2)
    except:
        pass
    ####################################################################
    sleep(2)
    driver.get(url1)
    driver.execute_script('window.scrollTo(0,400)')
    sleep(5)
    #####################################################################
    #to sike ads
    try:
        WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "ytp-ad-skip-button")))
        sleep(8)
        WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "ytp-ad-skip-button"))).click()
        print('pass ads')
    except:
        pass
    #play video
    sleep(2)
    try:
        play=driver.find_element_by_class_name('ytp-play-button')
        if plays==1:
            if play.get_attribute('aria-label')=='Play (k)':
                play.click()
                print('play')
        else:
            if play.get_attribute('aria-label')!='Play (k)':
                play.click()
                print('display')
    except:
        pass
    sleep(3)
    ######################################################################
    if likes == 1:
        try:
            like=driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button')
            if like.get_attribute('aria-pressed')=='false':
                like.click() #Like
                print('like')
            sleep(3)
        except:
            pass
    ######################################################################
    if dislikes ==1:
        try:
            dislike=driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a/yt-icon-button/button')
            if dislike.get_attribute('aria-pressed')=='false':
                dislike.click() #Like
                print('dislike')
            sleep(3)
        except:
            pass
    ######################################################################
    #to subscrbe
    if subscribes==1:
        try:
            SUBSCRIBE=driver.find_element_by_class_name('ytd-subscribe-button-renderer')
            if SUBSCRIBE.text !='SUBSCRIBED':
                SUBSCRIBE.click()
                print('subscribe')
            try:
                sleep(1)
                driver.find_element_by_class_name('ytd-subscription-notification-toggle-button-renderer').click()
                #all
                driver.find_element_by_xpath('//*[@id="items"]/ytd-menu-service-item-renderer[1]').click()
                print('all')
            except:
                pass
        except:
            pass
    #######################################################################
    if shares==1:
        try:
            driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-button-renderer[1]/a').click() #Share-step 1
            sleep(3)
            #share facebook
            driver.find_elements_by_xpath('//*[@id="target"]/yt-icon')[1].click()
            sleep(2)
            driver.switch_to_window(driver.window_handles[1])
            sleep(2)
            driver.find_element_by_name('__CONFIRM__').submit()
            sleep(2)
            driver.switch_to_window(driver.window_handles[0])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="close-button"]').click()
            print('share in faceboce')
        except:
            pass
    #######################################################################
    if comments !='0':
        try:
            com=choice(comments.split(','))
            WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.ID, "simplebox-placeholder"))).click()
            sleep(2)
            WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.ID, "contenteditable-root"))).send_keys(com)
            sleep(2)
            WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.ID, "submit-button"))).click()
            print('comment')
        except:
            pass
    driver.execute_script('window.scrollTo(0,0)')
    ########################################################################
    if download ==1:
        try:
            v = new(url1)
            s = v.getbest()
            filename = s.download()
        except:
            pass
##################################################################################################################################################
##################################################################################################################################################
def Time(tim):
    import time
    tt=time.localtime()
    h1=int(time.strftime("%H"))
    m1=int(time.strftime("%M"))
    t=tim.split(':')
    h2=int(t[0])
    m2=int(t[1])
    h=h2-h1
    m=m2-m1
    if m<0:
        m=m*(-1)
    if h<0:
        h=h*(-1)
    s=h*60*60+m*69
    return s

database=DataBase()
for data in database[1]:
    #sleep(Time(data[0]))
    youtube(database[0],data)




