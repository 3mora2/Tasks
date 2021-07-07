# import subprocess
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import warnings
warnings.filterwarnings("ignore")
# subprocess.Popen('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222')
# chrome_options = Options()
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(chrome_options=chrome_options)
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Firefox()
med = input('name module : ')  # 'Respiratory'
num = input('number module : ')  # '0710214'
name = input('your name : ')  # 'عمار القطب العوضي خلف'
mail = input('your email : ')  # 'ammar.k6@domazhermedicine.edu.eg'
l = ['الفسيولوجى', 'التشريح', 'الهستولوجى', 'البيوكيمسترى', 'الفارما', 'البارا', 'البكتريا', 'طب المجتمع', 'الباثولوجى', 'الباطنه']  # 'الطب الشرعى', 'طب المجتمع', 'الرمد', 'الانف والاذن والحنجرة', 'النساء والتوليد', 'الاطفال', 'الباطنه', 'الجراحة', 'الانجليزى', 'المواد الشرعية']
while True:
    if len(l) == 0:
        break
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeXLSUsCbyprIzqSiHy59xsyPT9m7BE8PrrvW5k__x7IFEEbA/viewform?usp=sf_link")
    sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                                (By.CSS_SELECTOR, 'div.quantumWizTextinputPaperinputInputArea > input'))).send_keys(mail)
    sleep(2)
    driver.find_element_by_css_selector('div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span > span').click()
    sleep(2)
    driver.find_element_by_css_selector('div:nth-child(3)  div.quantumWizTextinputPaperinputInputArea > input').send_keys(name)
    driver.find_element_by_css_selector('#i16 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i38 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(6) div.quantumWizTextinputPaperinputInputArea > input').send_keys(med)
    driver.find_element_by_css_selector('div:nth-child(7) div.quantumWizTextinputPaperinputInputArea > input').send_keys(num)
    text = ' '
    driver.find_element_by_css_selector('div:nth-child(8) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div').click()
    sleep(2)
    for ele in driver.find_elements_by_css_selector(
            'div:nth-child(8) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div.exportSelectPopup.quantumWizMenuPaperselectPopup.appsMaterialWizMenuPaperselectPopup > div'):
        if ele.text.strip() in l:
            if ele.text == '':
                continue
            text = ele.text.strip()
            ele.click()
            del l[l.index(ele.text)]
            break
    driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input').send_keys(text)

    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    # driver.find_element_by_css_selector(
    #     'div.isUndragged .appsMaterialWizButtonPaperbuttonContent.exportButtonContent').click()
    #######################################################################################
    print(1)
    sleep(3)
    driver.find_element_by_css_selector('div:nth-child(3)  label:nth-child(4)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(4)  label:nth-child(5)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(5)  label:nth-child(6)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(6)  label:nth-child(4)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(7)  label:nth-child(5)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(8)  label:nth-child(6)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('div:nth-child(9)  label:nth-child(5)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector(
        'div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div > span > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('div:nth-child(10)  label:nth-child(5)  div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    ################################
    print(2)
    sleep(3)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    ###################################
    print(3)
    sleep(3)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i107 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i110 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i129 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i148 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    #####################################
    print(4)
    sleep(3)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i107 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i110 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i129 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i148 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i167 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i186 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span > span').click()
    ########################################
    print(5)
    sleep(3)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    #########################################
    print(6)
    sleep(3)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i107 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i110 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i129 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i148 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i167 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i186 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    ####################################
    sleep(3)
    print(7)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i107 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i110 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i129 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    ############################
    sleep(3)
    print(8)
    driver.find_element_by_css_selector('#i15 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i34 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i53 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i72 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i91 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i107 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i110 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    driver.find_element_by_css_selector('#i129 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div').click()
    # driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2.isUndragged > span').click()
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    ###################
    sleep(3)
    driver.find_elements_by_css_selector('.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')[-1].click()
    #driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonFilled.freebirdFormviewerViewNavigationSubmitButton.freebirdThemedFilledButtonM2.isUndragged > span').click()





'''
Heamatopiotic 0710103
MSK 0710212
Respiratory 0710214
'''