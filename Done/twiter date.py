from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import random

user_name = '8ic__'

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=chrome_options)
try:
    driver.get(f'https://twitter.com/{user_name}')
    sleep(2)
    followers = driver.find_element_by_css_selector(
        'div:nth-child(2) > a > span.css-901oao.css-16my406.r-1qd0xha.r-vw2c0b.r-ad9z0x.r-bcqeeo.r-qvutc0 > span').text
    if 'تغريدة مُثبَّتة' in driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div/div/div/div[2]/section/div/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]').text or 'Pinned Tweet' in driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div/div/div/div[2]/section/div/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]').text:
        times = driver.find_elements_by_tag_name('article')[1].find_element_by_css_selector(
            'div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a').get_attribute('title')
    else:
        times = driver.find_elements_by_tag_name('article')[0].find_element_by_css_selector(
            'div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a').get_attribute('title')

    print(followers, times)
except Exception as e:
    times = driver.find_elements_by_tag_name('article')[0].find_element_by_css_selector(
        'div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a').get_attribute('title')
    print(e)
    print(followers, times)