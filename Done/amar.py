from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
###################################
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://egshoping.com/ar/login/')
name = driver.find_element_by_xpath('//*[@id="login"]/div/p[1]/input')
name.send_keys('ahmedali@gmail.com')
password = driver.find_element_by_xpath('//*[@id="login"]/div/p[2]/input')
password.send_keys('Password12')
password.submit()
driver.get('https://egshoping.com/index.php?route=seller/account-product/create')
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="cke_1_contents"]/iframe')))
text = driver.find_element_by_tag_name('body')
text.send_keys('fbbfgbfgbfgbg')
driver.switch_to.default_content()
