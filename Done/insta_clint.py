'''import requests
from bs4 import BeautifulSoup
session = requests.Session()
respons=session.get('https://www.mohmal.com/ar/inbox')
soup=BeautifulSoup(respons.text,'lxml')
mail=soup.find('div',class_='email').attrs['data-email']
'''
from selenium import webdriver
import time
driver=webdriver.Chrome('G:\\programing\\projects\\automation\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.fakenamegenerator.com/gen-male-ar-tn.php')
fn=driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3')
bdata=driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[5]/dd')
mouns = str(bdata.text).split(' ')[0]
year=str(bdata.text).split(' ')[2]
brday=str(bdata.text).split(' ')[1].split(',')[0]
frn=str(fn.text).split(' ')[0]
scn=str(fn.text).split(' ')[1]
if "-" in frn:
    frn=frn.replace('-','')
if "-" in scn:
    scn= scn.replace('-','')
if "'" in frn:
    frn=frn.replace("'",'')
if "'" in scn:
    scn= scn.replace("'",'')
print(frn,scn,year,mouns,brday)
input('')
##############################
driver.get('https://www.mohmal.com/ar/inbox')
time.sleep(2)
mail=driver.find_element_by_class_name('email').text
print(mail)
###################################
time.sleep(2)
driver.execute_script('window.open("");')
driver.switch_to_window(driver.window_handles[1])
driver.get('https://www.facebook.com/reg/')
time.sleep(2)
driver.find_element_by_name('firstname').send_keys(frn)
time.sleep(2)
driver.find_element_by_name('lastname').send_keys(scn)
time.sleep(2)
driver.find_element_by_name('reg_email__').send_keys(mail)
time.sleep(2)
driver.find_element_by_name('reg_email_confirmation__').send_keys(mail)
driver.find_element_by_name('reg_passwd__').send_keys('ammar2020')
#year
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[24]').click()
#day
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[19]').click()
#sex
time.sleep(2)
driver.find_element_by_id('u_0_7').click()
time.sleep(2)
driver.find_element_by_name('websubmit').click()
##################################
input('done')
driver.get('https://www.instagram.com/accounts/emailsignup/')
driver.find_element_by_name('emailOrPhone').send_keys(mail)
driver.find_element_by_name('fullName').send_keys(mail.split('@')[0])
driver.find_element_by_name('username').send_keys(mail.split('@')[0])
driver.find_element_by_name('password').send_keys('ammar2020')
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
print(mail,mail.split('@')[0])
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[22]').click()
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
#driver.close()
