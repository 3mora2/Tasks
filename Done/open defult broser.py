from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--user-data-dir={}".format(
    r'C:\Users\3mora\AppData\Local\Google\Chrome\User Data'))
chrome_options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

