import smtplib
from email.message import EmailMessage

from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from PySide2.QtCore import Signal, QThread
from time import sleep
import json

from aqar_way import FULL_NAMES, OTHER_VALIDATION, VALIDATION


class StartAqar(QThread):
    driver: WebDriver
    final = Signal()
    error = Signal()
    pause = False
    stop = False
    skip = False
    tableWidget_2: QTableWidget
    # element_s = "h4 a.listTitle"
    element_s = '.listing_LinkedListingCard__5SRvZ a'

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def run(self) -> None:
        self.pause = False
        self.stop = False
        self.skip = False

        if not self.check():
            self.error.emit()
            return

        url = self.select_number(self.init, self.driver.current_url)
        self.driver.get(url)
        page = 1
        while True:
            while self.pause:
                if self.stop:
                    break

                sleep(1)

            if self.stop:
                break

            if self.skip:
                break
            links = [self.tableWidget_2.item(i, 0).text() for i in range(self.tableWidget_2.rowCount())]
            for element in self.driver.find_elements(By.CSS_SELECTOR, self.element_s):
                while self.pause:
                    if self.stop:
                        break
                    sleep(1)

                if self.stop:
                    break

                if self.skip:
                    break

                link = element.get_attribute('href')

                if link not in links:
                    print(len(links), page)
                    try:
                        r = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(r)
                        self.tableWidget_2.setItem(r, 0, QTableWidgetItem(str(link)))
                    except Exception as e:
                        print(e)

            if page == self.num:
                break

            try:
                next_url = self.driver.find_element_by_css_selector('#next-page').get_attribute('href')
                self.driver.get(next_url)
                sleep(1)
                page += 1
            except:
                break

        self.get_posts()

        if self.is_send_email:
            self.send_mail()
        self.final.emit()

    def get_posts(self):
        for i in range(self.tableWidget_2.rowCount()):
            link = self.tableWidget_2.item(i, 0).text()
            sleep(self.sleep)
            while self.pause:
                if self.stop:
                    break

                sleep(1)

            if self.stop:
                break

            self.driver.get(link)
            sleep(2)
            # text = self.driver.find_element_by_xpath('//script[contains(text(), "window.__store__")]').get_attribute(
            #     'innerText').replace(
            #     'window.__store__ = ', '')
            text = self.driver.find_element_by_css_selector('script#__NEXT_DATA__').get_attribute(
                'innerText').replace(
                'window.__store__ = ', '')
            data = json.loads(text)
            # user_info_id = list(data['usersReducer'].get('usersInfo'))[0]
            data_info = data['listingReducer']['selectedListing']
            user_name = data_info.get('user').get("name")
            # user_type = data_info.get('user').get("type")
            # user_paid = data_info.get('user').get("paid")
            # user_fee = data_info.get('user').get("fee")
            try:
                imgs = list(
                    map(lambda x: 'https://images.aqar.fm/' + x, data['listingReducer']['selectedListing']['imgs']))
            except:
                imgs = []
            data_info['imgs'] = ', '.join(imgs)

            try:
                videos = list(
                    map(lambda x: x.get('video'), data['listingReducer']['selectedListing']['videos']))
            except:
                videos = []
            data_info['videos'] = ', '.join(videos)
            data_info.pop('verified')
            data_info.pop('user')
            data_info.pop('views')
            data_info.pop('links')
            data_info.pop('related')
            data_info['user_name'] = user_name

            # try:
            #     area = self.driver.find_element_by_xpath('//tr[td[contains(text(),"المساحة")]] /td[div]').text
            # except:
            #     area = None
            # try:
            #     price_m = self.driver.find_element_by_xpath('//tr[td[contains(text(),"سعر المتر")]] /td[div]').text
            # except:
            #     price_m = None
            #
            # try:
            #     direct = self.driver.find_element_by_xpath('//tr[td[contains(text(),"الواجهة")]] /td[div]').text
            # except:
            #     direct = None
            #
            # try:
            #     props = self.driver.find_element_by_xpath('//tr[td[contains(text(),"الغرض")]] /td[div]').text
            # except:
            #     props = None
            #
            # try:
            #     wh = self.driver.find_element_by_xpath('//tr[td[contains(text(),"عرض الشارع")]] /td[div]').text
            # except:
            #     wh = None
            # data_info['الواجهة'] = direct
            # data_info['المساحة'] = area
            # data_info['سعر المتر'] = price_m
            # data_info['الغرض'] = props
            # data_info['عرض الشارع'] = wh

            try:
                last = self.driver.find_element_by_css_selector('span.userViewPhone').text
                self.driver.find_element_by_css_selector('span.userViewPhone').click()
                while True:
                    phone = self.driver.find_element_by_css_selector('span.userViewPhone').text
                    if phone != last:
                        if phone.startswith('05'):
                            phone = '+966'+phone[1:]
                        break
                    if self.driver.find_elements_by_css_selector('#popup-content'):
                        phone = None
                        break

            except:
                phone = None
            data_info['location'] = f'lat: {data_info["location"].get("lat")}, lng: {data_info["location"].get("lng")}'
            data_info['phone'] = phone
            if data_info['age'] == 0:
                data_info['age'] = 'جديد'
            data_info = self.check_value(data_info)

            self.update_headers(data_info)

            for c, key in enumerate(data_info.keys()):
                if data_info[key] is not None:
                    self.tableWidget_2.setItem(i, c+1, QTableWidgetItem(str(data_info[key])))

            print(i)

        self.driver.quit()

    @staticmethod
    def select_number(n, url):
        if '?' in url:
            url = url.split('?')[0]

        list_url = url.split('/')
        if list_url[-1].isnumeric():
            list_url[-1] = str(n)
            url = '/'.join(list_url)
        else:
            url = '/'.join(list_url) + '/' + str(n)
        return url

    @staticmethod
    def replace(key):
        value = FULL_NAMES.get(key, None)
        if value:
            return value.get('name').get('ar')

        return key

    def update_headers(self, data_info):
        old_headers = [self.tableWidget_2.horizontalHeaderItem(c).text() for c in
                       range(self.tableWidget_2.columnCount())]

        if old_headers.__len__() < len(data_info.keys()):
            old_headers += data_info.keys()
            old_headers = list(map(self.replace, old_headers))
            self.tableWidget_2.setColumnCount(len(old_headers))
            self.tableWidget_2.setHorizontalHeaderLabels(old_headers)

    def check_value(self, data_info):
        for key in data_info.keys():
            value = data_info[key]
            if key in OTHER_VALIDATION.keys():
                data_info[key] = f'{value} {OTHER_VALIDATION.get(key)}'
            elif key in VALIDATION.keys():
                options = VALIDATION.get(key, {}).get('options')
                if options:
                    result = list(filter(lambda x: value is not None and (x.get('value') == value), options))
                    if result:
                        result = result[0]
                        data_info[key] = result.get('title')

        return data_info

    def send_mail(self):
        try:
            topic = 'تم الانتهاء من استخراج البيانات'
            subject = 'تم الانتهاء'
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.SENDER_EMAIL
            msg['To'] = self.Recipient_email
            msg.set_content(topic)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.SENDER_EMAIL, self.APP_PASSWORD)
                smtp.send_message(msg)
        except Exception as e:
            print(e)