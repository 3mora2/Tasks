data=str(input('>>>')).split(':')
from selenium import webdriver
from  time import sleep
import os,requests,warnings
warnings.filterwarnings("ignore")

path='PDF'
if not os.path.exists(path):
    os.makedirs(path)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://elecciones1.registraduria.gov.co/e14_pre2_2018/")
sleep(2)
p=1
pdf_links=[]
e=[]
select_main=driver.find_element_by_id('select_dep')
try:
    category_main=[option.text for option in select_main.find_elements_by_tag_name('option')]
except Exception as ee:
    print(ee)
    exit()
##############################################################################################
if len(data)==1:
    dataa=data[0].split('-')
    if len(dataa)==1:
        Category_Main_s=int(dataa[0])-1 if dataa[0].isnumeric() and int(dataa[0])>0 else 0   
        Category_Main_e=len(category_main)        
    elif len(dataa)==2:
        Category_Main_s=int(dataa[0])-1 if dataa[0].isnumeric() and int(dataa[0])>0 else 0
        Category_Main_e=int(dataa[1])-1 if dataa[1].isnumeric() and int(dataa[1])>0  and int(dataa[1])-1 < len(category_main) else len(category_main)
    else:
        Category_Main_s=0
        Category_Main_e=len(category_main)
    Category_1=0
elif len(data)==2:
    dataa=data[0].split('-')
    if len(dataa)==1:
        Category_Main_s=int(dataa[0])-1 if dataa[0].isnumeric() and int(dataa[0])>0 else 0   
        Category_Main_e=len(category_main)        
    elif len(dataa)==2:
        Category_Main_s=int(dataa[0])-1 if dataa[0].isnumeric() and int(dataa[0])>0 else 0
        Category_Main_e=int(dataa[1])-1 if dataa[1].isnumeric() and int(dataa[1])>0  and int(dataa[1])-1 < len(category_main) else len(category_main)
    else:
        Category_Main_s=0
        Category_Main_e=len(category_main)
    Category_1=int(data[1])-1 if data[1].isnumeric() and int(data[1])>0 else None

################################################################################################
for cate_main in category_main[Category_Main_s:Category_Main_e]:
    select_main.send_keys(cate_main)
    sleep(3)    
    select_1=driver.find_element_by_id('mpio')
    category_1=[]
    for option1 in select_1.find_elements_by_tag_name('option'):category_1.append(option1.text)
    if Category_1!=0:
        Category_1=int(data[1])-1 if data[1].isnumeric() and int(data[1])>0 and int(data[1])-1 < len(category_1) else len(category_1) 
    for cate_1 in category_1[Category_1:]:
        Category_1=0
        select_1.send_keys(cate_1)
        sleep(3)
        select_2=driver.find_element_by_id('zona')
        category_2=[]
        for option2 in select_2.find_elements_by_tag_name('option'):
            if option2.get_attribute('value')!='-1':
                category_2.append(option2.text)
        for cate_2 in category_2:
            
            select_2.send_keys(cate_2)
            sleep(4)
            select_3=driver.find_element_by_id('pto')
            category_3=[]
            
            for option3 in select_3.find_elements_by_tag_name('option'):
                category_3.append(option3.text)
            for cate_3 in category_3:
                select_3.send_keys(cate_3)
                driver.find_element_by_class_name('btn-cons').click()
                sleep(4)
                pdf=driver.find_element_by_xpath('//*[@id="datatable-example"]/tbody').find_elements_by_xpath('//tr/td/a')
                for i in pdf:
                    if '.pdf' in i.get_attribute('href'):
                        pdf_links.append(i.get_attribute('href'))
                        '''try:
                            name=f'{cate_main}_{cate_1}_{cate_2}_{cate_3}_{i.text}'
                            r = requests.get(i.get_attribute('href'), stream=True)
                            with open(path+'\\'+f'{name}.pdf','wb') as f:
                                f.write(r.content)
        
                        except Exception as ee:
                            print(ee)
                        p+=1'''
                        
                print(f'{category_main.index(cate_main)+1}-{len(category_main)} : {category_1.index(cate_1)+1}-{len(category_1)} : {category_2.index(cate_2)+1}-{len(category_2)}: {category_3.index(cate_3)+1}-{len(category_3)} :pdf_links : ',len(pdf_links))
                
driver.quit()
#0-34 : 0-125 : 6-35: 1-5 :pdf_links :  712

