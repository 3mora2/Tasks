import warnings

from selenium.webdriver import ActionChains

warnings.filterwarnings("ignore")

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

from time import sleep
import subprocess


class Main:
    URL = 'https://www.royalairmaroc.com/int/'

    def __init__(self):
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
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def start(self):
        self.driver.get(self.URL)
        self.driver.get("https://www.royalairmaroc.com/int/")
        sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, ".location-picker-input:nth-child(2)").click()
        sleep(2)
        self.driver.find_elements(By.CSS_SELECTOR, ".location-picker-list-option > .primary-info")[0].click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".display-text").click()
        sleep(2)
        actions = ActionChains(self.driver)
        date1 = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Saturday, June 19, 2021"] > span  > .day')
        actions.move_to_element(date1).perform()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Saturday, June 19, 2021"] > span  > .day').click()
        sleep(2)
        date2 = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Saturday, July 31, 2021"] > span  > .day')
        actions.move_to_element(date2).perform()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Saturday, July 31, 2021"] > span  > .day').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".cabin").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".confirm-btn").click()
        sleep(3)
        self.driver.execute_script("document.querySelector('.path2').click()")


if __name__ == '__main__':
    app = Main()
    app.start()
