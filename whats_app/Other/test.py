from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-plugins')
# chrome_options.add_argument('--disable-popup-blocking')
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
# driver.find_element_by_css_selector('div[role="button"][title="إرفاق"]').click()
# driver.find_element_by_css_selector('[data-testid="attach-image"]+input').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")
# driver.find_element_by_css_selector('[class="_13NKt copyable-text selectable-text"][data-tab="6"]').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")
#
# driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()
# driver.find_element_by_css_selector('[data-testid="attach-document"]+input[type="file"]').send_keys(r"C:\Users\3mora\Dropbox\All\whats_app\1.png")
# driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()
# list_num = []
# old = 0
# error = 0
# while True:
#
#     for element in driver.find_elements_by_xpath(
#             '//div[div[@role="row"]//span[@data-testid="default-group"]] //div[@role="gridcell"]/div/span'):
#         print(element.text)
#     for element in driver.find_elements_by_xpath(
#             '//div[div[@role="row"]] //div[@role="gridcell"]/div/span'):
#         if element.text not in list_num:
#             list_num.append(element.text)
#
#     if old == list_num.__len__():
#         error += 1
#         sleep(2)
#         print('-same')
#     else:
#         error = 0
#     old = list_num.__len__()
#     driver.find_element_by_css_selector('#pane-side > div:nth-child(3)').send_keys(Keys.PAGE_DOWN)
#     sleep(1)
#     print('-------------------')
#     if error == 3:
#         break


# driver.find_element_by_css_selector('#side .copyable-text.selectable-text').send_keys('.')
# sleep(1)
# driver.find_element_by_xpath(
#             '//div[div[@role="row"]//span[@data-testid="default-group"]] //div/span[contains(@title, "Noo")]').click()

JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """
text = """
زيادة متابعين انستقرام👀
كلنا نبي زباين ومتابعين صح؟🥳
اي زبون يدخل ع حسابك مباشرة يروح ع عدد المتابعين

عشان يشوف إذا عدد المتابعين كثير اكيد اول فكرة بتكون في باله انه اكيد المشروع ناجح ويفكر يجرب يطلب منتجك أو خدمتك 😇

 
  5 الالف متابع 🎆 80﷼

10 الالف متابع🎆 160﷼ 

20 الف متابع🎆 240﷼

 30 الف متابع🎆 330 ﷼

  50 الف متابع🎆 500 ﷼


 ( وصف الخدمة ) 

⛔تعويض المتابعين ف حال النقص

⛔ 20 يوم ضمان

⛔ متابعين اجانب

⛔ تبدأ تجيك الإضافات بعد ساعه 
➖➖➖➖➖➖➖➖➖➖
لتواصل على الواتس.
https://wa.me/966551326563
"""
# elem = WebDriverWait(driver, 5).until(
#     (ec.presence_of_element_located((By.CSS_SELECTOR,
#                                      '#main .copyable-area .copyable-text.selectable-text[contenteditable="true"]'))))
# .send_keys(t, Keys.SHIFT, Keys.ENTER)
# driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, text)
# element = driver.find_element_by_css_selector('#app > div._1ADa8._3Nsgw.app-wrapper-web.font-fix.os-win > div._1XkO3.two > div._3ArsE > div.ldL67._3sh5K > span > div._3bvta > span > div:nth-child(1) > div > div.KPJpj._2M_x0 > div._1YHIM > span > div > div._1urgr > div > div._1paHP > div._1UWac.Z2O8p.oHEu9 > div._13NKt.copyable-text.selectable-text')
# script = """var elm = arguments[0],
# txt = arguments[1];
# elm.textContent = txt;
# elm.dispatchEvent(new Event('keydown', {bubbles: true}));
# elm.dispatchEvent(new Event('keypress', {bubbles: true}));
# elm.dispatchEvent(new Event('input', {bubbles: true}));
# elm.dispatchEvent(new Event('keyup', {bubbles: true}));"""
# element.send_keys('')
# driver.execute_script(script, element, text)
