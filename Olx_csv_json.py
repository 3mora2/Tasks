#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import json
import pandas as pd


class Main_App:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.Login()

    def Login(self):
        self.driver.get('https://www.olx.com.eg/account/')
        WebDriverWait(self.driver, 10).until(
            (ec.visibility_of_element_located((By.CSS_SELECTOR, '#userEmail')))).send_keys(phone)
        sleep(1)
        WebDriverWait(self.driver, 10).until(
            (ec.visibility_of_element_located((By.CSS_SELECTOR, '#userPass')))).send_keys(password)
        sleep(1)
        WebDriverWait(self.driver, 10).until(
            (ec.visibility_of_element_located((By.CSS_SELECTOR, '#se_userLogin')))).click()
        sleep(3)

    def Open_URL(self):
        self.driver.get('https://www.olx.com.eg/properties/')
        sleep(4)
        Current_Page = 1
        Link = set()
        while True:
            print(f'- Current Page : {Current_Page}')
            for ele in self.driver.find_elements_by_css_selector('div.ads__item > div:nth-child(2) > a:nth-child(1)'):
                Link.add(ele.get_attribute('href'))
            print(len(Link))
            if Current_Page >= Number_page:
                print("- Stop....")
                break
            try:
                self.driver.find_element_by_css_selector('span.item a.pageNextPrev').click()
                print('- Next Page....')
                sleep(2)
                Current_Page += 1
            except:
                break

        self.Data(Link)

    def Data(self, Link):
        List_CSV = []
        List_Json = []
        for con, url in enumerate(Link):
            try:
                self.driver.get(url)
                sleep(2)
                name = WebDriverWait(self.driver, 10).until((ec.visibility_of_element_located((By.CSS_SELECTOR, 'h1.brkword')))).text
                # name = self.driver.find_element_by_css_selector('h1.brkword').text
                try:
                    self.driver.find_element_by_css_selector('div.contactbox-indent').click()
                    number = True
                except:
                    number = ''
                price = self.driver.find_element_by_css_selector('#offeractions > div > div.pricelabel > strong').text.replace('ج.م', '').replace('EGP', '').replace(',', '').strip()
                try:
                    city = self.driver.find_element_by_css_selector('span.show-map-link > strong').text.split('،')
                except:
                    city = ['', '']
                sleep(3)
                try:
                    user = self.driver.find_element_by_css_selector('.user-box__info__name').text
                except:
                    user = None
                # try:
                #     Amenities = self.driver.find_element_by_xpath(
                #         '//tr[th[contains(text(),"الكماليات")]|th[contains(text(),"Amenities")]]/td[contains(@class,"value")]/strong').text
                # except:
                #     Amenities = ''
                try:
                    Bedrooms = self.driver.find_element_by_xpath(
                        '//tr[th[contains(text(), "غرف نوم")]|th[contains(text(), "Bedrooms")]]/td[contains(@class,"value")]/strong').text
                except:
                    Bedrooms = ''
                try:
                    Bathrooms = self.driver.find_element_by_xpath(
                        '//tr[th[contains(text(), "الحمامات")]|th[contains(text(), "Bathrooms")]]/td[contains(@class,"value")]/strong').text
                except:
                    Bathrooms = ''
                try:
                    Area = self.driver.find_element_by_xpath(
                        '//tr[th[contains(text(), "المساحة")]|th[contains(text(), "Area")]]/td[contains(@class,"value")]/strong').text
                except:
                    Area = ''
                # Furnished = self.driver.find_element_by_xpath(
                #     '//tr[th[contains(text(), "مفروش")]|th[contains(text(), "Furnished")]]/td[contains(@class,"value")]/strong').text
                # Ad_Type = self.driver.find_element_by_xpath(
                #     '//tr[th[contains(text(), "نوع الإعلان")]|th[contains(text(), "Ad Type")]]/td[contains(@class,"value")]/strong').text
                try:
                    Type = self.driver.find_element_by_xpath(
                        '//tr[th[contains(text(), "النوع")]|th[text()="Type"]]/td[contains(@class,"value")]/strong').text
                except:
                    Type = ''
                # Payment_Option = self.driver.find_element_by_xpath(
                #     '//tr[th[contains(text(), "طريقة الدفع")]|th[contains(text(), "Payment Option")]]/td[contains(@class,"value")]/strong').text
                # desk = self.driver.find_element_by_css_selector('#textContent').text
                try:
                    self.driver.find_element_by_xpath(
                        '//tr[th[contains(text(), "كمبوند")]|th[contains(text(), "Compound")]]/td[contains(@class,"value")]/strong')
                    Compound = 'yes'
                except:
                    Compound = 'no'

                if number is not '':
                    try:
                        while True:
                            number = self.driver.find_element_by_css_selector('div.contactbox-indent').text.replace(' ', '')
                            if 'x' not in number:
                                break
                    except:
                        number = ''
                print(con, ' - ', number)
                List_Json.append(self.Data_Json(bathrooms=Bathrooms, city=city[0], gov=city[1], phone_number=number, area=Area,
                               Compound=Compound, Bedrooms=Bedrooms, price=price, Type=Type))
                List_CSV.append([user, number])
            except Exception as e:
                print(e)

        self.Save_CSV(List_CSV)
        self.Save_AS_Json(List_Json)

    @staticmethod
    def Save_CSV(data):
        city = pd.DataFrame(data, columns=['Name', 'Phone Number'])
        city.to_csv('data_file.csv', encoding='utf-8', index=False)
        print(city.to_json())

    @staticmethod
    def Data_Json(bathrooms, city, gov, phone_number, area, Compound, Bedrooms, price, Type, email="",
                  garage="private", finished="full", category="residential", property_location='', price_m='0',
                  rent_sale="sale", view="garden"):
        return {
            'bathrooms': str(bathrooms),
            'category': str(category),
            'city': str(city),
            'finished': str(finished),
            'garage': str(garage),
            'gov': str(gov),
            'property location': str(property_location),
            'email': str(email),
            'phone number': str(phone_number),
            'gross_space': str(area),
            'inside_comp': str(Compound),
            'price_m': str(price_m),
            'rent_sale': str(rent_sale),
            'rooms': str(Bedrooms),
            'total_price': str(price),
            'type': str(Type),
            'view': str(view)
                }

    def Save_AS_Json(self, data):
        self.data = data
        with open("data_file.json", mode="w", encoding="utf8") as write_file:
            json.dump(data, write_file)


if __name__ == '__main__':
    phone = '01028946519'  # input('- Enter your phone number : ')
    password = 'ammar2016'  # input('- Enter password : ')
    Number_page = 1  # int(input('- Enter Number Pages : '))
    app = Main_App()
    app.Open_URL()

'''
{
bathrooms: "1"
category: "residential"
city: "heliopolis"
finished: "full"
garage: "private"
gov: "cairo"
property location : ""
email:""
phone number:""
gross_space: "100"
inside_comp: "yes"
price_m: "0"
rent_sale: "sale"
rooms: "2"
total_price: "2000000"
type: "Apartment"
view: "garden"
}
'''
