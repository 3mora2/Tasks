from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def main(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(4)
    driver.get(url)
    sleep(3)
    Links = [element.get_attribute('href') for element in
             driver.find_elements_by_css_selector('div.Cover-overlay-28e > a')]

    for i, link in enumerate(Links):
        print(f'{i + 1} - {link}')
        driver.get(link)
        sleep(2)
        # driver.find_element_by_css_selector('div.Project-appreciate-2vE').click()
        try:
            driver.find_element_by_css_selector('div.e2e-Appreciate-appreciate-button.Project-appreciate-2vE').click()
            print('Appreciated')
        except:
            print("Can't Appreciate")

    driver.quit()


main(url='https://www.behance.net/omar2darwish')
