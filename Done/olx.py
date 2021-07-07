from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from time import sleep

book = Workbook()
sheet = book.active
sheet['A1'].value = 'الاسم'
sheet['B1'].value = "البائع"
sheet['C1'].value = "الرقم"
sheet['D1'].value = "الرابط"

sheet.column_dimensions['A'].width = 30
sheet.column_dimensions['B'].width = 15
sheet.column_dimensions['C'].width = 13
sheet.column_dimensions['D'].width = 70
sheet['A1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
sheet['B1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
sheet['C1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
sheet['D1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
phone = input('Enter your phone number : ')
password = input('Enter password : ')
url = input('Enter URL : ')
i = 2
l = []
driver = webdriver.Chrome()
driver.get('https://www.olx.com.eg/account/')
sleep(4)
driver.find_element_by_css_selector('#userEmail').send_keys(phone)
driver.find_element_by_css_selector('#userPass').send_keys(password)
driver.find_element_by_css_selector('#se_userLogin').click()
sleep(6)
driver.get(url)
# 'https://www.olx.com.eg/ads/?search%5Buser_id%5D=112424099&search%5Border%5D=filter_float_price%3Aasc')
while True:
    for ele in driver.find_elements_by_css_selector('div.ads__item > div:nth-child(2) > a:nth-child(1)'):
        try:
            if ele.get_attribute('href') not in l:
                l.append(ele.get_attribute('href'))
        except:
            pass
    print(len(l))
    try:
        driver.find_element_by_css_selector('span.item a.pageNextPrev').click()
        print('Next Page')
        sleep(2)
    except:
        break

for u in l:
    try:
        driver.get(u)
        sleep(2)
        name = driver.find_element_by_css_selector('h1.brkword').text
        driver.find_element_by_css_selector('div.contactbox-indent').click()
        sleep(4)
        try:
            user = driver.find_element_by_css_selector('.user-box__info__name').text
        except:
            user = None
        try:
            while True:
                number = driver.find_element_by_css_selector('div.contactbox-indent').text
                if 'x' not in number:
                    break

        except:
            number = None
        sheet[f'A{i}'].value = name
        sheet[f'A{i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        sheet[f'B{i}'].value = user
        sheet[f'B{i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        sheet[f'C{i}'].value = number
        sheet[f'C{i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        sheet[f'D{i}'].value = u
        sheet[f'D{i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        print(i, ' - ', number)
        book.save('olx.xlsx')
        i += 1
    except Exception as e:
        print(e)
