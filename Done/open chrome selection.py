import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()

# Open Default Chrome
user_data = os.path.expanduser("~") + r'\AppData\Local\Google\Chrome\User Data'

# Open Profile Chrome and Save Profile
# user_data = os.path.expanduser("~") + r'\AppData\Local\Google\Chrome\User Data\Selenium'

chrome_options.add_argument("--user-data-dir={}".format(user_data))

# If You have multi Profile Enter Name (Profile 4)
# chrome_options.add_argument('--profile-directory=Profile 4')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get('https://www.google.com')
