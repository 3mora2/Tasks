from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")
# remove title of automation
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument("--remote-debugging-port=9222")

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


def capt(self):
    self.driver.switch_to.frame(self.driver.find_element_by_css_selector('iframe'))
    self.driver.find_element_by_css_selector('.recaptcha-checkbox-border').click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(self.driver.find_element_by_css_selector('iframe[title="recaptcha challenge"]'))
    self.driver.find_element_by_css_selector('button.rc-button-audio').click()

#############################################3

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # Solve the error that the DevToolsActivePort file does not exist
chrome_options.add_argument(
    '--disable-gpu')  # Google documentation mentions that this attribute needs to be added to avoid bugs
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # Don't load pictures, speed up
chrome_options.add_argument(
    '--headless')  # The browser does not provide a visualization page. If the system does not support visualization under linux, this will fail to start
# Add User-Agent
chrome_options.add_argument(
    'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
chrome_options.add_argument('--proxy-server=http://')  # Use the proxy IP to log in to the browser
chrome_options.add_experimental_option("debuggerAddress",
                                       "127.0.0.1:9222")  # Use the remote debugging port to operate the browser to avoid being monitored as being controlled by an automated program
# Disable browser popups
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
chrome_options.add_experimental_option('prefs', prefs)
# Forbidden plugin
chrome_options.add_argument('--disable-plugins')
# Disable popup blocking
chrome_options.add_argument('--disable-popup-blocking')

# Create a WebDriver object (usually the default is wd), specify the Chrome browser driver, and add the above configuration
wd = webdriver.Chrome(
    executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
    options=chrome_options,
)
# fp = webdriver.FirefoxProfile(
#     r'C:\Users\3mora\AppData\Roaming\Mozilla\Firefox\Profiles\63z4wsqh.default-release')
# self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
# self.user_data = os.path.expanduser("~") + r'\AppData\Local\Google\Chrome\User Data'
# try:
#     pros = subprocess.Popen(
#         '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
#         rf' --user-data-dir="{self.user_data}" '
#         ' --remote-debugging-port=9222')
# except:
#     pros = subprocess.Popen(
#         '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
#         rf' --user-data-dir="{self.user_data}"'
#         '  --remote-debugging-port=9222')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15')
# options.add_argument('--disable-plugins-discovery')
# options.add_argument('referer=https://www.google.com/')
# options.add_argument('excludeSwitches', ['enable-automation'])
# options.add_argument('--disable-extensions')
# options.add_argument('--profile-directory=Default')
# options.add_argument('--disable-blink-featuresi=AutomationControlled')
#
# profile.set_preference('excludeSwitches', 'enable-automation')
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()