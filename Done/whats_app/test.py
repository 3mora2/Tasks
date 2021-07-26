from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-plugins')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument("--user-data-dir={}".format(r'C:\selenium\AutomationProfile'))
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get('https://web.whatsapp.com/')
# for numb in ['+201028946519', '+201000', '+201028946519']:
#     com = '''
#     if (!document.querySelector('header > a')){
#     header = document.querySelector('header');
#     newlink = document.createElement('a');
#     header.appendChild(newlink);
#     }
#     a = document.querySelector('header > a');'''+f'''
#     a.setAttribute('href', 'https://web.whatsapp.com/send?phone={numb}&text&app_absent=0');
#     '''+'''
#     document.querySelector('header > a').click()
#     '''
#     driver.execute_script(com)
#     sleep(2)
#     print(len(driver.find_elements_by_css_selector('div[data-animate-modal-body="true"]')))
driver.find_element_by_css_selector('div[role="button"][title="إرفاق"]').click()
driver.find_element_by_css_selector('[data-testid="attach-image"]+input').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")
driver.find_element_by_css_selector('[class="_13NKt copyable-text selectable-text"][data-tab="6"]').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")

driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()
driver.find_element_by_css_selector('[data-testid="attach-document"]+input[type="file"]').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")
driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()