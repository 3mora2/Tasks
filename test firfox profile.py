from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import os

user_data = os.path.expanduser("~") + r'\Selenium'
if not os.path.exists(user_data):
    os.mkdir(user_data)

options = Options()
options.add_argument('-no-sandbox')
options.add_argument('-disable-setuid-sandbox')
options.add_argument('-disable-dev-shm-usage')
options.add_argument('-disable-gpu')

options.add_argument("-profile")
options.add_argument(user_data)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),  options=options)
driver.get('about:support')
print(driver.find_element_by_css_selector('#profile-dir-box').text)



