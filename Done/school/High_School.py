# -- Install Require --
# pip install  requests  selenium  webdriver-manager  xlrd PyPDF2  mysql-connector

# Selenium
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

# Import DataBase
from database_py import Main_DB

from time import sleep
import os

import csv
import PyPDF2
from openpyxl import load_workbook

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", help="username of user.")
ap.add_argument("-p", "--pass", help="password of user.")
ap.add_argument("-i", "--id", help="id of user.")
args = vars(ap.parse_args())
username = args['user']
password = args['pass']
user_id = args['id']
print(username, password, user_id)
# high
# username = '1041591965'
# password = '141599ttss'
# user_id = "11"


class Main:
    # Path To Download Files
    path = rf'E:\Programming\Wael\school\{username}'
    if not os.path.exists(path):
        os.makedirs(path)

    def __init__(self):

        # Main_DB Class from file database
        self.Class_DB = Main_DB(user_id=user_id)

        # Chrome Option
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.path}
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        # General Wait To Avoid Weak Internet
        self.driver.implicitly_wait(5)

        # Special Wait
        self.wait_5 = WebDriverWait(self.driver, 5)
        self.wait = WebDriverWait(self.driver, 20)
        self.wait_3 = WebDriverWait(self.driver, 30)

    def login(self):
        # Open Url
        self.driver.get("https://noor.moe.gov.sa/Noor/Login.aspx")
        sleep(2)

        # Send UserName
        # self.driver.find_element_by_id("tbGn").send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tbGn"))).send_keys(username)
        sleep(2)

        # Send Pass
        # self.driver.find_element_by_id("tbGpr").send_keys(password)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tbGpr"))).send_keys(password)

        # Wait Until User Enter Code And Login
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.url_to_be('https://noor.moe.gov.sa/Noor/EduWavek12Portal/HomePage.aspx'))
        self.absence_alert()

    def absence_alert(self):
        # To Close Alert
        absence_alert = self.driver.find_element_by_id("btnCancel")
        if absence_alert.is_displayed():
            absence_alert.click()

    def Click_XPATH(self, xpath):
        try:
            self.Check_wait()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f".//select/option[text()='{xpath}']"))).click()
        except:
            return False

    def Check_wait(self):
        while True:
            if self.driver.find_element_by_id('Loading').is_displayed():
                sleep(1)
            else:
                sleep(1)
                break

    def Ch_wait(self):
        while True:
            try:
                if self.driver.find_element_by_xpath('//*[contains(@id,"AsyncWait_Wait")]').is_displayed():
                    sleep(1)
                else:
                    sleep(1)
                    break
            except:
                break

    def select_schools(self, title):
        # To Show All School
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
        sleep(2)

        # Open School
        for ele in self.driver.find_elements_by_xpath(
                "//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]"):
            if title in ele.text:
                ele.click()
                break
        sleep(2)

        # Try Show Tab_bar In Side
        try:
            self.driver.find_element_by_css_selector('.HamButt').click()
        except:
            pass

    def school_number(self):
        list_done = []
        list_wait = []
        main_school = False
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
            sleep(2)
            num = self.driver.find_elements_by_xpath(
                "//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]")
            if len(num) != 0:
                for ele in num:
                    list_wait.append(ele.text)
        except Exception as e:
            print(e)
        print(len(list_wait))
        if 'قائد' in self.driver.find_element_by_css_selector('span.usersubinfo').text:
            list_done.append(self.driver.find_element_by_css_selector('span.usersubinfo').text)
            main_school = True
        return list_wait, list_done, main_school

    def high(self):
        list_wait, list_done, main_school = self.school_number()
        if main_school:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="بياناتي الشخصية"]'))).click()
            school_name = self.driver.find_element_by_xpath(
                '//span[contains(@id,"ctl00_PlaceHolderMain_lblSchoolDes")]').text
            self.export_high()
            school_id = self.add_h_school_db(school_name)
            self.sheet_term_short(school_id)
            list_done.append(school_name)

        for school in list_wait:
            if school not in list_done:
                self.select_schools(school)
                self.absence_alert()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="بياناتي الشخصية"]'))).click()
                school_name = self.driver.find_element_by_xpath(
                    '//span[contains(@id,"ctl00_PlaceHolderMain_lblSchoolDes")]').text
                if school_name in list_done:
                    continue
                self.export_high()
                school_id = self.add_h_school_db(school_name)
                self.sheet_term_short(school_id)
                list_done.append(school)
                list_done.append(school_name)
                print(len(list_done))
                print(len(list_wait))

    def export_high(self):
        num_file = os.listdir(self.path)
        select_extra_services = (By.XPATH, '//a[text()="خدمات إضافية"]')
        select_message = (By.XPATH, '//div/a[text()="الرسائل"]')
        select_phone_user_down = (By.XPATH, '//div/a[text()="تحميل أرقام هواتف المستخدمين"]')
        select_export_phone_user = (By.XPATH, '//div/a[text()="تصدير  نموذج أرقام هواتف المستخدمين"]')
        select_option_student = (By.XPATH, '//*[@id="ctl00_PlaceHolderMain_ddlUserTypes"]/option[text()="طالب"]')
        select_export = (By.CSS_SELECTOR, 'input[title="تصدير"]')
        select_export_Data = (By.CSS_SELECTOR, 'input#ctl00_PlaceHolderMain_ibtnCloseForExportData')
        for select in [select_extra_services, select_message, select_phone_user_down, select_export_phone_user,
                       select_option_student, select_export, select_export_Data]:
            self.wait.until(EC.visibility_of_element_located(select)).click()
            sleep(2)
        self.download_wait_2(self.path, num_file)

    def add_h_school_db(self, school_name, school_stage=3):
        self.names = dict()
        school_id = self.Class_DB.add_school(school_name, school_stage)
        filename = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if '.csv' in f], key=os.path.getctime)
        print(filename)
        with open(filename, newline='', encoding='cp1256') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            _ = next(csv_reader)
            _ = next(csv_reader)
            for row in csv_reader:
                stud_id = row[0]
                name = row[1].strip()
                phone = str(row[2]).replace('.0', '')
                class_num = row[3]
                self.names[name] = stud_id
                # section = df['SectionName'][i]
                self.Class_DB.add_student(stud_id, name, phone, None, class_num, school_id)
                print(name)

        return school_id

    def open_category(self, cat, ul, scroll=False):
        not_ter_sum = (By.XPATH, f"// ul /li /a[contains(text(),'{cat}')]")
        btn_cat = f'div[href="{ul}"]'

        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
        try:
            student_data = self.wait_5.until(EC.visibility_of_element_located(not_ter_sum))
            if student_data.is_displayed() is False:
                self.driver.find_element_by_css_selector(btn_cat).click()
        except:
            self.driver.find_element_by_css_selector(btn_cat).click()

        if scroll:
            _ = self.driver.find_element_by_xpath("//div[@href='#ul163']").location_once_scrolled_into_view
        try:
            self.wait.until(EC.visibility_of_element_located(not_ter_sum)).click()
        except:
            print('- re click ')
            self.wait.until(EC.visibility_of_element_located(not_ter_sum)).click()

    def Export_File(self, show=True, file="PDF"):
        try:
            num_file = os.listdir(self.path)
            if show:
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="عرض"]'))).click()
            # sleep(4)
            self.Check_wait()
            self.Ch_wait()
            self.wait_3.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"] > span'))).click()
            try:
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{file}"]'))).click()
            except:
                sleep(2)
                print('- reExport -----------')
                self.wait_3.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"] > span'))).click()
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{file}"]'))).click()

            self.download_wait_2(self.path, num_file)
        except:
            return False

    def Split_pdf_2(self, out_path, school_id):
        file_xlsx = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if f'.xlsx' in f], key=os.path.getctime)
        file_pdf = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if f'.pdf' in f], key=os.path.getctime)

        # Open Xlsx File
        book = load_workbook(file_xlsx, read_only=True)
        # Get All Sheets
        sheets = book.worksheets

        # Open PDF
        read_pdf = PyPDF2.PdfFileReader(file_pdf)

        for num, sheet in enumerate(sheets):
            name = sheet['AD19'].value.strip()
            st_id = self.names[name]
            pdf = self.Class_DB.update_student(name, school_id, st_id)

            # Split PDF
            page = read_pdf.getPage(num)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(page)

            with open(out_path + '\\' + pdf, 'wb') as fh:
                pdf_writer.write(fh)

            print(num, pdf, name)

    def sheet_term_short(self, school_id):
        print(school_id)
        self.open_category(cat='إشعار فصلي مختصر', ul="#ul303")

        # choose first term
        app.Click_XPATH('الفصل الدراسي الأول 1439-1440')

        # Export File As Excel And PDF
        self.Export_File(file='Excel')
        self.Export_File(file='PDF', show=False)

        # Update Student Certificate
        self.Split_pdf_2(self.path, school_id)

    @staticmethod
    def download_wait_2(directory, filenames):
        while True:
            files = os.listdir(directory)
            new_l = set(files) - set(filenames)
            if len(new_l) != 0:
                if list(new_l)[0].endswith('.crdownload'):
                    sleep(6)
                    print('- Yet : .crdownload')
                else:
                    break
            else:
                print('- Yet')
                sleep(4)


if __name__ == '__main__':
    if username and password and user_id:
        app = Main()
        app.login()
        app.absence_alert()
        app.high()
    else:
        print('- Please Enter Username and Password and User Id')
