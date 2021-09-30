from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import platform
import os


class Test:
    url = 'https://accounts.google.com/signin/v2/identifier?hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        if platform.system() == 'Linux':
            self.user_data = os.path.expanduser("~") + '/.config/google-chrome/default'
            chrome_options.add_argument('--headless')
        else:
            self.user_data = os.path.expanduser("~").replace('\\', '/') + '/AppData/Local/Google/Chrome/User Data'

        chrome_options.add_argument(f"--user-data-dir={self.user_data}")
        chrome_options.add_argument('--no-sandbox')  # Solve the error that the DevToolsActivePort file does not exist
        chrome_options.add_argument('--disable-gpu')  # Google documentation mentions that this attribute needs to be added to avoid bugs
        # Add User-Agent
        chrome_options.add_argument(
          "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        # chrome_options.add_argument('--proxy-server=http://')  # Use the proxy IP to log in to the browser
        # remove title of automation
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # Forbidden plugin
        chrome_options.add_argument('--disable-plugins')
        # Disable popup blocking
        chrome_options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def login(self):
        self.driver.get(self.url)
        sleep(2)
        try:
            if 'myaccount.google.com' not in self.driver.current_url:
                self.driver.find_element_by_id('identifierId').send_keys(email)
                sleep(2)
                self.driver.find_element_by_id('identifierNext').click()
                sleep(3)
                self.driver.find_element_by_name('password').send_keys(password)
                sleep(3)
                self.driver.find_element_by_id('passwordNext').click()
                sleep(2)
        except:
            pass

    def start(self):
        self.driver.get('https://www.youtube.com/')
        sleep(2)
        self.driver.find_element_by_css_selector('#search').click()
        self.driver.find_element_by_css_selector('#search').send_keys('google', Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_css_selector('#contents ytd-video-renderer').click()


if __name__ == '__main__':
    email = input('- Enter email: ')
    password = input('- Enter pass: ')
    self = Test()
    self.login()
    self.start()
