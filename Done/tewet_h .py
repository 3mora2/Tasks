import warnings
warnings.filterwarnings("ignore")
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import random
from openpyxl import load_workbook
while True:
    path = input('Enter the name of your Excel file, for example( data.xlsx ) : ')
    if '.xlsx' in path:
        break
try:
    book = load_workbook(path)

except:
    exit()

sheet = book.active
#############################
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
# options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("--user-data-dir=Edge-data")
driver = Edge(options=options)
#############################
"""driver_n = 0
try:
    try:
        subprocess.Popen(
            '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
    except:
        subprocess.Popen(
            '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver_n = 1
except:
    exit()"""
########################################################

subject = sheet['D2'].value
description = sheet["E2"].value
name = sheet["A2"].value
user_name = sheet["B2"].value
email = sheet["C2"].value
n = 0
url = 'https://help.twitter.com/forms/restore'
while True:
    driver.get(url)
    sleep(1)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'reactivation'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'followers_zero'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'followers_waited_48'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'app'))).send_keys(driver.find_element_by_css_selector('#app > option:nth-child(4)').text)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'subject'))).send_keys(subject)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'description'))).send_keys(description)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'name'))).send_keys(name)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'user_name'))).send_keys(user_name)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email'))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit_button'))).click()
    n += 1
    print('Send :', n)
    """print("Deleting Cookies.........")
    driver.delete_all_cookies()"""
    sleep(6)
    if (n % 10) == 0:
        print('Close and Reopen')
        driver.close()
        driver.quit()
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        driver = Edge(options=options)
        """
        if driver_n == 1:
            driver = Edge(options=options)
            driver_n = 0
        else:
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver_n = 1
        sleep(2)"""