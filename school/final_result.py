#   pip install  requests  selenium  webdriver-manager  xlrd pandas
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
# from database_py import Main_DB
from selenium import webdriver
from time import sleep
import xlrd
import csv
import pandas
import os
import autoit

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

username = '1041591965'
password = '141599ttss'
# username = "1019247863"
# password = "as3236150"
# username = "1003438858"
# password = "y8107369y"
user_id = "11"
# SHORT_TIMEOUT = 3  # give enough time for the loading element to appear
# LONG_TIMEOUT = 5  # give enough time for loading to finish


class Main:
    # Path To Download Files
    # self.path = r'C:\Download'

    path = rf'G:\programing\projects\drob\wael\school\{username}'
    if not os.path.exists(path):
        os.makedirs(path)

    def __init__(self):

        # Main_DB Class from file database
        # self.Class_DB = Main_DB(user_id=user_id)

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
        # To Solve Code, Still Not Work
        # for i in range(100, 1000):
        #     self.driver.find_element_by_id('divGGchh').screenshot(f'{i}.png')
        #     self.driver.refresh()
        #     sleep(3)
        # code = text.new_v('text.png')
        # print(code)
        # if code is not False:
        #     self.driver.find_element_by_id("tbGc").send_keys(code)
        #     sleep(1)
        #     self.driver.find_element_by_id("btnSubl").click()
        #     sleep(1)
        #     if self.driver.current_url != 'https://noor.moe.gov.sa/Noor/EduWavek12Portal/HomePage.aspx':
        #         print('relogin')
        #         self.login()
        # else:
        #     print('refresh')
        #     self.driver.refresh()
        #     self.login()

    def absence_alert(self):
        # To Close Alert
        absence_alert = self.driver.find_element_by_id("btnCancel")
        if absence_alert.is_displayed():
            absence_alert.click()

    def schools(self, num):
        # To Show All School
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
        sleep(1)

        # Open School
        self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]")))[num].click()
        sleep(2)

        # Try Show Tab_bar In Side
        try:
            self.driver.find_element_by_css_selector('.HamButt').click()
        except:
            pass

    # If Open Pump Window Save As
    def save_as(self):
        try:
            autoit.win_wait_active("Save As", 6)
            autoit.control_set_text("Save As", 'Edit1', self.path)
            autoit.control_click("[Class:#32770]", "Button2")
            sleep(2)
            autoit.control_click("[Class:#32770]", "Button2")
            sleep(2)
            try:
                autoit.control_click("[Class:#32770]", "Button1")
            except:
                pass
        except Exception as e:
            print(e)

        sleep(10)

    def Export(self):
        # Detect Len Of School
        # school_len = len(self.wait.until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]"))))
        school = True
        school_len = len(self.driver.find_elements_by_xpath("//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]"))
        if school_len == 0:
            school_len = 1
            school = False
        first = 0
        for i in range(school_len):
            print(i)
            if school:
                self.schools(i-first)
                first = 1
                sleep(2)
            self.open_category(cat='البيانات الخاصة بالارشاد الطلابي', ul="#ul41")
            # try:
            #     self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
            # except Exception as e:
            #     print(e)
            #
            # try:
            #     student_data = self.wait_5.until(EC.visibility_of_element_located((By.XPATH, "// ul /li /a[contains(text(),'البيانات الخاصة بالارشاد الطلابي')]")))
            #     if student_data.is_displayed() is False:
            #         self.driver.find_element_by_css_selector('div[href="#ul41"]').click()
            # except:
            #     self.driver.find_element_by_css_selector('div[href="#ul41"]').click()
            # sleep(1)
            # self.wait_5.until(EC.visibility_of_element_located(
            #     (By.XPATH, "// ul /li /a[contains(text(),'البيانات الخاصة بالارشاد الطلابي')]"))).click()
            n = len(os.listdir(self.path))
            sleep(2)
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_PlaceHolderMain_ibtnExportButton"))).click()
            # self.save_as()
            print(self.Class_DB.download_wait(self.path, 150, n))
            school_id, school_stage, wb = self.add_school_db()
            self.student_midterm(school_stage)
            self.read_students(wb, school_id, school_stage)

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
        # self.driver.find_element_by_id("divMenuItem_321").find_element_by_xpath(".//a[@href='#']").click()
        # sleep(2)
        if stage == 2:
            self.open_category(cat='إشعار درجات اعمال السنة', ul="#ul166")
            # self.driver.find_element_by_xpath(".//div[@href='#ul166']").click()
            # sleep(2)
            # self.wait.until(
            #     EC.element_to_be_clickable((By.XPATH, ".//a[contains(text(),'إشعار درجات اعمال السنة')]"))).click()

        elif stage == 1:
            self.open_category(cat='إشعار فترات أعمال السنة', ul="#ul165", scroll=True)
            # self.driver.find_element_by_xpath(".//div[@href='#ul165']").click()
            # sleep(2)
            # _ = self.driver.find_element_by_xpath("//div[@href='#ul163']").location_once_scrolled_into_view
            # self.wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "//li[a[contains(text(),'إشعار فترات أعمال السنة')]]"))).click()
            ##########################################################################################################
            # while True:
            #     if self.wait.until(
            #             EC.element_to_be_clickable((By.XPATH, "//li[a[contains(text(),'إشعار فترات أعمال السنة')]]"))).is_displayed():
            #         break
            #     else:
            #         _ = self.wait.until(
            #             EC.element_to_be_clickable((By.XPATH, "//li[a[contains(text(),'إشعار فترات أعمال السنة')]]"))).location_once_scrolled_into_view
            #         print('- Wait : (إشعار فترات أعمال السنة) ')
            #         sleep(1)

    def Click_XPATH(self, xpath):
        self.Check_wait()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f".//select/option[text()='{xpath}']"))).click()

    def Check_wait(self):
        while True:
            if self.driver.find_element_by_id('Loading').is_displayed():
                sleep(1)
            else:
                sleep(1)
                break

    def read_students(self, wb, school_id, stage):
        first = 'الفصل الأول'
        times = 'أولى'
        times_1 = 'الفترة الأولى'
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
            if self.Class_DB.student_exist(stud_id, school_id):
                print('- Found ')
                continue
            else:
                if stage == 1:
                    elements = [class_name, section_name, class_num, times_1, name]
                elif stage == 2:
                    elements = [first, 'منتظم', class_name, section_name, class_num, times, name]
                else:
                    print('Not Define')
                    continue

                for text in elements:
                    self.Click_XPATH(text)
                    sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, f".//select/option[text()='{first}']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #         (By.XPATH, ".//select/option[text()='منتظم']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, f".//select/option[text()='{class_name}']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, f".//select/option[text()='{section_name}']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, f".//select/option[text()='{class_num}']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #                     (By.XPATH, f".//select/option[text()='{times}']"))).click()
                # sleep(1)
                # self.wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, f".//select/option[text()='{name}']"))).click()
                # sleep(1)
                self.Check_wait()
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="عرض"]'))).click()
                sleep(2)
                # self.Check_wait()
                self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[title="تصدير"]'))).click()
                n = len(os.listdir(self.path))
                sleep(1)
                try:
                    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="PDF"]'))).click()
                except:
                    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"]'))).click()
                    sleep(1)
                    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="PDF"]'))).click()

                print(self.Class_DB.download_wait(self.path, 150, n))
                # sleep(3)
                path_pdf = self.path + r'\PDF'
                if not os.path.exists(path_pdf):
                    os.makedirs(path_pdf)
                filename = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if '.pdf' in f], key=os.path.getctime)
                old_file = os.path.join(self.path, filename)
                new_file = os.path.join(path_pdf, stud_id + ".pdf")
                os.rename(old_file, new_file)

                self.Class_DB.add_student(stud_id, name, phone, class_info[0], class_num, school_id)
                new = max([fr'{path_pdf}\{f}' for f in os.listdir(path_pdf) if '.pdf' in f], key=os.path.getctime)
                print(f"- {i-3} - Done, Student Id : {stud_id}, PDF : {new} ::::::::: {str(stud_id) in new}")

    def select_schools(self, title):
        # To Show All School
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
        sleep(2)

        # Open School
        for ele in self.driver.find_elements_by_xpath("//ul[contains(@class,'menu TopUsers')] / li / a[contains(text(),'قائد')]"):
            if title in ele.text:
                ele.click()
                break
        sleep(2)

        # Try Show Tab_bar In Side
        try:
            self.driver.find_element_by_css_selector('.HamButt').click()
        except:
            pass

    def high(self):
        list_done = []
        list_wait = []
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.switchUser > a.switchmenu"))).click()
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
            self.export_high()

        for school in list_wait:
            if school not in list_done:
                self.select_schools(school)
                self.export_high()
                list_done.append(school)
                print(len(list_done))
                print(len(list_wait))

    def export_high(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="خدمات إضافية"]'))).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div/a[text()="الرسائل"]'))).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div/a[text()="تحميل أرقام هواتف المستخدمين"]'))).click()
        sleep(2)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div/a[text()="تصدير  نموذج أرقام هواتف المستخدمين"]'))).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl00_PlaceHolderMain_ddlUserTypes"]/option[text()="طالب"]'))).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[title="تصدير"]'))).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#ctl00_PlaceHolderMain_ibtnCloseForExportData'))).click()
        # app.driver.find_element_by_xpath('//a[text()="خدمات إضافية"]').click()
        # app.driver.find_element_by_xpath('//div/a[text()="الرسائل"]').click()
        # app.driver.find_element_by_xpath('//div/a[text()="تحميل أرقام هواتف المستخدمين"]').click()
        # app.driver.find_element_by_xpath('//*[@id="ctl00_PlaceHolderMain_ddlUserTypes"]/option[text()="طالب"]').click()
        # app.driver.find_element_by_xpath('//div/a[text()="تصدير  نموذج أرقام هواتف المستخدمين"]').click()
        # app.driver.find_element_by_css_selector('#ctl00_PlaceHolderMain_ddlUserTypes > option[value="6"]').click()
        # app.driver.find_element_by_css_selector('input[title="تصدير"]').click()
        # app.driver.find_element_by_css_selector('input[value="إغلاق"]').submit()

    def read_csv(self):
        filename = max([fr'{self.path}\{f}' for f in os.listdir(self.path) if '.csv' in f], key=os.path.getctime)
        df = pandas.read_csv(filename, header=1, encoding='latin-1')
        print(df['MobileNumber'])

    def open_category(self, cat, ul, scroll=False):
        not_ter_sum = (By.XPATH, f"// ul /li /a[contains(text(),'{cat}')]")
        btn_cat = f'div[href="{ul}"]'
        
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
        try:
            student_data = self.wait_5.until(EC.visibility_of_element_located(not_ter_sum))
            if student_data.is_displayed() is False:
                self.driver.find_element_by_css_selector(btn_cat).click()
        except:
            self.driver.find_element_by_css_selector(btn_cat).click()

        if scroll:
            _ = self.driver.find_element_by_xpath("//div[@href='#ul163']").location_once_scrolled_into_view

        self.wait_5.until(EC.visibility_of_element_located(not_ter_sum)).click()

    def Export_File(self, show=True, file="PDF"):
        if show:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="عرض"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{file}"]'))).click()

    def new1(self):
        self.open_category(cat='إشعار فصلي مختصر', ul="#ul303")
        self.Export_File()
        # self.wait.until(EC.visibility_of_element_located(
            # (By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
        # try:
        #     student_data = self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'إشعار فصلي مختصر')]")))
        #     if student_data.is_displayed() is False:
        #         self.driver.find_element_by_css_selector('div[href="#ul303"]').click()
        #     self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'إشعار فصلي مختصر')]"))).click()
        # except:
        #     self.driver.find_element_by_css_selector('div[href="#ul303"]').click()
        #     self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'إشعار فصلي مختصر')]"))).click()
        # app.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="عرض"]'))).click()
        # app.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"]'))).click()
        # app.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="PDF"]'))).click()

    def new2(self):
        self.open_category(cat='كشف طالبات المدرسة مرتب بالرقم الأكاديمي', ul="#ul283")
        self.Export_File(show=False)
        # self.wait.until(EC.visibility_of_element_located(
        #     (By.CSS_SELECTOR, "ul > #divMenuItem_3257 ~ li#divMenuItem_321 > a"))).click()
        #
        # try:
        #     student_data = self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'كشف طالبات المدرسة مرتب بالرقم الأكاديمي')]")))
        #     if student_data.is_displayed() is False:
        #         self.driver.find_element_by_css_selector('div[href="#ul283"]').click()
        #     self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'كشف طالبات المدرسة مرتب بالرقم الأكاديمي')]"))).click()
        # except:
        #     self.driver.find_element_by_css_selector('div[href="#ul283"]').click()
        #     self.wait_5.until(EC.visibility_of_element_located(
        #         (By.XPATH, "// ul /li /a[contains(text(),'كشف طالبات المدرسة مرتب بالرقم الأكاديمي')]"))).click()
        #
        # app.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="تصدير"]'))).click()
        # app.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="PDF"]'))).click()

    ###############################################################################################################################
    #
    # def student_certificates(self, wb, school_id):
    #     self.driver.find_element_by_id("divMenuItem_321").find_element_by_xpath(".//a[@href='#']").click()
    #     sleep(2)
    #     self.driver.find_element_by_xpath(".//div[@href='#ul165']").click()
    #     sleep(2)
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, ".//a[contains(text(),'شهادات الطلبة')]"))).click()
    #     sleep(3)
    #     self.select_education_sys()
    #     sleep(3)
    #     self.read_students(wb, school_id)
    #
    # def read_students(self, wb, school_id):
    #     past_class_id = 0
    #     past_class_num = 0
    #     sheet = wb.sheet_by_name("Sheet2")
    #     for i in range(4, sheet.nrows):
    #         phone = sheet.cell_value(i, 1)
    #         class_num = sheet.cell_value(i, 2)
    #         class_id = sheet.cell_value(i, 3)
    #         name = sheet.cell_value(i, 4)
    #         stud_id = sheet.cell_value(i, 5)
    #
    #         class_info = self.Class_DB.select_class_info(str(class_id), class_num, school_id)
    #         class_name = class_info[1]
    #         section_name = class_info[2]
    #         if self.Class_DB.student_exist(stud_id, school_id):
    #             continue
    #         else:
    #             if class_id != past_class_id:
    #                 skip_class_select = 1
    #                 past_class_id = class_id
    #             else:
    #                 skip_class_select = 0
    #
    #             if class_num != past_class_num:
    #                 skip_chum_select = 1
    #                 past_class_num = class_num
    #             else:
    #                 skip_chum_select = 0
    #
    #             self.call_all_certificate_functions(class_name, section_name, class_num, name, stud_id, skip_class_select,
    #                                            skip_chum_select)
    #             self.Class_DB.add_student(stud_id, name, phone, class_info[0], class_num, school_id)
    #             print(' -Done')
    #
    # def call_all_certificate_functions(self, class_name, section_name, cnum, stu_name, stu_id, skip_class_select, skip_cnum_select):
    #     if skip_class_select == 1:
    #         self.select_class(class_name)
    #         self.wait_for_loader()
    #         self.select_section(section_name)
    #         self.wait_for_loader()
    #
    #     if skip_cnum_select == 1:
    #         self.select_class_num(cnum)
    #         self.wait_for_loader()
    #
    #     self.select_student_name(stu_name)
    #     self.wait_for_loader()
    #     self.certificate_show_btn()
    #     # wait_for_loader()
    #     # download_pdf_certicate()
    #     # wait_for_loader()
    #     # download_certicate()
    #     self.Class_DB.download_wait(self.path, 150)
    #     downloaded_filename3 = max([self.path + "\\" + f for f in os.listdir(self.path)], key=os.path.getctime)
    #     old_file1 = os.path.join(self.path, downloaded_filename3)
    #     new_file1 = os.path.join(self.path, str(stu_id) + ".pdf")
    #     os.rename(old_file1, new_file1)
    #
    # def download_certicate(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, ".//div[@id='ctl00_PlaceHolderMain_rvGetSTDSemNotification_ctl09_ctl04_ctl00_Menu']"))).click()
    #
    # def download_pdf_certicate(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, ".//a[@id='ctl00_PlaceHolderMain_rvGetSTDSemNotification_ctl09_ctl04_ctl00_ButtonLink']"))).click()
    #
    # def certificate_show_btn(self):
    #     self.wait.until(EC.presence_of_element_located((By.ID, "ctl00_PlaceHolderMain_ibtnView"))).click()
    #
    # def select_student_name(self, sname):
    #     wait = WebDriverWait(self.driver, 20)
    #     wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, ".//select[@name='ctl00$PlaceHolderMain$ddlStudents']/option[text()='" + sname + "']"))).click()
    #
    # def select_class_num(self, cnum):
    #     wait = WebDriverWait(self.driver, 20)
    #     wait.until(EC.element_to_be_clickable((By.XPATH, f".//select[@name='ctl00$PlaceHolderMain$oDistributionUC$ddlSection']/option[text()='{str(cnum)}']"))).click()
    #
    # def select_section(self, sname):
    #     wait = WebDriverWait(self.driver, 5)
    #     wait.until(EC.element_to_be_clickable((By.XPATH,
    #         f".//select[@name='ctl00$PlaceHolderMain$oDistributionUC$ddlSpecialty']/option[text()='{sname}']"))).click()
    #
    # def select_education_sys(self):
    #     wait = WebDriverWait(self.driver, 3)
    #     wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, ".//select[@name='ctl00$PlaceHolderMain$ddlStudySystem']/option[text()='منتظم']"))).click()
    #
    # def wait_for_loader(self):
    #     LOADING_ELEMENT_XPATH = ".//div[@id='ctl00_divLoadingFlash']"
    #     try:
    #         # wait for loading element to appear
    #         # - required to prevent prematurely checking if element
    #         #   has disappeared, before it has had a chance to appear
    #         WebDriverWait(self.driver, SHORT_TIMEOUT
    #                       ).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    #
    #         # then wait for the element to disappear
    #         WebDriverWait(self.driver, LONG_TIMEOUT
    #                       ).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    #
    #     except TimeoutException:
    #         print('pass 1')
    #         # if timeout exception was raised - it may be safe to
    #         # assume loading has finished, however this may not
    #         # always be the case, use with caution, otherwise handle
    #         # appropriately.
    #         pass
    #
    # def select_class(self, cname):
    #     wait = WebDriverWait(self.driver, 5)
    #     wait.until(EC.element_to_be_clickable((By.XPATH,
    #         f".//select[@name='ctl00$PlaceHolderMain$oDistributionUC$ddlClass']/option[text()='{cname}']"))).click()


if __name__ == '__main__':
    if username and password and user_id:
        app = Main()
        app.login()
        app.absence_alert()
        # app.Export()
        # app.high()
    else:
        print('- Please Enter Username and Password and User Id')
