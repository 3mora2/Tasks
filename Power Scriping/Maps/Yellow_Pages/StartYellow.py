from time import sleep
from PySide2.QtCore import QThread, Signal
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PySide2.QtWidgets import QTableWidgetItem
from selenium.webdriver.chrome.webdriver import WebDriver


class StartYellow(QThread):
    driver: WebDriver
    final = Signal(object)
    error = Signal()
    error_driver = Signal()
    pause = False
    stop = False
    data = dict()

    @staticmethod
    def safe_find_element_by(driver, by, element):
        try:
            return driver.find_element(by, element)
        except NoSuchElementException:
            return None

    def run(self):
        if self.check():
            self.extract()
        else:
            self.error_driver.emit()
        self.final.emit(self.data)

    def extract(self):
        num = 2
        while True:
            for element in self.driver.find_elements_by_css_selector('.searchResultsDiv'):
                while self.pause:
                    if self.stop:
                        break
                    sleep(1)

                if self.stop:
                    break

                companyName = self.safe_find_element_by(element, By.CSS_SELECTOR, '.companyName')
                if companyName:
                    companyName = companyName.text
                companyURL = self.safe_find_element_by(element, By.CSS_SELECTOR, '.companyName')
                if companyURL:
                    companyURL = companyURL.get_attribute('href')

                business_description = self.safe_find_element_by(element, By.CSS_SELECTOR, '.business-description')
                if business_description:
                    business_description = business_description.text

                img = self.safe_find_element_by(element, By.CSS_SELECTOR, 'a>img')
                if img:
                    img = img.get_attribute('src')

                company_address = self.safe_find_element_by(element, By.CSS_SELECTOR, '.company_address')
                if company_address:
                    company_address = company_address.text

                show_branches = self.safe_find_element_by(element, By.CSS_SELECTOR, '.show_branches_SRP')
                if show_branches:
                    show_branches = show_branches.get_attribute('href')

                category = self.safe_find_element_by(element, By.CSS_SELECTOR, '.category')
                if category:
                    category = category.text
                otherCategories = self.safe_find_element_by(element, By.CSS_SELECTOR, '.otherCategories')
                if otherCategories:
                    category += ',' + ','.join(otherCategories.get_attribute('data-content').split('<br>'))

                keywords = [el.text for el in element.find_elements_by_css_selector('.search-keywords .two-words span')]
                otherKeywords = self.safe_find_element_by(element, By.CSS_SELECTOR, '.otherKeywords')
                if otherKeywords:
                    keywords += otherKeywords.get_attribute('data-content').split('<br>')
                keywords = ', '.join(keywords)

                aboutUs = self.safe_find_element_by(element, By.CSS_SELECTOR, '.aboutUs')
                if aboutUs:
                    aboutUs = aboutUs.text

                website = self.safe_find_element_by(element, By.CSS_SELECTOR, '.website > a')
                if website:
                    website = website.get_attribute('href')

                show_directions = self.safe_find_element_by(element, By.CSS_SELECTOR, '#show_directions.latlng-mob>a')
                if show_directions:
                    show_directions = show_directions.get_attribute('href')

                whatsapp = self.safe_find_element_by(element, By.CSS_SELECTOR, '.whatsapp > a')
                if whatsapp:
                    whatsapp = whatsapp.get_attribute('href')

                mob = self.safe_find_element_by(element, By.CSS_SELECTOR, '.search-call-mob')
                if mob:
                    mob = mob.get_attribute('href').split(":")[-1].strip()

                show_review = self.safe_find_element_by(element, By.CSS_SELECTOR, '.show-review')
                if show_review:
                    show_review = show_review.text

                self.data[num] = {
                    'img': img,
                    'show_review': show_review,
                    'companyName': companyName,
                    'mob': mob,
                    'whatsapp': whatsapp,
                    'business_description': business_description,
                    'category': category,
                    'show_directions': show_directions,
                    'keywords': keywords,
                    'company_address': company_address,
                    'website': website,
                    'show_branches': show_branches,
                    'aboutUs': aboutUs,
                    'companyURL': companyURL,
                }
                print(num - 1)

                r = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(r)
                self.tableWidget_3.setItem(r, 0, QTableWidgetItem(str(companyName)))
                self.tableWidget_3.setItem(r, 1, QTableWidgetItem(str(mob if mob else '')))
                self.tableWidget_3.setItem(r, 2, QTableWidgetItem(str(category if category else '')))
                self.tableWidget_3.setItem(r, 3, QTableWidgetItem(str(show_review if show_review else '')))
                self.tableWidget_3.setItem(r, 4, QTableWidgetItem(str(company_address if company_address else '')))
                self.tableWidget_3.setItem(r, 5, QTableWidgetItem(str(show_directions if show_directions else '')))
                num += 1

            while self.pause:
                if self.stop:
                    break
                sleep(1)

            if self.stop:
                break

            try:
                self.driver.find_element_by_css_selector('li + .waves-effect > a').click()
                sleep(4)
            except:
                break
        print('- Done....', end='\r')
