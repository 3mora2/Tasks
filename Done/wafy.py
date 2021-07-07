from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import subprocess


class Main:
    def __init__(self):
        chrome_options = Options()
        try:
            subprocess.Popen(
                '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
        except:
            subprocess.Popen(
                '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.implicitly_wait(5)

    def start(self):
        self.driver.get('https://mbasic.facebook.com/profile.php')
        input('- Enter........')
        urls = []
        total = 0
        dealt = 0
        while True:
            for element in self.driver.find_elements_by_css_selector('section > article'):
                try:
                    u = element.find_element_by_xpath('footer/div/a[text()="More"]').get_attribute('href')
                    if u not in urls:
                        total += 1
                        urls.append(u)
                except Exception as e:
                    print(e)

            print('- Number :', len(urls), 'All :', total)

            try:
                next_url = self.driver.find_element_by_xpath('//div[a/span[contains(text(),"See More Stories")]]/a'
                                                             ).get_attribute('href')

            except:
                print('- ***************** Finish ***************')
                break

            if len(urls) > 10:
                for index, url in enumerate(urls):
                    try:
                        self.driver.get(url)
                        sleep(1)
                        self.driver.find_element_by_css_selector('[value="DELETE"]').click()
                        sleep(1)
                        self.driver.find_element_by_css_selector('[value="Submit"]').click()
                        sleep(1)
                        dealt += 1
                        print('- DElET :', dealt, 'Now :', index+1)
                    except Exception as e:
                        print(e)
                urls = []
            print('- Next .......')
            self.driver.get(next_url)
            sleep(3)


if __name__ == '__main__':
    app = Main()
    # app.start()
