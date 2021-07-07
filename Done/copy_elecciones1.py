from selenium import webdriver
from  time import sleep
import os,requests,warnings
warnings.filterwarnings("ignore")
#url_ele.xlsx

################################

################################

f_f=[]
path='PDF'
if not os.path.exists(path):
    os.makedirs(path)
    Categorys=[1,0,0,0,0]
 
elif os.path.exists(path):
    
    if len(os.listdir('PDF'))>0:
        try:
            c=[]
            for file in os.listdir('PDF'):c.append(int(file.split('.pdf')[0].split('_')[0]))
            c.sort()
            e_f=[file.split('.pdf')[0].split('_') for file in os.listdir('PDF') if file.split('.pdf')[0].split('_')[0]== str(c[-1])][0]

            f_f=[file.split('.pdf')[0].split('_') for file in os.listdir('PDF')  if file.split('.pdf')[0].split('_')[1]==e_f[1] and file.split('.pdf')[0].split('_')[2]==e_f[2] and file.split('.pdf')[0].split('_')[3]==e_f[3] and file.split('.pdf')[0].split('_')[4]==e_f[4]]

            
            print(len(f_f))
            if len(f_f)!=0:
                Categorys=f_f[0]
                
            else:Categorys=[1,0,0,0,0]
        except:Categorys=[1,0,0,0,0]
        
        
        
    else:
        p=1
        Categorys=[1,0,0,0,0]

p=int(Categorys[0])+len(f_f) if int(Categorys[0]) != 1 else int(Categorys[0])      
c_m=Categorys[1]
c_1=Categorys[2]
c_2=Categorys[3]
c_3=Categorys[4]

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://elecciones1.registraduria.gov.co/e14_pre2_2018/")
sleep(2)
pdf_links=[]
e=[]
try:
    select_main=driver.find_element_by_id('select_dep')
    try:
        category_main=[option.text for option in select_main.find_elements_by_tag_name('option')]
        
    except Exception as ee:
        print(ee)
        exit()
        
    n1=n2=n3=None
    n_m=category_main.index(c_m) if c_m !=0 else 0
    ################################################################################################
    #Section # 1-34 : 1-125 : 17-35 : 4-4 : Downloaded_PDF = 1915
    for cate_main in category_main[:]:
        select_main.send_keys(cate_main)
        sleep(3)    
        select_1=driver.find_element_by_id('mpio')
        category_1=[]
        for option1 in select_1.find_elements_by_tag_name('option'):category_1.append(option1.text)
        n1=category_1.index(c_1) if c_1 !=0 and n1==None else 0
        
        for cate_1 in category_1[n1:]:
            c_1=0
            select_1.send_keys(cate_1)
            sleep(3)
            select_2=driver.find_element_by_id('zona')
            category_2=[]
            for option2 in select_2.find_elements_by_tag_name('option'):
                if option2.get_attribute('value')!='-1':
                    category_2.append(option2.text)
            n2=category_2.index(c_2) if c_2 !=0 and n2==None else 0
            for cate_2 in category_2[n2:]:
                c_2=0
                select_2.send_keys(cate_2)
                sleep(4)
                select_3=driver.find_element_by_id('pto')
                category_3=[]
                
                for option3 in select_3.find_elements_by_tag_name('option'):
                    category_3.append(option3.text)
                n3=category_3.index(c_3) if c_3 !=0 and n3==None else 0
                
                for cate_3 in category_3[n3:]:
                    c_3=0
                    select_3.send_keys(cate_3)
                    driver.find_element_by_class_name('btn-cons').click()
                    sleep(4)
                    pdf=driver.find_element_by_xpath('//*[@id="datatable-example"]/tbody').find_elements_by_xpath('//tr/td/a')
                    for i in pdf:
                        if '.pdf' in i.get_attribute('href'):
                            pdf_links.append(i.get_attribute('href'))
                            if pdf_links.index(i.get_attribute('href'))<len(f_f) and p==int(Categorys[0])+len(f_f) :
                                continue
                            name=f'{p}_{cate_main}_{cate_1}_{cate_2}_{cate_3}_{i.text}'
                            try:
                                sleep(.5)
                                r = requests.get(i.get_attribute('href'), stream=True)
                                with open(path+'\\'+f'{name}.pdf','wb') as f:
                                    f.write(r.content)
                            except Exception as ee:
                                print(ee)
                            p+=1
                            print(f'Section # {category_main.index(cate_main)+1}-{len(category_main)} : {category_1.index(cate_1)+1}-{len(category_1)} : {category_2.index(cate_2)+1}-{len(category_2)} : {category_3.index(cate_3)+1}-{len(category_3)} : Downloaded_PDF = {len(pdf_links)}')
                        
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()
#0-34 : 0-125 : 6-35: 1-5 :pdf_links :  712

