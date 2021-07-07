# -- Install Require --
# pip install  requests  selenium  webdriver-manager  xlrd PyPDF2  mysql-connector openpyxl

# Selenium
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import re
# Import DataBase
from database_py import Main_DB
from time import sleep
import os
import xlrd
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
# username = "1003438858"
# password = "y8107369y"

# username = "1019247863"
# password = "as3236150"
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
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tbGn"))).send_keys(username)
        sleep(2)

        # Send Pass
        # self.driver.find_element_by_id("tbGpr").send_keys(password)
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tbGpr"))).send_keys(password)

        # Wait Until User Enter Code And Login
        wait = WebDriverWait(self.driver, 100)
        wait.until(ec.url_to_be('https://noor.moe.gov.sa/Noor/EduWavek12Portal/HomePage.aspx'))
        self.absence_alert()

    def absence_alert(self):
        # To Close Alert
        absence_alert = self.driver.find_element_by_id("btnCancel")
        if absence_alert.is_displayed():
            absence_alert.click()

    def export_con(self):
        self.open_category(cat='البيانات الخاصة بالارشاد الطلابي', ul="#ul41")
        n = os.listdir(self.path)
        sleep(2)
        self.wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_PlaceHolderMain_ibtnExportButton"))).click()
        # self.save_as()
        self.download_wait_2(self.path, n)
        school_id, school_stage, wb = self.add_school_db()
        self.student_midterm(school_stage)

        list_names, choose = self.dict_info(wb, school_id)
        print(choose)
        self.read_students(list_names, choose, school_stage, school_id)

    def export(self):
        list_wait, list_done, main_school = self.school_number()
        if main_school:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, '//a[text()="بياناتي الشخصية"]'))).click()
            school_name = self.driver.find_element_by_xpath(
                '//span[contains(@id,"ctl00_PlaceHolderMain_lblSchoolDes")]').text
            list_done.append(school_name)
            self.export_con()

        for school in list_wait:
            if school not in list_done:
                self.select_schools(school)
                print(school)
                self.absence_alert()
                try:
                    self.wait.until(ec.visibility_of_element_located((By.XPATH, '//a[text()="بياناتي الشخصية"]'))).click()
                except:
                    self.select_schools(school)
                    print(school)
                    self.wait.until(ec.visibility_of_element_located((By.XPATH, '//a[text()="بياناتي الشخصية"]'))).click()

                school_name = self.driver.find_element_by_xpath(
                    '//span[contains(@id,"ctl00_PlaceHolderMain_lblSchoolDes")]').text
                if school_name in list_done:
                    continue
                self.export_con()

                list_done.append(school)
                list_done.append(school_name)

    def add_school_db(self):
        filename = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if '.xls' in f], key=os.path.getctime)
        print(filename)
        wb = xlrd.open_workbook(filename)
        school_sheet = wb.sheet_by_name("Sheet1")
        school_name = school_sheet.cell_value(3, 2)
        school_stage = int(school_sheet.cell_value(4, 2))
        school_id = self.Class_DB.add_school(school_name, school_stage)
        print('school_id : ', school_id)
        self.add_class_db(wb, school_id)
        return school_id, school_stage, wb

    def add_class_db(self, wb, school_id):
        classes_sheet = wb.sheet_by_name("Sheet3")
        for j in range(4, classes_sheet.nrows):
            class_id = classes_sheet.cell_value(j, 10)
            class_name = classes_sheet.cell_value(j, 9)
            class_sec_name = classes_sheet.cell_value(j, 8)
            class_num = int(classes_sheet.cell_value(j, 7))
            self.Class_DB.add_class(class_id, class_name, class_sec_name, class_num, school_id)

    def student_midterm(self, stage):
        if stage == 1:
            self.open_category(cat='إشعار فترات أعمال السنة', ul="#ul165", scroll=True)

        elif stage == 2:
            self.open_category(cat='إشعار درجات اعمال السنة', ul="#ul166")

    def click_xpath(self, xpath):
        try:
            self.check_wait()
            self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, f".//select/option[text()='{xpath}']"))).click()
        except:
            return False

    def check_wait(self):
        while True:
            if self.driver.find_element_by_id('Loading').is_displayed():
                sleep(1)
            else:
                sleep(1)
                break

    def ch_wait(self):
        while True:
            try:
                if self.driver.find_element_by_xpath('//*[contains(@id,"AsyncWait_Wait")]').is_displayed():
                    sleep(1)
                else:
                    sleep(1)
                    break
            except:
                break

    def dict_info(self, wb, school_id):
        choose = set()
        list_names = dict()
        sheet = wb.sheet_by_name("Sheet2")
        for i in range(4, sheet.nrows):
            phone = sheet.cell_value(i, 1)
            class_num = sheet.cell_value(i, 2)
            class_id = sheet.cell_value(i, 3)
            name = sheet.cell_value(i, 4)
            stud_id = sheet.cell_value(i, 5)

            class_info = self.Class_DB.select_class_info(str(class_id), class_num, school_id)
            class_name = class_info[1]
            section_name = class_info[2]

            choose.add((class_num, class_name, section_name))
            list_names[name] = {'phone': phone, "class_num": class_num, "class_id": class_id, 'stud_id': stud_id,
                                'class_name': class_name, 'section_name': section_name}

        choose = sorted(choose, key=lambda x: (x[1], x[2], x[0]))
        return list_names, choose

    def read_students(self, list_names, choose, stage, id_s):
        print(stage)
        first = 'الفصل الأول'
        times = 'أولى'
        times_1 = 'الفترة الأولى'
        for ch in choose:
            if stage == 1:
                elements = [ch[1], ch[2], ch[0], times_1]
            elif stage == 2:
                elements = [first, 'منتظم', ch[1], ch[2], ch[0], times]
            else:
                print('Not Define')
                continue

            for text in elements:
                self.click_xpath(text)
                sleep(1)

            self.check_wait()
            # Export File As Excel And PDF
            r = self.export_file(file='Excel')
            if r is False:
                continue
            self.export_file(file='PDF', show=False)
            self.split_pdf_1(self.path, list_names, id_s, stage=stage)

    def move_file(self, stud_id, file='PDF', extent='pdf'):
        path_pdf = self.path + fr'{file}'
        if not os.path.exists(path_pdf):
            os.makedirs(path_pdf)

        filename = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if f'.{extent}' in f], key=os.path.getctime)
        old_file = os.path.join(self.path, filename)
        new_file = os.path.join(path_pdf, stud_id + f'.{extent}')
        os.rename(old_file, new_file)

    def select_schools(self, title):
        # To Show All School
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
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
                ec.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
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

    def open_category(self, cat, ul, scroll=False):
        not_ter_sum = (By.XPATH, f"// ul /li /a[contains(text(),'{cat}')]")
        btn_cat = f'div[href="{ul}"]'

        self.wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
        try:
            student_data = self.wait_5.until(ec.visibility_of_element_located(not_ter_sum))
            if student_data.is_displayed() is False:
                self.driver.find_element_by_css_selector(btn_cat).click()
        except:
            self.driver.find_element_by_css_selector(btn_cat).click()

        if scroll:
            _ = self.driver.find_element_by_xpath("//div[@href='#ul163']").location_once_scrolled_into_view
        try:
            self.wait.until(ec.visibility_of_element_located(not_ter_sum)).click()
        except:
            print('- re click ')
            self.wait.until(ec.visibility_of_element_located(not_ter_sum)).click()

    def export_file(self, show=True, file="PDF"):
        try:
            num_file = os.listdir(self.path)
            if show:
                self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[title="عرض"]'))).click()
            # sleep(4)
            self.check_wait()
            self.ch_wait()
            self.wait_3.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"] > span'))).click()
            try:
                self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{file}"]'))).click()
            except:
                sleep(2)
                print('- reExport -----------')
                self.wait_3.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"] > span'))).click()
                self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{file}"]'))).click()

            self.download_wait_2(self.path, num_file)
        except:
            return False

    def split_pdf_1(self, out_path, list_names, school_id, stage=1):
        file_xlsx = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if f'.xlsx' in f], key=os.path.getctime)
        file_pdf = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if f'.pdf' in f], key=os.path.getctime)

        # Open Xlsx File
        book = load_workbook(file_xlsx, read_only=True)
        # Get All Sheets
        sheets = book.worksheets
        # Open PDF
        read_pdf = PyPDF2.PdfFileReader(file_pdf)

        for num, sheet in enumerate(sheets):
            pdf = ''
            if stage == 2:
                name = sheet['AF28'].value.strip().split(':')[-1]
            else:
                name = sheet['X12'].value
                if name is None:
                    name = sheet['T12'].value
                    pdf = '-1'
            name = name.strip()
            if name not in list_names.keys():
                print('- Not found : ', name)
                continue

            phone = list_names[name]['phone']
            class_num = list_names[name]['class_num']
            class_id = list_names[name]['class_id']
            stud_id = list_names[name]['stud_id']

            pdf = ''.join(re.findall(r'\w+', stud_id)) + pdf + ".pdf"
            self.Class_DB.add_student(stud_id, name, phone, class_id, class_num, school_id, pdf_name=pdf)
            # Split PDF
            page = read_pdf.getPage(num)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(page)

            with open(out_path + '\\' + pdf, 'wb') as fh:
                pdf_writer.write(fh)

            print(num, pdf, name)

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
        app.export()
    else:
        print('- Please Enter Username and Password and User Id')
