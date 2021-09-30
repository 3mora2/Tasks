from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import speech_recognition as sr
import subprocess
import requests
import os


def __cleanup(files):
    for x in files:
        if os.path.exists(x):
            os.remove(x)


chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
# remove title of automation
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument("--remote-debugging-port=9222")

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://google.com')

driver.get('https://patrickhlauke.github.io/recaptcha/')
sleep(3)
driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))
driver.find_element_by_css_selector('.recaptcha-checkbox-border').click()
sleep(1)
driver.switch_to.default_content()
sleep(3)
driver.switch_to.frame(driver.find_element_by_css_selector('iframe[title="recaptcha challenge"]'))
driver.find_element_by_css_selector('button.rc-button-audio').click()
sleep(3)
try:
    mp3_file = 'test.mp3'
    wav_file = 'test.wav'
    url = driver.find_element_by_css_selector('a.rc-audiochallenge-tdownload-link').get_attribute('href')

    rr = requests.get(url)
    if rr.ok:
        with open(mp3_file, 'wb')as f:
            f.write(rr.content)

        with open(os.devnull, "w") as f:
            subprocess.Popen(["ffmpeg", "-i", mp3_file, wav_file], stdin=f, stdout=f, stderr=f).communicate()

        r = sr.Recognizer()
        harvard = sr.AudioFile(r'test.wav')
        with harvard as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        driver.find_element_by_id("audio-response").send_keys(text)
        driver.find_element_by_id("recaptcha-verify-button").click()
        print(text)
        __cleanup([mp3_file, wav_file])
    else:
        print('- Not Found audio')

except Exception as e:
    print(e)
    print('- Not Found audio')


'''
https://github.com/skotz/cbl-js
'''
