from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--user-data-dir={}".format(
    r'C:\Users\3mora\AppData\Local\Google\Chrome\User Data'))
# chrome_options.add_argument('--profile-directory=Profile 3')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# data = driver.execute_script("return document.querySelector('#root + script').text")
# import json
# json_data = json.loads(data.replace('window.__PRELOADED_STATE__ = ', ''))
# for size in json_data['entities']['products']['16657571']['sizes']:
#     print(size, "\n")
# 'https://int.stadiumgoods.com/en-sa/shopping/forum-buckle-low-bad-bunny-the-first-cafe-16657571'
#
# img = '\n'.join(set(img['sources']['2048'] for img in json_data['entities']['products']['16657571']['images']))
# desk = json_data['entities']['products']['16657571']['description']
# sku = json_data['entities']['products']['16657571']['sku']