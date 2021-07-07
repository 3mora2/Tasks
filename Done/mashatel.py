from openpyxl import Workbook
path = 'GARDEN FURNITURE .xlsx'
sheet = Workbook()
sh = sheet.active
urll = ['https://mashatel.me/product/13442', 'https://mashatel.me/product/7636', 'https://mashatel.me/product/7878', 'https://mashatel.me/product/7942', 'https://mashatel.me/product/1532', 'https://mashatel.me/product/8365', 'https://mashatel.me/product/8364', 'https://mashatel.me/product/8074', 'https://mashatel.me/product/8369', 'https://mashatel.me/product/8373', 'https://mashatel.me/product/8366', 'https://mashatel.me/product/8368', 'https://mashatel.me/product/8370', 'https://mashatel.me/product/1531', 'https://mashatel.me/product/1533', 'https://mashatel.me/product/1534', 'https://mashatel.me/product/8376', 'https://mashatel.me/product/8374', 'https://mashatel.me/product/8375']
num = 1
for u in urll:
    sh[f"B{num}"] = u
    num += 1
sheet.save(path)
'''
from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
from requests_html import HTMLSession
s=HTMLSession()
sheet = load_workbook(path)
from io import BytesIO
from openpyxl.drawing.image import Image

# product_url = []
options = EdgeOptions()
options.use_chromium = True
options.add_argument("disable-gpu")
options.add_argument("--user-data-dir=Edge-data")
driver = Edge(options=options)


driver.get('https://mashatel.me/categories')
link_cage = []
for element in driver.find_elements_by_css_selector('div.col-md-4.categories-box > a'):
    link_cage.append(element.get_attribute('href'),element.text)'''
'''
('https://mashatel.me/category/156', 'DISINFECTANT')

urll = ['https://mashatel.me/product/12004', 'https://mashatel.me/product/12007', 'https://mashatel.me/product/12010', 'https://mashatel.me/product/12006', 'https://mashatel.me/product/12009', 'https://mashatel.me/product/12011', 'https://mashatel.me/product/12099', 'https://mashatel.me/product/12098', 'https://mashatel.me/product/12003', 'https://mashatel.me/product/12005', 'https://mashatel.me/product/12008', 'https://mashatel.me/product/12151', 'https://mashatel.me/product/12143']
num= 1
sh[f'B{num}']='name'
sh[f'C{num}']='price'
sh[f'D{num}']='state'
sh[f'E{num}']='seller'
sh[f'F{num}']='Colorar'
sh[f'G{num}']='Volumear'
sh[f'H{num}']='Varietyar'
#######################
sh[f'J{num}']='name'
sh[f'K{num}']='price'
sh[f'L{num}']='state'
sh[f'M{num}']='seller'
sh[f'N{num}']='Color'
sh[f'O{num}']='Volume'
sh[f'P{num}']='Variety'
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            Color = [elem.text.replace('Color :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][0]
        except:
            Color = None
        try:
            Variety = [elem.text.replace('Variety :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Volume = [elem.text.replace('Volume (ml) :','').replace('Volume (Litre) :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Volume (ml) :' in elem.text or 'Volume (Litre) :' in elem.text][0]
        except:
            Volume = None
    #################################################
        
        try:
            Colorar = [elem.text.replace('اللون :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'اللون :' in elem.text][0]
        except:
            Colorar = None
        try:
            Volumear = [elem.text.replace('الحجم(مل) :','').replace('الحجم (لتر) :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'الحجم(مل) :' in elem.text or 'الحجم (لتر) :' in elem.text][0]
        except:
            Volumear = None
        try:
            Varietyar = [elem.text.replace('تنوع :','').strip() for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'تنوع :' in elem.text][0]
        except:
            Varietyar = None

        sh[f'B{num}']=name
        sh[f'C{num}']=price
        sh[f'D{num}']=state
        sh[f'E{num}']=seller
        sh[f'F{num}']=Colorar
        sh[f'G{num}']=Volumear
        sh[f'H{num}']=Varietyar
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'I{num}')
        
        sh[f'J{num}'] = name
        sh[f'K{num}'] = price
        sh[f'L{num}'] = state
        sh[f'M{num}'] = seller
        sh[f'N{num}'] = Color
        sh[f'O{num}'] = Volume
        sh[f'P{num}'] = Variety
        
        num +=1
    except Exception as e:
        print(e)


sheet.save('DISINFECTANT.xlsx')
'''
'''
('https://mashatel.me/category/161', 'PREMIUM COLLECTION')

urll=['https://mashatel.me/product/14257', 'https://mashatel.me/product/14411', 'https://mashatel.me/product/14262', 'https://mashatel.me/product/14261', 'https://mashatel.me/product/14259', 'https://mashatel.me/product/14258', 'https://mashatel.me/product/14256', 'https://mashatel.me/product/14255', 'https://mashatel.me/product/14254', 'https://mashatel.me/product/14054', 'https://mashatel.me/product/12115', 'https://mashatel.me/product/13500', 'https://mashatel.me/product/13476', 'https://mashatel.me/product/12738', 'https://mashatel.me/product/12861', 'https://mashatel.me/product/12859', 'https://mashatel.me/product/12856', 'https://mashatel.me/product/12727', 'https://mashatel.me/product/12725', 'https://mashatel.me/product/12715', 'https://mashatel.me/product/12713', 'https://mashatel.me/product/12702', 'https://mashatel.me/product/12700', 'https://mashatel.me/product/12696', 'https://mashatel.me/product/11635', 'https://mashatel.me/product/12376', 'https://mashatel.me/product/12614', 'https://mashatel.me/product/12612', 'https://mashatel.me/product/12611', 'https://mashatel.me/product/12489', 'https://mashatel.me/product/12487', 'https://mashatel.me/product/12436', 'https://mashatel.me/product/11986', 'https://mashatel.me/product/12000', 'https://mashatel.me/product/12233', 'https://mashatel.me/product/11972', 'https://mashatel.me/product/11982', 'https://mashatel.me/product/11409', 'https://mashatel.me/product/11412', 'https://mashatel.me/product/11415', 'https://mashatel.me/product/11647', 'https://mashatel.me/product/11265', 'https://mashatel.me/product/11335', 'https://mashatel.me/product/11407', 'https://mashatel.me/product/11907', 'https://mashatel.me/product/11981', 'https://mashatel.me/product/12013', 'https://mashatel.me/product/12169', 'https://mashatel.me/product/12114', 'https://mashatel.me/product/12232', 'https://mashatel.me/product/12375', 'https://mashatel.me/product/11264', 'https://mashatel.me/product/11337', 'https://mashatel.me/product/11398', 'https://mashatel.me/product/11400', 'https://mashatel.me/product/11408', 'https://mashatel.me/product/11636', 'https://mashatel.me/product/11903', 'https://mashatel.me/product/11977', 'https://mashatel.me/product/11978', 'https://mashatel.me/product/11979', 'https://mashatel.me/product/12065', 'https://mashatel.me/product/12066', 'https://mashatel.me/product/12116']

num= 1
sh[f'B{num}'] = 'name'
sh[f'C{num}'] = 'price'
sh[f'D{num}'] = 'state'
sh[f'E{num}'] = 'seller'
sh[f'F{num}'] = 'Species'
sh[f'G{num}'] ='Variety'
sh[f'H{num}'] = 'Grow'
sh[f'J{num}'] = 'Sunlight'
sh[f'H{num}'] = 'Common'
sh[f'I{num}'] = 'Water'
sh[f'J{num}'] = 'Soil'
sh[f'K{num}'] = 'Fertilizers'
sh[f'L{num}'] = 'Genus'
sh[f'M{num}'] = 'Height'
sh[f'N{num}'] = 'Size'
sh[f'O{num}'] = 'des'
sh[f'Q{num}'] = 'name'
sh[f'R{num}'] = 'price'
sh[f'S{num}'] = 'state'
sh[f'T{num}'] = 'seller'
sh[f'U{num}'] = 'Species'
sh[f'V{num}'] ='Variety'
sh[f'W{num}'] = 'Grow'
sh[f'X{num}'] = 'Sunlight'
sh[f'Y{num}'] = 'Common'
sh[f'Z{num}'] = 'Water'
sh[f'AA{num}'] = 'Soil'
sh[f'AB{num}'] = 'Fertilizers'
sh[f'AC{num}'] = 'Genus'
sh[f'AD{num}'] = 'Height'
sh[f'AE{num}'] = 'Size'
sh[f'AF{num}'] = 'des'
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        try:
            Species = [elem.text.replace('Species :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Species :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('Difficulty to Grow :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Difficulty to Grow :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('Sunlight :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Sunlight :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('Common Names :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Common Names :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('Water :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Water :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('Soil :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Soil :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('Fertilizers :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Fertilizers :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('Genus :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Genus :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('Plant Height (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Plant Height (cm) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('Pot Size (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Size (cm) :' in elem.text][0]
        except:
            Size = None
        try:
            Species = [elem.text.replace('انواع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'انواع :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('مستوى صعوبة النمو ::', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى صعوبة النمو :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('ضوء الشمس :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ضوء الشمس :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('الأسماء الشائعة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الأسماء الشائعة :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('سقي النبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'سقي النبات :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('التربة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'التربة :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('السماد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'السماد :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('النوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'النوع :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('ارتفاع النبات (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ارتفاع النبات (سم) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('حجم الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'حجم الاناء (سم) :' in elem.text][0]
        except:Size=None
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Species
        sh[f'G{num}'] = Variety
        sh[f'H{num}'] = Grow
        sh[f'J{num}'] = Sunlight
        sh[f'H{num}'] = Common
        sh[f'I{num}'] = Water
        sh[f'J{num}'] = Soil
        sh[f'K{num}'] = Fertilizers
        sh[f'L{num}'] = Genus
        sh[f'M{num}'] = Height
        sh[f'N{num}'] = Size
        sh[f'O{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'P{num}')
        sh[f'Q{num}'] = name
        sh[f'R{num}'] = price
        sh[f'S{num}'] = state
        sh[f'T{num}'] = seller
        sh[f'U{num}'] = Species
        sh[f'V{num}'] = Variety
        sh[f'W{num}'] = Grow
        sh[f'X{num}'] = Sunlight
        sh[f'Y{num}'] = Common
        sh[f'Z{num}'] = Water
        sh[f'AA{num}'] = Soil
        sh[f'AB{num}'] = Fertilizers
        sh[f'AC{num}'] = Genus
        sh[f'AD{num}'] = Height
        sh[f'AE{num}'] = Size
        sh[f'AF{num}'] = des
        num += 1
    except:
        pass
sheet.save('PREMIUM COLLECTION.xlsx')
'''
'''
('https://mashatel.me/category/26', 'INDOOR PLANTS')

urll = ['https://mashatel.me/product/12467', 'https://mashatel.me/product/12511', 'https://mashatel.me/product/12500', 'https://mashatel.me/product/7172', 'https://mashatel.me/product/14328', 'https://mashatel.me/product/12442', 'https://mashatel.me/product/12573', 'https://mashatel.me/product/12575', 'https://mashatel.me/product/12444', 'https://mashatel.me/product/12450', 'https://mashatel.me/product/12459', 'https://mashatel.me/product/13460', 'https://mashatel.me/product/13464', 'https://mashatel.me/product/13468', 'https://mashatel.me/product/13595', 'https://mashatel.me/product/13597', 'https://mashatel.me/product/13599', 'https://mashatel.me/product/13446', 'https://mashatel.me/product/465', 'https://mashatel.me/product/469', 'https://mashatel.me/product/560', 'https://mashatel.me/product/563', 'https://mashatel.me/product/595', 'https://mashatel.me/product/596', 'https://mashatel.me/product/761', 'https://mashatel.me/product/768', 'https://mashatel.me/product/2599', 'https://mashatel.me/product/2600', 'https://mashatel.me/product/7190', 'https://mashatel.me/product/255', 'https://mashatel.me/product/13265', 'https://mashatel.me/product/13527', 'https://mashatel.me/product/13653', 'https://mashatel.me/product/13900', 'https://mashatel.me/product/14213', 'https://mashatel.me/product/14260', 'https://mashatel.me/product/14283', 'https://mashatel.me/product/14298', 'https://mashatel.me/product/14339', 'https://mashatel.me/product/14377', 'https://mashatel.me/product/14392', 'https://mashatel.me/product/14413', 'https://mashatel.me/product/14412', 'https://mashatel.me/product/12468', 'https://mashatel.me/product/12471', 'https://mashatel.me/product/12474', 'https://mashatel.me/product/12473', 'https://mashatel.me/product/13182', 'https://mashatel.me/product/13462', 'https://mashatel.me/product/13523', 'https://mashatel.me/product/13604', 'https://mashatel.me/product/14371', 'https://mashatel.me/product/14364', 'https://mashatel.me/product/1686', 'https://mashatel.me/product/14308', 'https://mashatel.me/product/14325', 'https://mashatel.me/product/14190', 'https://mashatel.me/product/2928', 'https://mashatel.me/product/7926', 'https://mashatel.me/product/12228', 'https://mashatel.me/product/14107', 'https://mashatel.me/product/12646', 'https://mashatel.me/product/910', 'https://mashatel.me/product/12743', 'https://mashatel.me/product/14304', 'https://mashatel.me/product/8345', 'https://mashatel.me/product/14193', 'https://mashatel.me/product/1195', 'https://mashatel.me/product/1194', 'https://mashatel.me/product/14302', 'https://mashatel.me/product/13938', 'https://mashatel.me/product/14279', 'https://mashatel.me/product/12104', 'https://mashatel.me/product/13565', 'https://mashatel.me/product/13567', 'https://mashatel.me/product/8348', 'https://mashatel.me/product/2606', 'https://mashatel.me/product/14253', 'https://mashatel.me/product/12227', 'https://mashatel.me/product/12494', 'https://mashatel.me/product/13622', 'https://mashatel.me/product/8220', 'https://mashatel.me/product/6260', 'https://mashatel.me/product/2699', 'https://mashatel.me/product/8235', 'https://mashatel.me/product/1184', 'https://mashatel.me/product/13929', 'https://mashatel.me/product/13902', 'https://mashatel.me/product/12344', 'https://mashatel.me/product/12542', 'https://mashatel.me/product/2592', 'https://mashatel.me/product/14183', 'https://mashatel.me/product/14181', 'https://mashatel.me/product/13694', 'https://mashatel.me/product/14173', 'https://mashatel.me/product/14129', 'https://mashatel.me/product/8410', 'https://mashatel.me/product/13569', 'https://mashatel.me/product/12316', 'https://mashatel.me/product/12367', 'https://mashatel.me/product/12374', 'https://mashatel.me/product/13940', 'https://mashatel.me/product/1189', 'https://mashatel.me/product/1187', 'https://mashatel.me/product/1186', 'https://mashatel.me/product/13691', 'https://mashatel.me/product/1688', 'https://mashatel.me/product/12149', 'https://mashatel.me/product/3148', 'https://mashatel.me/product/12145', 'https://mashatel.me/product/12346', 'https://mashatel.me/product/13681', 'https://mashatel.me/product/13898', 'https://mashatel.me/product/12225', 'https://mashatel.me/product/14105', 'https://mashatel.me/product/14101', 'https://mashatel.me/product/8572', 'https://mashatel.me/product/6139', 'https://mashatel.me/product/905', 'https://mashatel.me/product/14052', 'https://mashatel.me/product/12372', 'https://mashatel.me/product/14007', 'https://mashatel.me/product/8358', 'https://mashatel.me/product/12263', 'https://mashatel.me/product/2597', 'https://mashatel.me/product/908', 'https://mashatel.me/product/13950', 'https://mashatel.me/product/13948', 'https://mashatel.me/product/13944', 'https://mashatel.me/product/1170', 'https://mashatel.me/product/12182', 'https://mashatel.me/product/12188', 'https://mashatel.me/product/12179', 'https://mashatel.me/product/587', 'https://mashatel.me/product/12185', 'https://mashatel.me/product/13643', 'https://mashatel.me/product/13707', 'https://mashatel.me/product/13711', 'https://mashatel.me/product/13712', 'https://mashatel.me/product/13715', 'https://mashatel.me/product/12102', 'https://mashatel.me/product/12108', 'https://mashatel.me/product/12063', 'https://mashatel.me/product/12299', 'https://mashatel.me/product/12304', 'https://mashatel.me/product/12306', 'https://mashatel.me/product/12439', 'https://mashatel.me/product/11878', 'https://mashatel.me/product/8522', 'https://mashatel.me/product/1207', 'https://mashatel.me/product/1172', 'https://mashatel.me/product/12610', 'https://mashatel.me/product/12206', 'https://mashatel.me/product/8308', 'https://mashatel.me/product/13686', 'https://mashatel.me/product/8574', 'https://mashatel.me/product/8474', 'https://mashatel.me/product/8526', 'https://mashatel.me/product/8558', 'https://mashatel.me/product/1177', 'https://mashatel.me/product/9650', 'https://mashatel.me/product/13642', 'https://mashatel.me/product/13640', 'https://mashatel.me/product/13639', 'https://mashatel.me/product/13638', 'https://mashatel.me/product/593', 'https://mashatel.me/product/2605', 'https://mashatel.me/product/7226', 'https://mashatel.me/product/12488', 'https://mashatel.me/product/13405', 'https://mashatel.me/product/12037', 'https://mashatel.me/product/561', 'https://mashatel.me/product/13407', 'https://mashatel.me/product/13403', 'https://mashatel.me/product/13401', 'https://mashatel.me/product/7162', 'https://mashatel.me/product/2590', 'https://mashatel.me/product/7122', 'https://mashatel.me/product/7250', 'https://mashatel.me/product/12736', 'https://mashatel.me/product/565', 'https://mashatel.me/product/7920', 'https://mashatel.me/product/564', 'https://mashatel.me/product/1698', 'https://mashatel.me/product/1699', 'https://mashatel.me/product/12744', 'https://mashatel.me/product/12741', 'https://mashatel.me/product/12742', 'https://mashatel.me/product/12740', 'https://mashatel.me/product/12714', 'https://mashatel.me/product/12705', 'https://mashatel.me/product/12597', 'https://mashatel.me/product/7934', 'https://mashatel.me/product/7601', 'https://mashatel.me/product/589', 'https://mashatel.me/product/6136', 'https://mashatel.me/product/8359', 'https://mashatel.me/product/863', 'https://mashatel.me/product/12543', 'https://mashatel.me/product/6204', 'https://mashatel.me/product/12499', 'https://mashatel.me/product/8234', 'https://mashatel.me/product/6141', 'https://mashatel.me/product/12484', 'https://mashatel.me/product/7180', 'https://mashatel.me/product/12153', 'https://mashatel.me/product/7156', 'https://mashatel.me/product/7160', 'https://mashatel.me/product/7248', 'https://mashatel.me/product/7603', 'https://mashatel.me/product/12391', 'https://mashatel.me/product/2861', 'https://mashatel.me/product/1185', 'https://mashatel.me/product/12336', 'https://mashatel.me/product/12315', 'https://mashatel.me/product/12312', 'https://mashatel.me/product/6185', 'https://mashatel.me/product/12230', 'https://mashatel.me/product/12207', 'https://mashatel.me/product/572', 'https://mashatel.me/product/12061', 'https://mashatel.me/product/12044', 'https://mashatel.me/product/12041', 'https://mashatel.me/product/11885', 'https://mashatel.me/product/8488', 'https://mashatel.me/product/7910', 'https://mashatel.me/product/8434', 'https://mashatel.me/product/11259', 'https://mashatel.me/product/8564', 'https://mashatel.me/product/8428', 'https://mashatel.me/product/8426', 'https://mashatel.me/product/8432', 'https://mashatel.me/product/8592', 'https://mashatel.me/product/8400', 'https://mashatel.me/product/8486', 'https://mashatel.me/product/8466', 'https://mashatel.me/product/8580', 'https://mashatel.me/product/1206', 'https://mashatel.me/product/8307', 'https://mashatel.me/product/8468', 'https://mashatel.me/product/8542', 'https://mashatel.me/product/9640', 'https://mashatel.me/product/2901', 'https://mashatel.me/product/8422', 'https://mashatel.me/product/8416', 'https://mashatel.me/product/6282', 'https://mashatel.me/product/2902', 'https://mashatel.me/product/8438', 'https://mashatel.me/product/8482', 'https://mashatel.me/product/8448', 'https://mashatel.me/product/860', 'https://mashatel.me/product/7220', 'https://mashatel.me/product/7543', 'https://mashatel.me/product/8554', 'https://mashatel.me/product/7218', 'https://mashatel.me/product/6178', 'https://mashatel.me/product/8436', 'https://mashatel.me/product/8498', 'https://mashatel.me/product/902', 'https://mashatel.me/product/8418', 'https://mashatel.me/product/7120', 'https://mashatel.me/product/7202', 'https://mashatel.me/product/2583', 'https://mashatel.me/product/7124', 'https://mashatel.me/product/7602', 'https://mashatel.me/product/6176', 'https://mashatel.me/product/2708', 'https://mashatel.me/product/7126', 'https://mashatel.me/product/9086']
num = 1

sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "بائع رمز المسلسل وعاء"
sh[f'G{num}'] = 'انواع'
sh[f'H{num}'] = 'تنوع'
sh[f'I{num}'] = 'مستوى صعوبة النمو'
sh[f'J{num}'] = 'ضوء الشمس'
sh[f'K{num}'] = 'الأسماء الشائعة'
sh[f'L{num}'] = 'سقي النبات'
sh[f'M{num}'] = 'التربة'
sh[f'N{num}'] = 'السماد'
sh[f'O{num}'] = 'النوع'
sh[f'P{num}'] = 'ارتفاع النبات (سم)'
sh[f'Q{num}'] = 'حجم الاناء (سم)'
sh[f'R{num}'] = 'مستوى سام'
sh[f'S{num}'] = "الوصف"

sh[f'U{num}'] = 'name'
sh[f'V{num}'] = 'price'
sh[f'W{num}'] = 'state'
sh[f'X{num}'] = 'seller'
sh[f'Y{num}'] = 'Species'
sh[f'Z{num}'] = 'Variety'
sh[f'AA{num}'] = 'Difficulty to Grow'
sh[f'AB{num}'] = 'Sunlight'
sh[f'AC{num}'] = 'Common Names'
sh[f'AD{num}'] = 'Water'
sh[f'AE{num}'] = 'Soil'
sh[f'AF{num}'] = 'Fertilizers'
sh[f'AG{num}'] = 'Genus'
sh[f'AH{num}'] = 'Height'
sh[f'AI{num}'] = 'Size'
sh[f'AJ{num}'] = 'Toxic Level'
sh[f'AK{num}'] = 'des'
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        try:
            Species = [elem.text.replace('Species :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Species :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('Difficulty to Grow :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Difficulty to Grow :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('Sunlight :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Sunlight :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('Common Names :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Common Names :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('Water :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Water :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('Soil :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Soil :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('Fertilizers :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Fertilizers :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('Genus :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Genus :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('Plant Height (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Plant Height (cm) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('Pot Size (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Size (cm) :' in elem.text][0]
        except:
            Size = None
        try:
            posnous = [elem.text.replace('Toxic Level :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Toxic Level :' in elem.text][0]
        except:
            posnous=None

        ################################################################################################################
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            Species = [elem.text.replace('انواع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'انواع :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('مستوى صعوبة النمو :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى صعوبة النمو :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('ضوء الشمس :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ضوء الشمس :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('الأسماء الشائعة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الأسماء الشائعة :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('سقي النبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'سقي النبات :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('التربة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'التربة :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('السماد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'السماد :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('النوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'النوع :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('ارتفاع النبات (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ارتفاع النبات (سم) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('حجم الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'حجم الاناء (سم) :' in elem.text][0]
        except:
            Size = None

        try:
            posnous = [elem.text.replace('مستوى سام :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى سام :' in elem.text][0]
        except:
            posnous=None
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = code
        sh[f'G{num}'] = Species
        sh[f'H{num}'] = Variety
        sh[f'I{num}'] = Grow
        sh[f'J{num}'] = Sunlight
        sh[f'K{num}'] = Common
        sh[f'L{num}'] = Water
        sh[f'M{num}'] = Soil
        sh[f'N{num}'] = Fertilizers
        sh[f'O{num}'] = Genus
        sh[f'P{num}'] = Height
        sh[f'Q{num}'] = Size
        sh[f'R{num}'] = posnous
        sh[f'S{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'T{num}')

        sh[f'U{num}'] = name
        sh[f'V{num}'] = price
        sh[f'W{num}'] = state
        sh[f'X{num}'] = seller
        sh[f'Y{num}'] = Species
        sh[f'Z{num}'] = Variety
        sh[f'AA{num}'] = Grow
        sh[f'AB{num}'] = Sunlight
        sh[f'AC{num}'] = Common
        sh[f'AD{num}'] = Water
        sh[f'AE{num}'] = Soil
        sh[f'AF{num}'] = Fertilizers
        sh[f'AG{num}'] = Genus
        sh[f'AH{num}'] = Height
        sh[f'AI{num}'] = Size
        sh[f'AJ{num}'] = posnous
        sh[f'AK{num}'] = des
        num += 1
        print(num)
    except:
        pass
sheet.save('INDOOR PLANTS.xlsx')
'''
'''
('https://mashatel.me/category/27', 'OUTDOOR PLANTS')

urll = ['https://mashatel.me/product/14420', 'https://mashatel.me/product/14414', 'https://mashatel.me/product/12423', 'https://mashatel.me/product/12447', 'https://mashatel.me/product/12460', 'https://mashatel.me/product/12680', 'https://mashatel.me/product/12747', 'https://mashatel.me/product/12764', 'https://mashatel.me/product/12896', 'https://mashatel.me/product/12935', 'https://mashatel.me/product/12942', 'https://mashatel.me/product/12968', 'https://mashatel.me/product/12978', 'https://mashatel.me/product/12984', 'https://mashatel.me/product/12986', 'https://mashatel.me/product/12443', 'https://mashatel.me/product/12451', 'https://mashatel.me/product/12453', 'https://mashatel.me/product/12456', 'https://mashatel.me/product/12678', 'https://mashatel.me/product/13551', 'https://mashatel.me/product/13563', 'https://mashatel.me/product/13703', 'https://mashatel.me/product/13705', 'https://mashatel.me/product/14210', 'https://mashatel.me/product/600', 'https://mashatel.me/product/611', 'https://mashatel.me/product/616', 'https://mashatel.me/product/928', 'https://mashatel.me/product/1118', 'https://mashatel.me/product/1147', 'https://mashatel.me/product/6571', 'https://mashatel.me/product/6804', 'https://mashatel.me/product/7369', 'https://mashatel.me/product/7437', 'https://mashatel.me/product/259', 'https://mashatel.me/product/261', 'https://mashatel.me/product/262', 'https://mashatel.me/product/272', 'https://mashatel.me/product/279', 'https://mashatel.me/product/282', 'https://mashatel.me/product/283', 'https://mashatel.me/product/284', 'https://mashatel.me/product/285', 'https://mashatel.me/product/13252', 'https://mashatel.me/product/14277', 'https://mashatel.me/product/615', 'https://mashatel.me/product/12745', 'https://mashatel.me/product/12751', 'https://mashatel.me/product/12753', 'https://mashatel.me/product/12757', 'https://mashatel.me/product/12759', 'https://mashatel.me/product/12762', 'https://mashatel.me/product/12900', 'https://mashatel.me/product/12944', 'https://mashatel.me/product/12956', 'https://mashatel.me/product/12958', 'https://mashatel.me/product/12962', 'https://mashatel.me/product/12972', 'https://mashatel.me/product/12976', 'https://mashatel.me/product/12980', 'https://mashatel.me/product/12449', 'https://mashatel.me/product/12454', 'https://mashatel.me/product/12455', 'https://mashatel.me/product/13144', 'https://mashatel.me/product/13150', 'https://mashatel.me/product/13159', 'https://mashatel.me/product/13162', 'https://mashatel.me/product/13155', 'https://mashatel.me/product/13229', 'https://mashatel.me/product/13235', 'https://mashatel.me/product/13269', 'https://mashatel.me/product/13701', 'https://mashatel.me/product/12946', 'https://mashatel.me/product/13137', 'https://mashatel.me/product/2807', 'https://mashatel.me/product/12672', 'https://mashatel.me/product/275', 'https://mashatel.me/product/927', 'https://mashatel.me/product/12689', 'https://mashatel.me/product/13919', 'https://mashatel.me/product/14179', 'https://mashatel.me/product/14149', 'https://mashatel.me/product/14131', 'https://mashatel.me/product/6591', 'https://mashatel.me/product/1096', 'https://mashatel.me/product/6506', 'https://mashatel.me/product/12198', 'https://mashatel.me/product/12674', 'https://mashatel.me/product/1095', 'https://mashatel.me/product/14057', 'https://mashatel.me/product/12659', 'https://mashatel.me/product/273', 'https://mashatel.me/product/13931', 'https://mashatel.me/product/13927', 'https://mashatel.me/product/12668', 'https://mashatel.me/product/13925', 'https://mashatel.me/product/13913', 'https://mashatel.me/product/13921', 'https://mashatel.me/product/13915', 'https://mashatel.me/product/13917', 'https://mashatel.me/product/934', 'https://mashatel.me/product/12196', 'https://mashatel.me/product/6223', 'https://mashatel.me/product/12686', 'https://mashatel.me/product/12684', 'https://mashatel.me/product/12682', 'https://mashatel.me/product/8950', 'https://mashatel.me/product/12052', 'https://mashatel.me/product/12055', 'https://mashatel.me/product/12117', 'https://mashatel.me/product/12119', 'https://mashatel.me/product/12121', 'https://mashatel.me/product/12123', 'https://mashatel.me/product/12175', 'https://mashatel.me/product/12177', 'https://mashatel.me/product/12190', 'https://mashatel.me/product/12192', 'https://mashatel.me/product/12200', 'https://mashatel.me/product/6585', 'https://mashatel.me/product/12666', 'https://mashatel.me/product/13668', 'https://mashatel.me/product/7359', 'https://mashatel.me/product/7365', 'https://mashatel.me/product/7383', 'https://mashatel.me/product/13475', 'https://mashatel.me/product/280', 'https://mashatel.me/product/2673', 'https://mashatel.me/product/1085', 'https://mashatel.me/product/7415', 'https://mashatel.me/product/7423', 'https://mashatel.me/product/7385', 'https://mashatel.me/product/707', 'https://mashatel.me/product/12046', 'https://mashatel.me/product/705', 'https://mashatel.me/product/12049', 'https://mashatel.me/product/935', 'https://mashatel.me/product/263', 'https://mashatel.me/product/12690', 'https://mashatel.me/product/7118', 'https://mashatel.me/product/1084', 'https://mashatel.me/product/12615', 'https://mashatel.me/product/12599', 'https://mashatel.me/product/608', 'https://mashatel.me/product/2924', 'https://mashatel.me/product/1086', 'https://mashatel.me/product/12485', 'https://mashatel.me/product/1083', 'https://mashatel.me/product/12363', 'https://mashatel.me/product/1078', 'https://mashatel.me/product/7930', 'https://mashatel.me/product/1077', 'https://mashatel.me/product/1079', 'https://mashatel.me/product/1080', 'https://mashatel.me/product/1115', 'https://mashatel.me/product/1116', 'https://mashatel.me/product/6572', 'https://mashatel.me/product/6782', 'https://mashatel.me/product/6786', 'https://mashatel.me/product/6788', 'https://mashatel.me/product/6792', 'https://mashatel.me/product/6796', 'https://mashatel.me/product/7777', 'https://mashatel.me/product/603', 'https://mashatel.me/product/10754', 'https://mashatel.me/product/2327', 'https://mashatel.me/product/1209', 'https://mashatel.me/product/1683', 'https://mashatel.me/product/6147', 'https://mashatel.me/product/613', 'https://mashatel.me/product/1117', 'https://mashatel.me/product/942', 'https://mashatel.me/product/1094', 'https://mashatel.me/product/2336', 'https://mashatel.me/product/609', 'https://mashatel.me/product/614', 'https://mashatel.me/product/929', 'https://mashatel.me/product/604', 'https://mashatel.me/product/1211', 'https://mashatel.me/product/1681', 'https://mashatel.me/product/606']
num = 1
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "بائع رمز المسلسل وعاء"
sh[f'G{num}'] = 'انواع'
sh[f'H{num}'] = 'تنوع'
sh[f'I{num}'] = 'مستوى صعوبة النمو'
sh[f'J{num}'] = 'ضوء الشمس'
sh[f'K{num}'] = 'الأسماء الشائعة'
sh[f'L{num}'] = 'سقي النبات'
sh[f'M{num}'] = 'التربة'
sh[f'N{num}'] = 'السماد'
sh[f'O{num}'] = 'النوع'
sh[f'P{num}'] = 'ارتفاع النبات (سم)'
sh[f'Q{num}'] = 'حجم الاناء (سم)'
sh[f'R{num}'] = 'مستوى سام'
sh[f'S{num}'] = "الوصف"
"""
sh[f'U{num}'] = 'name'
sh[f'V{num}'] = 'price'
sh[f'W{num}'] = 'state'
sh[f'X{num}'] = 'seller'
sh[f'Y{num}'] = 'Species'
sh[f'Z{num}'] = 'Variety'
sh[f'AA{num}'] = 'Difficulty to Grow'
sh[f'AB{num}'] = 'Sunlight'
sh[f'AC{num}'] = 'Common Names'
sh[f'AD{num}'] = 'Water'
sh[f'AE{num}'] = 'Soil'
sh[f'AF{num}'] = 'Fertilizers'
sh[f'AG{num}'] = 'Genus'
sh[f'AH{num}'] = 'Height'
sh[f'AI{num}'] = 'Size'
sh[f'AJ{num}'] = 'Toxic Level'
sh[f'AK{num}'] = 'des'
num = 2
driver.get(urll[0])
sleep(5)
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        try:
            Species = [elem.text.replace('Species :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Species :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('Difficulty to Grow :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Difficulty to Grow :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('Sunlight :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Sunlight :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('Common Names :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Common Names :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('Water :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Water :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('Soil :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Soil :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('Fertilizers :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Fertilizers :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('Genus :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Genus :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('Plant Height (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Plant Height (cm) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('Pot Size (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Size (cm) :' in elem.text][0]
        except:
            Size = None
        try:
            posnous = [elem.text.replace('Toxic Level :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Toxic Level :' in elem.text][0]
        except:
            posnous=None
        """
        ################################################################################################################
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            Species = [elem.text.replace('انواع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'انواع :' in elem.text][0]
        except:
            Species = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None
        try:
            Grow = [elem.text.replace('مستوى صعوبة النمو :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى صعوبة النمو :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('ضوء الشمس :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ضوء الشمس :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('الأسماء الشائعة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الأسماء الشائعة :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('سقي النبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'سقي النبات :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('التربة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'التربة :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('السماد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'السماد :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('النوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'النوع :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('ارتفاع النبات (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ارتفاع النبات (سم) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('حجم الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'حجم الاناء (سم) :' in elem.text][0]
        except:
            Size = None

        try:
            posnous = [elem.text.replace('مستوى سام :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى سام :' in elem.text][0]
        except:
            posnous=None
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = code
        sh[f'G{num}'] = Species
        sh[f'H{num}'] = Variety
        sh[f'I{num}'] = Grow
        sh[f'J{num}'] = Sunlight
        sh[f'K{num}'] = Common
        sh[f'L{num}'] = Water
        sh[f'M{num}'] = Soil
        sh[f'N{num}'] = Fertilizers
        sh[f'O{num}'] = Genus
        sh[f'P{num}'] = Height
        sh[f'Q{num}'] = Size
        sh[f'R{num}'] = posnous
        sh[f'S{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'T{num}')

        """
        sh[f'U{num}'] = name
        sh[f'V{num}'] = price
        sh[f'W{num}'] = state
        sh[f'X{num}'] = seller
        sh[f'Y{num}'] = Species
        sh[f'Z{num}'] = Variety
        sh[f'AA{num}'] = Grow
        sh[f'AB{num}'] = Sunlight
        sh[f'AC{num}'] = Common
        sh[f'AD{num}'] = Water
        sh[f'AE{num}'] = Soil
        sh[f'AF{num}'] = Fertilizers
        sh[f'AG{num}'] = Genus
        sh[f'AH{num}'] = Height
        sh[f'AI{num}'] = Size
        sh[f'AJ{num}'] = posnous
        sh[f'AK{num}'] = des
        num += 1
        print(num)
    except:
        pass
sheet.save('OUTDOOR PLANTS.xlsx')
'''
'''
('https://mashatel.me/category/130', 'WHOLESALE FLOWERS')

urll = ['https://mashatel.me/product/8994', 'https://mashatel.me/product/12014', 'https://mashatel.me/product/12016', 'https://mashatel.me/product/12017', 'https://mashatel.me/product/13375', 'https://mashatel.me/product/14050', 'https://mashatel.me/product/12020', 'https://mashatel.me/product/12051', 'https://mashatel.me/product/12060', 'https://mashatel.me/product/12070', 'https://mashatel.me/product/12073', 'https://mashatel.me/product/12077', 'https://mashatel.me/product/12087', 'https://mashatel.me/product/12093', 'https://mashatel.me/product/12094', 'https://mashatel.me/product/12292', 'https://mashatel.me/product/13365', 'https://mashatel.me/product/13372', 'https://mashatel.me/product/13373', 'https://mashatel.me/product/13377', 'https://mashatel.me/product/13378', 'https://mashatel.me/product/13381', 'https://mashatel.me/product/13418', 'https://mashatel.me/product/13958', 'https://mashatel.me/product/13965', 'https://mashatel.me/product/13967', 'https://mashatel.me/product/13968', 'https://mashatel.me/product/14192', 'https://mashatel.me/product/14202', 'https://mashatel.me/product/14203', 'https://mashatel.me/product/14205', 'https://mashatel.me/product/14212', 'https://mashatel.me/product/14220', 'https://mashatel.me/product/14223', 'https://mashatel.me/product/14225', 'https://mashatel.me/product/14228', 'https://mashatel.me/product/14230', 'https://mashatel.me/product/14381', 'https://mashatel.me/product/14383', 'https://mashatel.me/product/14215', 'https://mashatel.me/product/7902', 'https://mashatel.me/product/9378', 'https://mashatel.me/product/14185', 'https://mashatel.me/product/14186', 'https://mashatel.me/product/14204', 'https://mashatel.me/product/14216', 'https://mashatel.me/product/14227', 'https://mashatel.me/product/14379', 'https://mashatel.me/product/14380', 'https://mashatel.me/product/14382', 'https://mashatel.me/product/14384', 'https://mashatel.me/product/14385', 'https://mashatel.me/product/14386', 'https://mashatel.me/product/14387', 'https://mashatel.me/product/14388', 'https://mashatel.me/product/14389', 'https://mashatel.me/product/14390', 'https://mashatel.me/product/14391', 'https://mashatel.me/product/14407', 'https://mashatel.me/product/14410', 'https://mashatel.me/product/14408', 'https://mashatel.me/product/14406', 'https://mashatel.me/product/14405', 'https://mashatel.me/product/14404', 'https://mashatel.me/product/14394', 'https://mashatel.me/product/14395', 'https://mashatel.me/product/12269', 'https://mashatel.me/product/14218', 'https://mashatel.me/product/14357', 'https://mashatel.me/product/14356', 'https://mashatel.me/product/14355', 'https://mashatel.me/product/14354', 'https://mashatel.me/product/14353', 'https://mashatel.me/product/14352', 'https://mashatel.me/product/14351', 'https://mashatel.me/product/14350', 'https://mashatel.me/product/14347', 'https://mashatel.me/product/14344', 'https://mashatel.me/product/14343', 'https://mashatel.me/product/9379', 'https://mashatel.me/product/12258', 'https://mashatel.me/product/13376', 'https://mashatel.me/product/12289', 'https://mashatel.me/product/12248', 'https://mashatel.me/product/12634', 'https://mashatel.me/product/12638', 'https://mashatel.me/product/12630', 'https://mashatel.me/product/12636', 'https://mashatel.me/product/12632', 'https://mashatel.me/product/12628', 'https://mashatel.me/product/12626', 'https://mashatel.me/product/12624', 'https://mashatel.me/product/9381', 'https://mashatel.me/product/12378', 'https://mashatel.me/product/12246', 'https://mashatel.me/product/12252', 'https://mashatel.me/product/12234', 'https://mashatel.me/product/12250', 'https://mashatel.me/product/12244', 'https://mashatel.me/product/12242', 'https://mashatel.me/product/12240', 'https://mashatel.me/product/9049', 'https://mashatel.me/product/12083', 'https://mashatel.me/product/8993', 'https://mashatel.me/product/9002', 'https://mashatel.me/product/8990', 'https://mashatel.me/product/9098', 'https://mashatel.me/product/9121', 'https://mashatel.me/product/9126', 'https://mashatel.me/product/9128', 'https://mashatel.me/product/9124', 'https://mashatel.me/product/8992', 'https://mashatel.me/product/9102', 'https://mashatel.me/product/9001', 'https://mashatel.me/product/9003', 'https://mashatel.me/product/9014', 'https://mashatel.me/product/9006']
num = 1
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = 'السعر'
sh[f'D{num}'] = 'الحالة'
sh[f'E{num}'] = 'البائع'
sh[f'F{num}'] = 'اللون'
sh[f'G{num}'] = 'بائع رمز المسلسل وعاء'
sh[f'H{num}'] = 'عدد السيقان'
sh[f'I{num}'] = 'طول الساق'
sh[f'J{num}'] = 'الوصف'
#######################
"""
sh[f'L{num}'] = 'name'
sh[f'M{num}'] = 'price'
sh[f'N{num}'] = 'state'
sh[f'O{num}'] = 'seller'
sh[f'P{num}'] = 'Color'
sh[f'Q{num}'] = 'Volume'
sh[f'R{num}'] = 'Variety'
sh[f'S{num}'] = 'des'

num = 2
driver.get(urll[0])
sleep(8)
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None

        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][0]
        except:
            Color = None
        try:
            number = [elem.text.replace('Number of Stems :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Number of Stems :' in elem.text][0]
        except:
            number = None
        try:
            Height = [elem.text.replace('Bunch Height (cm) :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Bunch Height (cm) :' in elem.text][0]
        except:
            Height = None
        """

        #################################################

        try:
            Colorar = [elem.text.replace('اللون :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'اللون :' in elem.text][0]
        except:
            Colorar = None
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            number = [elem.text.replace('عدد السيقان :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'عدد السيقان :' in elem.text][0]
        except:
            number = None
        try:
            Height = [elem.text.replace('طول الساق :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'طول الساق :' in elem.text][0]
        except:
            Height = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Colorar
        sh[f'G{num}'] = code
        sh[f'H{num}'] = number
        sh[f'I{num}'] = Height
        sh[f'J{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'K{num}')

        """
        sh[f'L{num}'] = name
        sh[f'M{num}'] = price
        sh[f'N{num}'] = state
        sh[f'O{num}'] = seller
        sh[f'P{num}'] = Color
        sh[f'Q{num}'] = number
        sh[f'R{num}'] = Height
        sh[f'S{num}'] = des

        num += 1
    except Exception as e:
        print(e)

sheet.save('WHOLESALE FLOWERS.xlsx')
'''
'''
('https://mashatel.me/category/76', 'POTS & VASES')

num=1
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "اللون"
sh[f'G{num}'] = 'تنوع'
sh[f'H{num}'] = "بائع رمز المسلسل وعاء"
sh[f'J{num}'] = "الارتفاع"
sh[f'H{num}'] = "القطر"
sh[f'I{num}'] = "الطول"
sh[f'J{num}'] = "العرض"
sh[f'K{num}'] = "مثال ل"
sh[f'L{num}'] = "الشكل"
sh[f'M{num}'] = "المواد"
sh[f'N{num}'] = "القاعده"
sh[f'O{num}'] = "الوصف"
"""
sh[f'Q{num}'] = 'name'
sh[f'R{num}'] = 'price'
sh[f'S{num}'] = 'state'
sh[f'T{num}'] = 'seller'
sh[f'U{num}'] = 'Color'
sh[f'V{num}'] = 'Variety'
sh[f'W{num}'] = 'high'
sh[f'X{num}'] = 'Diameter'
sh[f'Y{num}'] = 'loning'
sh[f'Z{num}'] = 'wegd'
sh[f'AA{num}'] = 'Ideal'
sh[f'AB{num}'] = 'Shape'
sh[f'AC{num}'] = 'Material'
sh[f'AD{num}'] = 'Pot Plate'
sh[f'AE{num}'] = 'des'

urll = ['https://mashatel.me/product/14044', 'https://mashatel.me/product/13757', 'https://mashatel.me/product/11994', 'https://mashatel.me/product/12704', 'https://mashatel.me/product/12719', 'https://mashatel.me/product/12774', 'https://mashatel.me/product/12778', 'https://mashatel.me/product/12780', 'https://mashatel.me/product/12796', 'https://mashatel.me/product/12800', 'https://mashatel.me/product/12836', 'https://mashatel.me/product/12838', 'https://mashatel.me/product/13044', 'https://mashatel.me/product/13210', 'https://mashatel.me/product/13213', 'https://mashatel.me/product/13218', 'https://mashatel.me/product/13225', 'https://mashatel.me/product/13227', 'https://mashatel.me/product/12708', 'https://mashatel.me/product/351', 'https://mashatel.me/product/353', 'https://mashatel.me/product/2511', 'https://mashatel.me/product/9372', 'https://mashatel.me/product/10861', 'https://mashatel.me/product/10863', 'https://mashatel.me/product/10867', 'https://mashatel.me/product/10869', 'https://mashatel.me/product/10875', 'https://mashatel.me/product/10931', 'https://mashatel.me/product/10865', 'https://mashatel.me/product/331', 'https://mashatel.me/product/337', 'https://mashatel.me/product/345', 'https://mashatel.me/product/10841', 'https://mashatel.me/product/10845', 'https://mashatel.me/product/10873', 'https://mashatel.me/product/12862', 'https://mashatel.me/product/14189', 'https://mashatel.me/product/13741', 'https://mashatel.me/product/14369', 'https://mashatel.me/product/14367', 'https://mashatel.me/product/14365', 'https://mashatel.me/product/14362', 'https://mashatel.me/product/14360', 'https://mashatel.me/product/405', 'https://mashatel.me/product/13766', 'https://mashatel.me/product/13764', 'https://mashatel.me/product/438', 'https://mashatel.me/product/439', 'https://mashatel.me/product/440', 'https://mashatel.me/product/417', 'https://mashatel.me/product/418', 'https://mashatel.me/product/14316', 'https://mashatel.me/product/503', 'https://mashatel.me/product/11922', 'https://mashatel.me/product/14306', 'https://mashatel.me/product/10941', 'https://mashatel.me/product/14297', 'https://mashatel.me/product/14296', 'https://mashatel.me/product/14295', 'https://mashatel.me/product/14290', 'https://mashatel.me/product/14289', 'https://mashatel.me/product/14287', 'https://mashatel.me/product/14285', 'https://mashatel.me/product/14281', 'https://mashatel.me/product/14275', 'https://mashatel.me/product/14273', 'https://mashatel.me/product/12776', 'https://mashatel.me/product/12834', 'https://mashatel.me/product/14075', 'https://mashatel.me/product/14080', 'https://mashatel.me/product/14081', 'https://mashatel.me/product/13811', 'https://mashatel.me/product/13756', 'https://mashatel.me/product/13758', 'https://mashatel.me/product/13736', 'https://mashatel.me/product/13760', 'https://mashatel.me/product/13775', 'https://mashatel.me/product/322', 'https://mashatel.me/product/13735', 'https://mashatel.me/product/10847', 'https://mashatel.me/product/10849', 'https://mashatel.me/product/10851', 'https://mashatel.me/product/10899', 'https://mashatel.me/product/10881', 'https://mashatel.me/product/10883', 'https://mashatel.me/product/10889', 'https://mashatel.me/product/10897', 'https://mashatel.me/product/14085', 'https://mashatel.me/product/14084', 'https://mashatel.me/product/14083', 'https://mashatel.me/product/14082', 'https://mashatel.me/product/14079', 'https://mashatel.me/product/14078', 'https://mashatel.me/product/14076', 'https://mashatel.me/product/14074', 'https://mashatel.me/product/14071', 'https://mashatel.me/product/14070', 'https://mashatel.me/product/14067', 'https://mashatel.me/product/14064', 'https://mashatel.me/product/14063', 'https://mashatel.me/product/14062', 'https://mashatel.me/product/14061', 'https://mashatel.me/product/14060', 'https://mashatel.me/product/13799', 'https://mashatel.me/product/13790', 'https://mashatel.me/product/14047', 'https://mashatel.me/product/408', 'https://mashatel.me/product/10887', 'https://mashatel.me/product/10895', 'https://mashatel.me/product/10925', 'https://mashatel.me/product/10943', 'https://mashatel.me/product/14045', 'https://mashatel.me/product/14046', 'https://mashatel.me/product/14043', 'https://mashatel.me/product/14042', 'https://mashatel.me/product/14041', 'https://mashatel.me/product/14040', 'https://mashatel.me/product/14021', 'https://mashatel.me/product/14031', 'https://mashatel.me/product/14030', 'https://mashatel.me/product/14029', 'https://mashatel.me/product/14028', 'https://mashatel.me/product/14026', 'https://mashatel.me/product/14025', 'https://mashatel.me/product/14023', 'https://mashatel.me/product/12002', 'https://mashatel.me/product/12434', 'https://mashatel.me/product/13034', 'https://mashatel.me/product/13833', 'https://mashatel.me/product/13832', 'https://mashatel.me/product/10746', 'https://mashatel.me/product/13809', 'https://mashatel.me/product/13788', 'https://mashatel.me/product/13779', 'https://mashatel.me/product/13802', 'https://mashatel.me/product/13801', 'https://mashatel.me/product/13800', 'https://mashatel.me/product/13797', 'https://mashatel.me/product/13795', 'https://mashatel.me/product/13793', 'https://mashatel.me/product/13539', 'https://mashatel.me/product/13541', 'https://mashatel.me/product/13543', 'https://mashatel.me/product/13545', 'https://mashatel.me/product/13547', 'https://mashatel.me/product/13747', 'https://mashatel.me/product/13767', 'https://mashatel.me/product/13759', 'https://mashatel.me/product/10747', 'https://mashatel.me/product/13751', 'https://mashatel.me/product/13750', 'https://mashatel.me/product/13749', 'https://mashatel.me/product/13748', 'https://mashatel.me/product/13744', 'https://mashatel.me/product/13743', 'https://mashatel.me/product/13742', 'https://mashatel.me/product/13728', 'https://mashatel.me/product/13734', 'https://mashatel.me/product/13708', 'https://mashatel.me/product/13720', 'https://mashatel.me/product/13713', 'https://mashatel.me/product/13716', 'https://mashatel.me/product/13718', 'https://mashatel.me/product/13032', 'https://mashatel.me/product/389', 'https://mashatel.me/product/323', 'https://mashatel.me/product/13624', 'https://mashatel.me/product/324', 'https://mashatel.me/product/435', 'https://mashatel.me/product/326', 'https://mashatel.me/product/447', 'https://mashatel.me/product/329', 'https://mashatel.me/product/330', 'https://mashatel.me/product/325', 'https://mashatel.me/product/445', 'https://mashatel.me/product/446', 'https://mashatel.me/product/10923', 'https://mashatel.me/product/10927', 'https://mashatel.me/product/10929', 'https://mashatel.me/product/10933', 'https://mashatel.me/product/10935', 'https://mashatel.me/product/10937', 'https://mashatel.me/product/13024', 'https://mashatel.me/product/13026', 'https://mashatel.me/product/13028', 'https://mashatel.me/product/13030', 'https://mashatel.me/product/13036', 'https://mashatel.me/product/13038', 'https://mashatel.me/product/13040', 'https://mashatel.me/product/13042', 'https://mashatel.me/product/13046', 'https://mashatel.me/product/13048', 'https://mashatel.me/product/13050', 'https://mashatel.me/product/13052', 'https://mashatel.me/product/13054', 'https://mashatel.me/product/13056', 'https://mashatel.me/product/13058', 'https://mashatel.me/product/13062', 'https://mashatel.me/product/13064', 'https://mashatel.me/product/13074', 'https://mashatel.me/product/13097', 'https://mashatel.me/product/13099', 'https://mashatel.me/product/13101', 'https://mashatel.me/product/12960', 'https://mashatel.me/product/12994', 'https://mashatel.me/product/12996', 'https://mashatel.me/product/12998', 'https://mashatel.me/product/13000', 'https://mashatel.me/product/13004', 'https://mashatel.me/product/13008', 'https://mashatel.me/product/13010', 'https://mashatel.me/product/13012', 'https://mashatel.me/product/13014', 'https://mashatel.me/product/13016', 'https://mashatel.me/product/13020', 'https://mashatel.me/product/13022', 'https://mashatel.me/product/407', 'https://mashatel.me/product/411', 'https://mashatel.me/product/12914', 'https://mashatel.me/product/12916', 'https://mashatel.me/product/12920', 'https://mashatel.me/product/12928', 'https://mashatel.me/product/12844', 'https://mashatel.me/product/12882', 'https://mashatel.me/product/12884', 'https://mashatel.me/product/12888', 'https://mashatel.me/product/12890', 'https://mashatel.me/product/12906', 'https://mashatel.me/product/12908', 'https://mashatel.me/product/12910', 'https://mashatel.me/product/2512', 'https://mashatel.me/product/12864', 'https://mashatel.me/product/12874', 'https://mashatel.me/product/12876', 'https://mashatel.me/product/12878', 'https://mashatel.me/product/13362', 'https://mashatel.me/product/2528', 'https://mashatel.me/product/12828', 'https://mashatel.me/product/12830', 'https://mashatel.me/product/12832', 'https://mashatel.me/product/12840', 'https://mashatel.me/product/12842', 'https://mashatel.me/product/12846', 'https://mashatel.me/product/12848', 'https://mashatel.me/product/12850', 'https://mashatel.me/product/12852', 'https://mashatel.me/product/12798', 'https://mashatel.me/product/12802', 'https://mashatel.me/product/12804', 'https://mashatel.me/product/12808', 'https://mashatel.me/product/12812', 'https://mashatel.me/product/12814', 'https://mashatel.me/product/12818', 'https://mashatel.me/product/12822', 'https://mashatel.me/product/12782', 'https://mashatel.me/product/12788', 'https://mashatel.me/product/12790', 'https://mashatel.me/product/12792', 'https://mashatel.me/product/12794', 'https://mashatel.me/product/12770', 'https://mashatel.me/product/12772', 'https://mashatel.me/product/467', 'https://mashatel.me/product/399', 'https://mashatel.me/product/396', 'https://mashatel.me/product/398', 'https://mashatel.me/product/352', 'https://mashatel.me/product/359', 'https://mashatel.me/product/360', 'https://mashatel.me/product/412', 'https://mashatel.me/product/444', 'https://mashatel.me/product/462', 'https://mashatel.me/product/11998', 'https://mashatel.me/product/2537', 'https://mashatel.me/product/11997', 'https://mashatel.me/product/7977', 'https://mashatel.me/product/11271', 'https://mashatel.me/product/12724', 'https://mashatel.me/product/12723', 'https://mashatel.me/product/12721', 'https://mashatel.me/product/12720', 'https://mashatel.me/product/12718', 'https://mashatel.me/product/12716', 'https://mashatel.me/product/12710', 'https://mashatel.me/product/12709', 'https://mashatel.me/product/12707', 'https://mashatel.me/product/12706', 'https://mashatel.me/product/12698', 'https://mashatel.me/product/11274', 'https://mashatel.me/product/2509', 'https://mashatel.me/product/2510', 'https://mashatel.me/product/2527', 'https://mashatel.me/product/12618', 'https://mashatel.me/product/2016', 'https://mashatel.me/product/2024', 'https://mashatel.me/product/368', 'https://mashatel.me/product/375', 'https://mashatel.me/product/376', 'https://mashatel.me/product/12492', 'https://mashatel.me/product/12495', 'https://mashatel.me/product/12503', 'https://mashatel.me/product/12481', 'https://mashatel.me/product/12480', 'https://mashatel.me/product/12479', 'https://mashatel.me/product/12433', 'https://mashatel.me/product/12432', 'https://mashatel.me/product/12431', 'https://mashatel.me/product/12430', 'https://mashatel.me/product/12429', 'https://mashatel.me/product/12428', 'https://mashatel.me/product/11914', 'https://mashatel.me/product/11910', 'https://mashatel.me/product/11926', 'https://mashatel.me/product/2018', 'https://mashatel.me/product/2022', 'https://mashatel.me/product/2023', 'https://mashatel.me/product/10308', 'https://mashatel.me/product/12205', 'https://mashatel.me/product/12204', 'https://mashatel.me/product/12203', 'https://mashatel.me/product/11916', 'https://mashatel.me/product/11272', 'https://mashatel.me/product/11996', 'https://mashatel.me/product/11995', 'https://mashatel.me/product/11993', 'https://mashatel.me/product/11992', 'https://mashatel.me/product/11983', 'https://mashatel.me/product/11908', 'https://mashatel.me/product/11924', 'https://mashatel.me/product/11936', 'https://mashatel.me/product/11942', 'https://mashatel.me/product/11940', 'https://mashatel.me/product/11906', 'https://mashatel.me/product/11905', 'https://mashatel.me/product/9933', 'https://mashatel.me/product/9895', 'https://mashatel.me/product/11273', 'https://mashatel.me/product/2271', 'https://mashatel.me/product/2273', 'https://mashatel.me/product/2275', 'https://mashatel.me/product/9919', 'https://mashatel.me/product/9905', 'https://mashatel.me/product/9897', 'https://mashatel.me/product/9729', 'https://mashatel.me/product/9727', 'https://mashatel.me/product/9722', 'https://mashatel.me/product/9738', 'https://mashatel.me/product/9735', 'https://mashatel.me/product/9754', 'https://mashatel.me/product/9756', 'https://mashatel.me/product/9755', 'https://mashatel.me/product/11399', 'https://mashatel.me/product/9915', 'https://mashatel.me/product/9923', 'https://mashatel.me/product/9931', 'https://mashatel.me/product/10015', 'https://mashatel.me/product/11270', 'https://mashatel.me/product/11269', 'https://mashatel.me/product/11268', 'https://mashatel.me/product/9887', 'https://mashatel.me/product/9891', 'https://mashatel.me/product/9907', 'https://mashatel.me/product/457', 'https://mashatel.me/product/9917', 'https://mashatel.me/product/9921', 'https://mashatel.me/product/9925', 'https://mashatel.me/product/9927', 'https://mashatel.me/product/9929', 'https://mashatel.me/product/9935', 'https://mashatel.me/product/9937', 'https://mashatel.me/product/9941', 'https://mashatel.me/product/9943', 'https://mashatel.me/product/9945', 'https://mashatel.me/product/9955', 'https://mashatel.me/product/9959', 'https://mashatel.me/product/9963', 'https://mashatel.me/product/9965', 'https://mashatel.me/product/9967', 'https://mashatel.me/product/9969', 'https://mashatel.me/product/9971', 'https://mashatel.me/product/10013', 'https://mashatel.me/product/10027', 'https://mashatel.me/product/9953', 'https://mashatel.me/product/9951', 'https://mashatel.me/product/9913', 'https://mashatel.me/product/9911', 'https://mashatel.me/product/9909', 'https://mashatel.me/product/9901', 'https://mashatel.me/product/9899', 'https://mashatel.me/product/9893', 'https://mashatel.me/product/9889', 'https://mashatel.me/product/9885', 'https://mashatel.me/product/9883', 'https://mashatel.me/product/9877', 'https://mashatel.me/product/9374', 'https://mashatel.me/product/9734', 'https://mashatel.me/product/7994', 'https://mashatel.me/product/7995', 'https://mashatel.me/product/7997', 'https://mashatel.me/product/7996', 'https://mashatel.me/product/7998', 'https://mashatel.me/product/7999', 'https://mashatel.me/product/7993', 'https://mashatel.me/product/7991', 'https://mashatel.me/product/8002', 'https://mashatel.me/product/8003', 'https://mashatel.me/product/8004', 'https://mashatel.me/product/8005', 'https://mashatel.me/product/8006', 'https://mashatel.me/product/7983', 'https://mashatel.me/product/383', 'https://mashatel.me/product/458', 'https://mashatel.me/product/459', 'https://mashatel.me/product/460', 'https://mashatel.me/product/461', 'https://mashatel.me/product/403', 'https://mashatel.me/product/416', 'https://mashatel.me/product/377', 'https://mashatel.me/product/365', 'https://mashatel.me/product/401', 'https://mashatel.me/product/402', 'https://mashatel.me/product/348', 'https://mashatel.me/product/349', 'https://mashatel.me/product/346', 'https://mashatel.me/product/347', 'https://mashatel.me/product/338', 'https://mashatel.me/product/339', 'https://mashatel.me/product/336', 'https://mashatel.me/product/333', 'https://mashatel.me/product/394', 'https://mashatel.me/product/393', 'https://mashatel.me/product/366', 'https://mashatel.me/product/384', 'https://mashatel.me/product/380', 'https://mashatel.me/product/381', 'https://mashatel.me/product/382']
driver.get(urll[0])
sleep(8)
num=2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        ##################
        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None
        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('Diameter (cm) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Diameter (cm) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('Length (cm) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Length (cm) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('Width (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Width (cm) :' in elem.text][0]
        except:
            wegd = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Ideal = [elem.text.replace('Ideal For :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Ideal For :' in elem.text][0]
        except:
            Ideal = None
        try:
            Shape = [elem.text.replace('Shape :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Shape :' in elem.text][0]
        except:
            Shape = None
        try:
            Material = [elem.text.replace('Material :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Material :' in elem.text][0]
        except:
            Material = None
        try:
            Pot_Plate = [elem.text.replace('Pot Plate :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Plate :' in elem.text][0]
        except:
            Pot_Plate = None
        """

        #################################################

        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'الارتفاع (سم) : ' in elem.text][0]
        except:
            high = None

        try:
            Diameter = [elem.text.replace('القطر(سم) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'القطر(سم) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('الطول (سم) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'الطول (سم) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('العرض(سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'العرض(سم) : ' in elem.text][0]
        except:
            wegd = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None
            
        try:
            Ideal = [elem.text.replace('مثالي ل :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مثالي ل :' in elem.text][0]
        except:
            Ideal = None
        try:
            Shape = [elem.text.replace('الشكل :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الشكل :' in elem.text][0]
        except:
            Shape = None
        try:
            Material = [elem.text.replace('المواد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'المواد :' in elem.text][0]
        except:
            Material = None
        try:
            Pot_Plate = [elem.text.replace('قاعدة الوعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'قاعدة الوعاء :' in elem.text][0]
        except:
            Pot_Plate = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Color
        sh[f'G{num}'] = Variety
        sh[f'H{num}'] = code
        sh[f'J{num}'] = high
        sh[f'H{num}'] = Diameter
        sh[f'I{num}'] = loning
        sh[f'J{num}'] = wegd
        sh[f'K{num}'] = Ideal
        sh[f'L{num}'] = Shape
        sh[f'M{num}'] = Material
        sh[f'N{num}'] = Pot_Plate
        sh[f'O{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'P{num}')
        """
        sh[f'Q{num}'] = name
        sh[f'R{num}'] = price
        sh[f'S{num}'] = state
        sh[f'T{num}'] = seller
        sh[f'U{num}'] = Color
        sh[f'V{num}'] = Variety
        sh[f'W{num}'] = high
        sh[f'X{num}'] = Diameter
        sh[f'Y{num}'] = loning
        sh[f'Z{num}'] = wegd
        sh[f'AA{num}'] = Ideal
        sh[f'AB{num}'] = Shape
        sh[f'AC{num}'] = Material
        sh[f'AD{num}'] = Pot_Plate
        sh[f'AE{num}'] = des
        num += 1
        print(num)
    except:
        pass
sheet.save('POTS & VASES.xlsx')
'''
'''
('https://mashatel.me/category/97', 'FLOWERING PLANTS')

urll = ['https://mashatel.me/product/2903', 'https://mashatel.me/product/6541', 'https://mashatel.me/product/12401', 'https://mashatel.me/product/12404', 'https://mashatel.me/product/12405', 'https://mashatel.me/product/12406', 'https://mashatel.me/product/12407', 'https://mashatel.me/product/12409', 'https://mashatel.me/product/12570', 'https://mashatel.me/product/12579', 'https://mashatel.me/product/12587', 'https://mashatel.me/product/12766', 'https://mashatel.me/product/12938', 'https://mashatel.me/product/12940', 'https://mashatel.me/product/12954', 'https://mashatel.me/product/12966', 'https://mashatel.me/product/12457', 'https://mashatel.me/product/13254', 'https://mashatel.me/product/13261', 'https://mashatel.me/product/13263', 'https://mashatel.me/product/13334', 'https://mashatel.me/product/13472', 'https://mashatel.me/product/13601', 'https://mashatel.me/product/13699', 'https://mashatel.me/product/13135', 'https://mashatel.me/product/13497', 'https://mashatel.me/product/13498', 'https://mashatel.me/product/867', 'https://mashatel.me/product/11487', 'https://mashatel.me/product/258', 'https://mashatel.me/product/267', 'https://mashatel.me/product/268', 'https://mashatel.me/product/269', 'https://mashatel.me/product/274', 'https://mashatel.me/product/12469', 'https://mashatel.me/product/12755', 'https://mashatel.me/product/12761', 'https://mashatel.me/product/12931', 'https://mashatel.me/product/12950', 'https://mashatel.me/product/12964', 'https://mashatel.me/product/12982', 'https://mashatel.me/product/12458', 'https://mashatel.me/product/13146', 'https://mashatel.me/product/13164', 'https://mashatel.me/product/13267', 'https://mashatel.me/product/13271', 'https://mashatel.me/product/13313', 'https://mashatel.me/product/2120', 'https://mashatel.me/product/14252', 'https://mashatel.me/product/1674', 'https://mashatel.me/product/6872', 'https://mashatel.me/product/2667', 'https://mashatel.me/product/1069', 'https://mashatel.me/product/1672', 'https://mashatel.me/product/1160', 'https://mashatel.me/product/14053', 'https://mashatel.me/product/6789', 'https://mashatel.me/product/13477', 'https://mashatel.me/product/729', 'https://mashatel.me/product/12562', 'https://mashatel.me/product/12560', 'https://mashatel.me/product/12408', 'https://mashatel.me/product/618', 'https://mashatel.me/product/8728', 'https://mashatel.me/product/11864', 'https://mashatel.me/product/612', 'https://mashatel.me/product/930', 'https://mashatel.me/product/13499', 'https://mashatel.me/product/602', 'https://mashatel.me/product/923', 'https://mashatel.me/product/932', 'https://mashatel.me/product/936', 'https://mashatel.me/product/938', 'https://mashatel.me/product/12410', 'https://mashatel.me/product/6565', 'https://mashatel.me/product/8200', 'https://mashatel.me/product/8194', 'https://mashatel.me/product/8201', 'https://mashatel.me/product/9083', 'https://mashatel.me/product/12475', 'https://mashatel.me/product/6553', 'https://mashatel.me/product/12616', 'https://mashatel.me/product/1676', 'https://mashatel.me/product/742', 'https://mashatel.me/product/607', 'https://mashatel.me/product/12490', 'https://mashatel.me/product/6574', 'https://mashatel.me/product/941', 'https://mashatel.me/product/1675', 'https://mashatel.me/product/12332', 'https://mashatel.me/product/12239', 'https://mashatel.me/product/12217', 'https://mashatel.me/product/6531', 'https://mashatel.me/product/6802', 'https://mashatel.me/product/7892', 'https://mashatel.me/product/7896', 'https://mashatel.me/product/6529', 'https://mashatel.me/product/6530', 'https://mashatel.me/product/6535', 'https://mashatel.me/product/6587', 'https://mashatel.me/product/6589', 'https://mashatel.me/product/6784', 'https://mashatel.me/product/6526', 'https://mashatel.me/product/2904', 'https://mashatel.me/product/1680']
num = 1
driver.get(urll[0])
sleep(8)

"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "بائع رمز المسلسل وعاء"
sh[f'G{num}'] = 'انواع'
sh[f'H{num}'] = 'اللون'
sh[f'I{num}'] = 'مستوى صعوبة النمو'
sh[f'J{num}'] = 'ضوء الشمس'
sh[f'K{num}'] = 'الأسماء الشائعة'
sh[f'L{num}'] = 'سقي النبات'
sh[f'M{num}'] = 'التربة'
sh[f'N{num}'] = 'السماد'
sh[f'O{num}'] = 'النوع'
sh[f'P{num}'] = 'ارتفاع النبات (سم)'
sh[f'Q{num}'] = 'حجم الاناء (سم)'
sh[f'R{num}'] = 'مستوى سام'
sh[f'S{num}'] = "الوصف"
"""
sh[f'U{num}'] = 'name'
sh[f'V{num}'] = 'price'
sh[f'W{num}'] = 'state'
sh[f'X{num}'] = 'seller'
sh[f'Y{num}'] = 'Species'
sh[f'Z{num}'] = 'Color'
sh[f'AA{num}'] = 'Difficulty to Grow'
sh[f'AB{num}'] = 'Sunlight'
sh[f'AC{num}'] = 'Common Names'
sh[f'AD{num}'] = 'Water'
sh[f'AE{num}'] = 'Soil'
sh[f'AF{num}'] = 'Fertilizers'
sh[f'AG{num}'] = 'Genus'
sh[f'AH{num}'] = 'Height'
sh[f'AI{num}'] = 'Size'
sh[f'AJ{num}'] = 'Toxic Level'
sh[f'AK{num}'] = 'des'

num = 2
driver.get(urll[0])
sleep(5)
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None

        try:
            Species = [elem.text.replace('Species :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Species :' in elem.text][0]
        except:
            Species = None
        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None
        try:
            Grow = [elem.text.replace('Difficulty to Grow :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Difficulty to Grow :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('Sunlight :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Sunlight :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('Common Names :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Common Names :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('Water :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Water :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('Soil :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Soil :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('Fertilizers :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Fertilizers :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('Genus :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Genus :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('Height (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Height (cm) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('Pot Size (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Size (cm) :' in elem.text][0]
        except:
            Size = None
        try:
            posnous = [elem.text.replace('Toxic Level :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Toxic Level :' in elem.text][0]
        except:
            posnous=None
        """
        ################################################################################################################
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            Species = [elem.text.replace('انواع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'انواع :' in elem.text][0]
        except:
            Species = None
        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            Grow = [elem.text.replace('مستوى صعوبة النمو :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى صعوبة النمو :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('ضوء الشمس :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ضوء الشمس :' in elem.text][0]
        except:
            Sunlight = None
        try:
            Common = [elem.text.replace('الأسماء الشائعة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الأسماء الشائعة :' in elem.text][0]
        except:
            Common = None
        try:
            Water = [elem.text.replace('سقي النبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'سقي النبات :' in elem.text][0]
        except:
            Water = None
        try:
            Soil = [elem.text.replace('التربة :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'التربة :' in elem.text][0]
        except:
            Soil = None
        try:
            Fertilizers = [elem.text.replace('السماد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'السماد :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Genus = [elem.text.replace('النوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'النوع :' in elem.text][0]
        except:
            Genus = None
        try:
            Height = [elem.text.replace('الارتفاع (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الارتفاع (سم) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('حجم الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'حجم الاناء (سم) :' in elem.text][0]
        except:
            Size = None

        try:
            posnous = [elem.text.replace('مستوى سام :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى سام :' in elem.text][0]
        except:
            posnous=None
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = code
        sh[f'G{num}'] = Species
        sh[f'H{num}'] = Color
        sh[f'I{num}'] = Grow
        sh[f'J{num}'] = Sunlight
        sh[f'K{num}'] = Common
        sh[f'L{num}'] = Water
        sh[f'M{num}'] = Soil
        sh[f'N{num}'] = Fertilizers
        sh[f'O{num}'] = Genus
        sh[f'P{num}'] = Height
        sh[f'Q{num}'] = Size
        sh[f'R{num}'] = posnous
        sh[f'S{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'T{num}')

        """
        sh[f'U{num}'] = name
        sh[f'V{num}'] = price
        sh[f'W{num}'] = state
        sh[f'X{num}'] = seller
        sh[f'Y{num}'] = Species
        sh[f'Z{num}'] = Color
        sh[f'AA{num}'] = Grow
        sh[f'AB{num}'] = Sunlight
        sh[f'AC{num}'] = Common
        sh[f'AD{num}'] = Water
        sh[f'AE{num}'] = Soil
        sh[f'AF{num}'] = Fertilizers
        sh[f'AG{num}'] = Genus
        sh[f'AH{num}'] = Height
        sh[f'AI{num}'] = Size
        sh[f'AJ{num}'] = posnous
        sh[f'AK{num}'] = des

        num += 1
        print(num)
    except:
        pass
sheet.save('FLOWERING PLANTS.xlsx')
'''
'''
('https://mashatel.me/category/56', 'ARTIFICIAL PLANTS')

urll = ['https://mashatel.me/product/12546', 'https://mashatel.me/product/12550', 'https://mashatel.me/product/1434', 'https://mashatel.me/product/1450', 'https://mashatel.me/product/1460', 'https://mashatel.me/product/1486', 'https://mashatel.me/product/2413', 'https://mashatel.me/product/2414', 'https://mashatel.me/product/2518', 'https://mashatel.me/product/2521', 'https://mashatel.me/product/2529', 'https://mashatel.me/product/2544', 'https://mashatel.me/product/2545', 'https://mashatel.me/product/2549', 'https://mashatel.me/product/2551', 'https://mashatel.me/product/8073', 'https://mashatel.me/product/8962', 'https://mashatel.me/product/8968', 'https://mashatel.me/product/8980', 'https://mashatel.me/product/1466', 'https://mashatel.me/product/1476', 'https://mashatel.me/product/1480', 'https://mashatel.me/product/1490', 'https://mashatel.me/product/8967', 'https://mashatel.me/product/8969', 'https://mashatel.me/product/2548', 'https://mashatel.me/product/1446', 'https://mashatel.me/product/1448', 'https://mashatel.me/product/1455', 'https://mashatel.me/product/1456', 'https://mashatel.me/product/1467', 'https://mashatel.me/product/1471', 'https://mashatel.me/product/1488', 'https://mashatel.me/product/1492', 'https://mashatel.me/product/8964', 'https://mashatel.me/product/8965', 'https://mashatel.me/product/8966', 'https://mashatel.me/product/8970', 'https://mashatel.me/product/8972', 'https://mashatel.me/product/8971', 'https://mashatel.me/product/8976', 'https://mashatel.me/product/8977', 'https://mashatel.me/product/2534', 'https://mashatel.me/product/2535', 'https://mashatel.me/product/2530', 'https://mashatel.me/product/12970', 'https://mashatel.me/product/12988', 'https://mashatel.me/product/12990', 'https://mashatel.me/product/12992', 'https://mashatel.me/product/2550', 'https://mashatel.me/product/2520', 'https://mashatel.me/product/2412', 'https://mashatel.me/product/2532', 'https://mashatel.me/product/2531', 'https://mashatel.me/product/8982', 'https://mashatel.me/product/8981', 'https://mashatel.me/product/8973', 'https://mashatel.me/product/8979', 'https://mashatel.me/product/8978', 'https://mashatel.me/product/1478']
num = 1
"""
sh[f'B{num}'] = "الاسم"
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "اللون"
sh[f'G{num}'] = "تنوع"
sh[f'H{num}'] = "بائع رمز المسلسل وعاء"
sh[f'I{num}'] = "الارتفاع"
sh[f'J{num}'] = "القطر"
sh[f'K{num}'] = "الوصف"
"""
sh[f'M{num}'] = 'name'
sh[f'N{num}'] = 'price'
sh[f'O{num}'] = 'state'
sh[f'P{num}'] = 'seller'
sh[f'Q{num}'] = 'Color'
sh[f'R{num}'] = 'Variety'
sh[f'S{num}'] = 'high'
sh[f'T{num}'] = 'Diameter'
sh[f'U{num}'] = 'des'


driver.get(urll[0])
sleep(8)
num=2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        ##################

        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None
        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            try:
                high = [elem.text.replace('Plant Height (cm) :', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Plant Height (cm) :' in elem.text][0]
            except:
                high = None
        try:
            Diameter = [elem.text.replace('Diameter (cm) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Diameter (cm) : ' in elem.text][0]
        except:
            Diameter = None

        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None

        """
        #################################################

        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'الارتفاع (سم) : ' in elem.text][0]
        except:
            try:
                high = [elem.text.replace('ارتفاع النبات (سم) :', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'ارتفاع النبات (سم) :' in elem.text][0]
            except:
                high = None

        try:
            Diameter = [elem.text.replace('القطر(سم) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'القطر(سم) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Color
        sh[f'G{num}'] = Variety
        sh[f'H{num}'] = code
        sh[f'I{num}'] = high
        sh[f'J{num}'] = Diameter
        sh[f'K{num}'] = des


        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'L{num}')
        """
        sh[f'M{num}'] = name
        sh[f'N{num}'] = price
        sh[f'O{num}'] = state
        sh[f'P{num}'] = seller
        sh[f'Q{num}'] = Color
        sh[f'R{num}'] = Variety
        sh[f'S{num}'] = high
        sh[f'T{num}'] = Diameter
        sh[f'U{num}'] = des

        num += 1
        print(num)
    except:
        pass
sheet.save('ARTIFICIAL PLANTS.xlsx')

'''
'''
('https://mashatel.me/category/93', 'OFFICE PLANTS')
urll = ['https://mashatel.me/product/11615', 'https://mashatel.me/product/12393', 'https://mashatel.me/product/12394', 'https://mashatel.me/product/12395', 'https://mashatel.me/product/12396', 'https://mashatel.me/product/12397', 'https://mashatel.me/product/691', 'https://mashatel.me/product/10080', 'https://mashatel.me/product/10094', 'https://mashatel.me/product/10098', 'https://mashatel.me/product/10106', 'https://mashatel.me/product/10140', 'https://mashatel.me/product/10154', 'https://mashatel.me/product/10156', 'https://mashatel.me/product/10092', 'https://mashatel.me/product/10138', 'https://mashatel.me/product/10128', 'https://mashatel.me/product/10118', 'https://mashatel.me/product/12033', 'https://mashatel.me/product/12158', 'https://mashatel.me/product/12125', 'https://mashatel.me/product/9616', 'https://mashatel.me/product/9614', 'https://mashatel.me/product/12398', 'https://mashatel.me/product/13478', 'https://mashatel.me/product/12400', 'https://mashatel.me/product/12860', 'https://mashatel.me/product/12858', 'https://mashatel.me/product/12854', 'https://mashatel.me/product/10071', 'https://mashatel.me/product/10102', 'https://mashatel.me/product/2561', 'https://mashatel.me/product/1706', 'https://mashatel.me/product/10126', 'https://mashatel.me/product/10069', 'https://mashatel.me/product/1568', 'https://mashatel.me/product/2237', 'https://mashatel.me/product/10082', 'https://mashatel.me/product/11617', 'https://mashatel.me/product/11613', 'https://mashatel.me/product/11611', 'https://mashatel.me/product/10074', 'https://mashatel.me/product/10086', 'https://mashatel.me/product/10122', 'https://mashatel.me/product/10130', 'https://mashatel.me/product/10132', 'https://mashatel.me/product/10134', 'https://mashatel.me/product/10136', 'https://mashatel.me/product/10142', 'https://mashatel.me/product/10144', 'https://mashatel.me/product/10148', 'https://mashatel.me/product/10078', 'https://mashatel.me/product/9604', 'https://mashatel.me/product/2554', 'https://mashatel.me/product/2556', 'https://mashatel.me/product/1553', 'https://mashatel.me/product/692']
num = 1
driver.get(urll[0])
sleep(8)


"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = 'تنوع'
sh[f'G{num}'] = 'انواع'
sh[f'H{num}'] = "المواد"
sh[f'I{num}'] = 'مستوى صعوبة النمو'
sh[f'J{num}'] = 'ضوء الشمس'
sh[f'K{num}'] = 'سقي النبات'
sh[f'L{num}'] = 'السماد'
sh[f'M{num}'] = "ارتفاع الاناء"
sh[f'N{num}'] = 'حجم الاناء (سم)'
sh[f'O{num}'] = "الوصف"
"""

"""
sh[f'Q{num}'] = 'name'
sh[f'R{num}'] = 'price'
sh[f'S{num}'] = 'seller'
sh[f'T{num}'] = 'Species'
sh[f'U{num}'] = 'Variety'
sh[f'V{num}'] = 'Grow'
sh[f'W{num}'] = 'Sunlight'
sh[f'X{num}'] = 'Water'
sh[f'Y{num}'] = 'Fertilizers'
sh[f'Z{num}'] = 'Height'
sh[f'AA{num}'] = 'Size'
sh[f'AB{num}'] = 'Material'
sh[f'AC{num}'] = 'state'
sh[f'AD{num}'] = 'des'
"""
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        ########################
        """
        try:
            Species = [elem.text.replace('Species :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Species :' in elem.text][0]
        except:
            Species = None

        try:
            Grow = [elem.text.replace('Difficulty to Grow :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Difficulty to Grow :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('Sunlight :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Sunlight :' in elem.text][0]
        except:
            Sunlight = None

        try:
            Water = [elem.text.replace('Water :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Water :' in elem.text][0]
        except:
            Water = None

        try:
            Fertilizers = [elem.text.replace('Fertilizers :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Fertilizers :' in elem.text][0]
        except:
            Fertilizers = None
        try:
            Height = [elem.text.replace('Pot Height (cms) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Height (cms) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('Pot Size (cm) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Pot Size (cm) :' in elem.text][0]
        except:
            Size = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Material = [elem.text.replace('Material :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Material :' in elem.text][0]
        except:
            Material = None

        """
        ###############################################################################################################

        """try:
            Species = [elem.text.replace('انواع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'انواع :' in elem.text][0]
        except:
            Species = None
        try:
            Grow = [elem.text.replace('مستوى صعوبة النمو :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مستوى صعوبة النمو :' in elem.text][0]
        except:
            Grow = None
        try:
            Sunlight = [elem.text.replace('ضوء الشمس :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ضوء الشمس :' in elem.text][0]
        except:
            Sunlight = None

        try:
            Water = [elem.text.replace('سقي النبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'سقي النبات :' in elem.text][0]
        except:
            Water = None

        try:
            Fertilizers = [elem.text.replace('السماد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'السماد :' in elem.text][0]
        except:
            Fertilizers = None

        try:
            Height = [elem.text.replace('ارتفاع الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'ارتفاع الاناء (سم) :' in elem.text][0]
        except:
            Height = None
        try:
            Size = [elem.text.replace('حجم الاناء (سم) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'حجم الاناء (سم) :' in elem.text][0]
        except:
            Size = None

        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None
        try:
            Material = [elem.text.replace('المواد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'المواد :' in elem.text][0]
        except:
            Material = None"""

        """sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Variety
        sh[f'G{num}'] = Species
        sh[f'H{num}'] = Material
        sh[f'I{num}'] = Grow
        sh[f'J{num}'] = Sunlight
        sh[f'K{num}'] = Water
        sh[f'L{num}'] = Fertilizers
        sh[f'M{num}'] = Height
        sh[f'N{num}'] = Size
        sh[f'O{num}'] = des"""
        print(num, main_url)
        res = s.get(main_url)
        """image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'P{num}')"""

        with open(f"phot\\{name}.jpg", 'wb') as f:
            f.write(res.content)



        """
        sh[f'Q{num}'] = name
        sh[f'R{num}'] = price
        sh[f'S{num}'] = seller
        sh[f'T{num}'] = Species
        sh[f'U{num}'] = Variety
        sh[f'V{num}'] = Grow
        sh[f'W{num}'] = Sunlight
        sh[f'X{num}'] = Water
        sh[f'Y{num}'] = Fertilizers
        sh[f'Z{num}'] = Height
        sh[f'AA{num}'] = Size
        sh[f'AB{num}'] = Material
        sh[f'AC{num}'] = state
        sh[f'AD{num}'] = des"""
        num += 1

    except Exception as e:
        print(e)

#sheet.save(path)
'''
'''
('https://mashatel.me/category/32', 'GARDENING ACCESSORIES')

urll = ['https://mashatel.me/product/892', 'https://mashatel.me/product/9171', 'https://mashatel.me/product/10051', 'https://mashatel.me/product/10063', 'https://mashatel.me/product/10065', 'https://mashatel.me/product/10049', 'https://mashatel.me/product/891', 'https://mashatel.me/product/1100', 'https://mashatel.me/product/1198', 'https://mashatel.me/product/13995', 'https://mashatel.me/product/13991', 'https://mashatel.me/product/13993', 'https://mashatel.me/product/13989', 'https://mashatel.me/product/13894', 'https://mashatel.me/product/13892', 'https://mashatel.me/product/9175', 'https://mashatel.me/product/11974', 'https://mashatel.me/product/2618', 'https://mashatel.me/product/12168', 'https://mashatel.me/product/12166', 'https://mashatel.me/product/11932', 'https://mashatel.me/product/2650', 'https://mashatel.me/product/2651']
num =1
driver.get(urll[0])
sleep(8)

"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "بائع رمز المسلسل وعاء"
sh[f'G{num}'] = "المواد"
sh[f'H{num}'] = 'اللون'
sh[f'I{num}'] = 'الوصف'

"""
sh[f'K{num}'] = 'name'
sh[f'L{num}'] = 'price'
sh[f'M{num}'] = 'state'
sh[f'N{num}'] = 'seller'
sh[f'O{num}'] = 'Material'
sh[f'P{num}'] = 'Color'
sh[f'Q{num}'] = 'des'

num = 2
driver.get(urll[0])
sleep(5)
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None


        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None

        try:
            Material = [elem.text.replace('Material :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Material :' in elem.text][0]
        except:
            Material = None

        ################################################################################################################
        """try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            Material = [elem.text.replace('المواد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'المواد :' in elem.text][0]
        except:
            Material = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = code
        sh[f'G{num}'] = Material
        sh[f'H{num}'] = Color
        sh[f'I{num}'] = des

        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'J{num}')"""

        sh[f'K{num}'] = name
        sh[f'L{num}'] = price
        sh[f'M{num}'] = state
        sh[f'N{num}'] = seller
        sh[f'O{num}'] = Material
        sh[f'P{num}'] = Color
        sh[f'Q{num}'] = des

        num += 1
        print(num)
    except:
        pass
sheet.save(path)
'''
'''
('https://mashatel.me/category/83', 'SOIL FERTILIZER PESTICIDE')

urll = ['https://mashatel.me/product/12619', 'https://mashatel.me/product/12461', 'https://mashatel.me/product/13423', 'https://mashatel.me/product/13424', 'https://mashatel.me/product/13427', 'https://mashatel.me/product/14003', 'https://mashatel.me/product/533', 'https://mashatel.me/product/535', 'https://mashatel.me/product/826', 'https://mashatel.me/product/827', 'https://mashatel.me/product/828', 'https://mashatel.me/product/831', 'https://mashatel.me/product/833', 'https://mashatel.me/product/835', 'https://mashatel.me/product/836', 'https://mashatel.me/product/837', 'https://mashatel.me/product/839', 'https://mashatel.me/product/843', 'https://mashatel.me/product/1226', 'https://mashatel.me/product/6533', 'https://mashatel.me/product/6559', 'https://mashatel.me/product/6561', 'https://mashatel.me/product/6778', 'https://mashatel.me/product/6780', 'https://mashatel.me/product/9867', 'https://mashatel.me/product/10045', 'https://mashatel.me/product/10046', 'https://mashatel.me/product/10047', 'https://mashatel.me/product/10048', 'https://mashatel.me/product/1862', 'https://mashatel.me/product/13692', 'https://mashatel.me/product/6511', 'https://mashatel.me/product/840', 'https://mashatel.me/product/6519', 'https://mashatel.me/product/13422', 'https://mashatel.me/product/1229', 'https://mashatel.me/product/6543', 'https://mashatel.me/product/8192']
num = 1
driver.get(urll[0])
sleep(10)
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = 'السعر'
sh[f'D{num}'] = 'الحالة'
sh[f'E{num}'] = 'البائع'
sh[f'F{num}'] = 'جيد ل'
sh[f'G{num}'] = 'الحجم'
sh[f'H{num}'] = 'الوزن'
sh[f'I{num}'] = 'بائع رمز المسلسل وعاء'
sh[f'J{num}'] = 'الوصف'
#######################
"""
sh[f'L{num}'] = 'name'
sh[f'M{num}'] = 'price'
sh[f'N{num}'] = 'state'
sh[f'O{num}'] = 'seller'
sh[f'P{num}'] = 'good'
sh[f'Q{num}'] = 'Volume'
sh[f'R{num}'] = 'wieght'
sh[f'S{num}'] = 'des'

num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None

        try:
            Good = [elem.text.replace('Good For :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Good For :' in elem.text][
                0]
        except:
            Good = None
        try:
            Weight = [elem.text.replace('Weight(Kg) : ', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Weight(Kg) : ' in elem.text][0]
        except:
            Weight = None
        try:
            Volume = [elem.text.replace('Volume (Litre) : ', '').replace('Volume (Litre) :', '').strip() for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Volume (Litre) : ' in elem.text or 'Volume (Litre) :' in elem.text][0]
        except:
            Volume = None

        """
        #################################################

        try:
            Good = [elem.text.replace('جيدة لـ : ', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'جيدة لـ : ' in elem.text][0]
        except:
            Good = None
        try:
            Volumear = [elem.text.replace('الحجم (لتر) : ', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'الحجم (لتر) : ' in elem.text][0]
        except:
            Volumear = None
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء : ', '').strip() for elem in
                         driver.find_elements_by_css_selector('div.single-product-tables > div') if
                         'بائع رمز المسلسل وعاء : ' in elem.text][0]
        except:
            code = None
        try:
            Weight = [elem.text.replace('الوزن (كغ) : ', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الوزن (كغ) : ' in elem.text][0]
        except:
            Weight = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Good
        sh[f'G{num}'] = Volumear
        sh[f'H{num}'] = Weight
        sh[f'I{num}'] = code
        sh[f'J{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'K{num}')
        """
        sh[f'L{num}'] = name
        sh[f'M{num}'] = price
        sh[f'N{num}'] = state
        sh[f'O{num}'] = seller
        sh[f'P{num}'] = Good
        sh[f'Q{num}'] = Volume
        sh[f'R{num}'] = Weight
        sh[f'S{num}'] = des

        num += 1
        print(num)
    except Exception as e:
        print(e)

sheet.save(path)
'''
'''
('https://mashatel.me/category/125', 'MEASURING INSTRUMENTS')

urll = ['https://mashatel.me/product/2769', 'https://mashatel.me/product/2759', 'https://mashatel.me/product/2777', 'https://mashatel.me/product/2783', 'https://mashatel.me/product/2785', 'https://mashatel.me/product/2797', 'https://mashatel.me/product/2799', 'https://mashatel.me/product/2801', 'https://mashatel.me/product/10039', 'https://mashatel.me/product/12282', 'https://mashatel.me/product/14018', 'https://mashatel.me/product/12277', 'https://mashatel.me/product/13710', 'https://mashatel.me/product/12281', 'https://mashatel.me/product/12298', 'https://mashatel.me/product/12297', 'https://mashatel.me/product/12276', 'https://mashatel.me/product/12280', 'https://mashatel.me/product/12279', 'https://mashatel.me/product/10041', 'https://mashatel.me/product/10042', 'https://mashatel.me/product/10035', 'https://mashatel.me/product/10036', 'https://mashatel.me/product/10033']

num = 1
"""
sh[f'B{num}'] = "الاسم"
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "اللون"
sh[f'G{num}'] = "الارتفاع"
sh[f'H{num}'] = "الوصف"
"""
sh[f'J{num}'] = 'name'
sh[f'K{num}'] = 'price'
sh[f'L{num}'] = 'state'
sh[f'M{num}'] = 'seller'
sh[f'N{num}'] = 'Color'
sh[f'O{num}'] = 'High'
sh[f'P{num}'] = 'des'

driver.get(urll[0])
sleep(8)
num=2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        ##################


        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None
        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            high = None
        """
        #################################################

        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'الارتفاع (سم) : ' in elem.text][0]
        except:
            high = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Color
        sh[f'G{num}'] = high
        sh[f'H{num}'] = des

        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'I{num}')
        """
        sh[f'J{num}'] = name
        sh[f'K{num}'] = price
        sh[f'L{num}'] = state
        sh[f'M{num}'] = seller
        sh[f'N{num}'] = Color
        sh[f'O{num}'] = high
        sh[f'P{num}'] = des

        num += 1
        print(num)
    except:
        pass
sheet.save(path)

'''
'''
('https://mashatel.me/category/82', 'SEEDS')

urll = ['https://mashatel.me/product/1274', 'https://mashatel.me/product/14320', 'https://mashatel.me/product/510', 'https://mashatel.me/product/1097', 'https://mashatel.me/product/1098', 'https://mashatel.me/product/1191', 'https://mashatel.me/product/1288', 'https://mashatel.me/product/2663', 'https://mashatel.me/product/9657', 'https://mashatel.me/product/9672', 'https://mashatel.me/product/9676', 'https://mashatel.me/product/9684', 'https://mashatel.me/product/9692', 'https://mashatel.me/product/9694', 'https://mashatel.me/product/9704', 'https://mashatel.me/product/9774', 'https://mashatel.me/product/9779', 'https://mashatel.me/product/9781', 'https://mashatel.me/product/9782', 'https://mashatel.me/product/9783', 'https://mashatel.me/product/9788', 'https://mashatel.me/product/9790', 'https://mashatel.me/product/9791', 'https://mashatel.me/product/9795', 'https://mashatel.me/product/1285', 'https://mashatel.me/product/13836', 'https://mashatel.me/product/13858', 'https://mashatel.me/product/13854', 'https://mashatel.me/product/13864', 'https://mashatel.me/product/13872', 'https://mashatel.me/product/13874', 'https://mashatel.me/product/13878', 'https://mashatel.me/product/13880', 'https://mashatel.me/product/13884', 'https://mashatel.me/product/1286', 'https://mashatel.me/product/1268', 'https://mashatel.me/product/9666', 'https://mashatel.me/product/9792', 'https://mashatel.me/product/1563', 'https://mashatel.me/product/1192']
num = 1
driver.get(urll[0])
sleep(10)
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = 'السعر'
sh[f'D{num}'] = 'الحالة'
sh[f'E{num}'] = 'البائع'
sh[f'F{num}'] = 'نسبة النقاء'
sh[f'G{num}'] = 'الحجم'
sh[f'H{num}'] = 'الوزن'
sh[f'I{num}'] = 'بائع رمز المسلسل وعاء'
sh[f'J{num}'] = 'نسبة الانبات'
sh[f'K{num}'] = 'الوصف'

"""
sh[f'M{num}'] = 'name'
sh[f'N{num}'] = 'price'
sh[f'O{num}'] = 'state'
sh[f'P{num}'] = 'seller'
sh[f'Q{num}'] = 'Physical'
sh[f'R{num}'] = 'Volume'
sh[f'S{num}'] = 'wieght'
sh[f'T{num}'] = 'Germination'
sh[f'U{num}'] = 'des'

num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None

        try:
            Physical = [elem.text.replace('Physical Purity (%) :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Physical Purity (%) :' in elem.text][
                0]
        except:
            Physical = None
        try:
            Germination = [elem.text.replace('Germination Percentage (%) :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Germination Percentage (%) :' in elem.text][
                0]
        except:
            Germination = None
        try:
            Weight = [elem.text.replace('Weight (gm) :', '').replace('Weight(Kg) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Weight (gm) :' in elem.text or 'Weight(Kg) :' in elem.text][0]
        except:
            Weight = None
        try:
            Volume = [elem.text.replace('Volume (ml) :', '').replace('Volume (Litre) :', '').strip() for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Volume (ml) :' in elem.text or 'Volume (Litre) :' in elem.text][0]
        except:
            Volume = None

        """
        #################################################

        try:
            Germination = [elem.text.replace('نسبة الانبات :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'نسبة الانبات :' in elem.text][0]
        except:
            Germination = None
        try:
            Physical = [elem.text.replace('نسبة النقاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'نسبة النقاء :' in elem.text][0]
        except:
            Physical = None

        try:
            Volumear = [elem.text.replace('الحجم(مل) :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'الحجم(مل) :' in elem.text][0]
        except:
            Volumear = None

        try:
            Weight = [elem.text.replace('الوزن (كغ) :', '').replace('الوزن(غ) :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الوزن (كغ) :' in elem.text or 'الوزن(غ) :' in elem.text][0]
        except:
            Weight = None

        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Physical
        sh[f'G{num}'] = Volumear
        sh[f'H{num}'] = Weight
        sh[f'I{num}'] = code
        sh[f'J{num}'] = Germination
        sh[f'K{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'L{num}')
        """
        sh[f'M{num}'] = name
        sh[f'N{num}'] = price
        sh[f'O{num}'] = state
        sh[f'P{num}'] = seller
        sh[f'Q{num}'] = Physical
        sh[f'R{num}'] = Volume
        sh[f'S{num}'] = Weight
        sh[f'T{num}'] = Germination
        sh[f'U{num}'] = des

        num += 1
        print(num)
    except Exception as e:
        print(e)

sheet.save(path)
'''
'''
('https://mashatel.me/category/92', 'HYDROPONIC SYSTEM')

urll = ['https://mashatel.me/product/541', 'https://mashatel.me/product/2723', 'https://mashatel.me/product/2809', 'https://mashatel.me/product/2850', 'https://mashatel.me/product/637', 'https://mashatel.me/product/2808', 'https://mashatel.me/product/633', 'https://mashatel.me/product/634', 'https://mashatel.me/product/636', 'https://mashatel.me/product/628', 'https://mashatel.me/product/638', 'https://mashatel.me/product/2852', 'https://mashatel.me/product/2854']
num =1
driver.get(urll[0])
sleep(8)

"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "بائع رمز المسلسل وعاء"
sh[f'G{num}'] = "المواد"
sh[f'H{num}'] = 'الارتفاع'
sh[f'I{num}'] = 'القطر'
sh[f'J{num}'] = "الطول"
sh[f'K{num}'] = "العرض"
sh[f'L{num}'] = "الحجم"
sh[f'M{num}'] = "الوزن"
sh[f'N{num}'] = "الوصف"
"""
sh[f'P{num}'] = 'name'
sh[f'Q{num}'] = 'price'
sh[f'R{num}'] = 'seller'
sh[f'S{num}'] = 'Material'
sh[f'T{num}'] = 'high'
sh[f'V{num}'] = 'Diameter'
sh[f'W{num}'] = 'loning'
sh[f'X{num}'] = 'wegd'
sh[f'Z{num}'] = 'Volume'
sh[f'AA{num}'] = 'Weight'
sh[f'AB{num}'] = 'state'
sh[f'AC{num}'] = 'des'



num = 2
driver.get(urll[0])
sleep(5)
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None

        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None



        try:
            Material = [elem.text.replace('Material :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Material :' in elem.text][0]
        except:
            Material = None

        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('Diameter (cm) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Diameter (cm) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('Length (cm) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Length (cm) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('Width (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Width (cm) : ' in elem.text][0]
        except:
            wegd = None

        try:
            Weight = [elem.text.replace('Weight (gm) :', '').replace('Weight(Kg) :', '').strip() for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Weight (gm) :' in elem.text or 'Weight(Kg) :' in elem.text][0]
        except:
            Weight = None
        try:
            Volume = [elem.text.replace('Volume (ml) :', '').replace('Volume (Litre) :', '').strip() for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Volume (ml) :' in elem.text or 'Volume (Litre) :' in elem.text][0]
        except:
            Volume = None
        """

        ################################################################################################################
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None

        try:
            Material = [elem.text.replace('المواد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'المواد :' in elem.text][0]
        except:
            Material = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                driver.find_elements_by_css_selector('div.single-product-tables > div') if
                'الارتفاع (سم) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('القطر(سم) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'القطر(سم) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('الطول (سم) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'الطول (سم) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('العرض(سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'العرض(سم) : ' in elem.text][0]
        except:
            wegd = None

        try:
            Volumear = [elem.text.replace('الحجم (لتر) :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'الحجم (لتر) :' in elem.text][0]
        except:
            Volumear = None

        try:
            Weight = [elem.text.replace('الوزن (كغ) :', '').replace('الوزن(غ) :', '').strip() for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'الوزن (كغ) :' in elem.text or 'الوزن(غ) :' in elem.text][0]
        except:
            Weight = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = code
        sh[f'G{num}'] = Material
        sh[f'H{num}'] = high
        sh[f'I{num}'] = Diameter
        sh[f'J{num}'] = loning
        sh[f'K{num}'] = wegd
        sh[f'L{num}'] = Volumear
        sh[f'M{num}'] = Weight
        sh[f'N{num}'] = des

        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'O{num}')
        """

        sh[f'P{num}'] = name
        sh[f'Q{num}'] = price
        sh[f'R{num}'] = seller
        sh[f'S{num}'] = Material
        sh[f'T{num}'] = high
        sh[f'V{num}'] = Diameter
        sh[f'W{num}'] = loning
        sh[f'X{num}'] = wegd
        sh[f'Z{num}'] = Volume
        sh[f'AA{num}'] = Weight
        sh[f'AB{num}'] = state
        sh[f'AC{num}'] = des


        num += 1
        print(num)
    except:
        pass
sheet.save(path)

'''
'''
('https://mashatel.me/category/55', 'GARDEN DECORATION')

urll = ['https://mashatel.me/product/12552', 'https://mashatel.me/product/12558', 'https://mashatel.me/product/12620', 'https://mashatel.me/product/12622', 'https://mashatel.me/product/13111', 'https://mashatel.me/product/516', 'https://mashatel.me/product/517', 'https://mashatel.me/product/7628', 'https://mashatel.me/product/427', 'https://mashatel.me/product/14188', 'https://mashatel.me/product/14187', 'https://mashatel.me/product/12650', 'https://mashatel.me/product/428', 'https://mashatel.me/product/429', 'https://mashatel.me/product/430', 'https://mashatel.me/product/7629', 'https://mashatel.me/product/7630', 'https://mashatel.me/product/7631', 'https://mashatel.me/product/7632', 'https://mashatel.me/product/7633', 'https://mashatel.me/product/12649', 'https://mashatel.me/product/12652', 'https://mashatel.me/product/12654', 'https://mashatel.me/product/12653', 'https://mashatel.me/product/12651', 'https://mashatel.me/product/12554']

num = 1
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "اللون"
sh[f'G{num}'] = 'تنوع'
sh[f'H{num}'] = "بائع رمز المسلسل وعاء"
sh[f'J{num}'] = "الارتفاع"
sh[f'H{num}'] = "القطر"
sh[f'I{num}'] = "الطول"
sh[f'J{num}'] = "العرض"
sh[f'K{num}'] = "مثال ل"
sh[f'L{num}'] = "الشكل"
sh[f'M{num}'] = "المواد"
sh[f'N{num}'] = "القاعده"
sh[f'O{num}'] = "الوصف"
"""
sh[f'Q{num}'] = 'name'
sh[f'R{num}'] = 'price'
sh[f'S{num}'] = 'state'
sh[f'T{num}'] = 'seller'
sh[f'U{num}'] = 'Color'
sh[f'V{num}'] = 'Variety'
sh[f'W{num}'] = 'high'
sh[f'X{num}'] = 'Diameter'
sh[f'Y{num}'] = 'loning'
sh[f'Z{num}'] = 'wegd'
sh[f'AA{num}'] = 'Ideal'
sh[f'AB{num}'] = 'Shape'
sh[f'AC{num}'] = 'Material'
sh[f'AD{num}'] = 'Pot Plate'
sh[f'AE{num}'] = 'des'

driver.get(urll[0])
sleep(8)
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None

        ##################
        try:
            Color = [elem.text.replace('Color :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Color :' in elem.text][
                0]
        except:
            Color = None
        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('Diameter (cm) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Diameter (cm) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('Length (cm) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Length (cm) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('Width (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Width (cm) :' in elem.text][0]
        except:
            wegd = None
        try:
            Variety = [elem.text.replace('Variety :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'Variety :' in elem.text][0]
        except:
            Variety = None
        try:
            Ideal = [elem.text.replace('Ideal For :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'Ideal For :' in elem.text][0]
        except:
            Ideal = None
        try:
            Shape = [elem.text.replace('Shape :', '').strip() for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'Shape :' in elem.text][0]
        except:
            Shape = None
        try:
            Material = [elem.text.replace('Material :', '').strip() for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Material :' in elem.text][0]
        except:
            Material = None
        try:
            Pot_Plate = [elem.text.replace('Pot Plate :', '').strip() for elem in
                         driver.find_elements_by_css_selector('div.single-product-tables > div') if
                         'Pot Plate :' in elem.text][0]
        except:
            Pot_Plate = None

        """
        #################################################

        try:
            Color = [elem.text.replace('اللون :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'اللون :' in elem.text][0]
        except:
            Color = None
        try:
            code = [elem.text.replace('بائع رمز المسلسل وعاء :', '').strip() for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'بائع رمز المسلسل وعاء :' in elem.text][0]
        except:
            code = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'الارتفاع (سم) : ' in elem.text][0]
        except:
            high = None

        try:
            Diameter = [elem.text.replace('القطر(سم) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'القطر(سم) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('الطول (سم) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'الطول (سم) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('العرض(سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'العرض(سم) : ' in elem.text][0]
        except:
            wegd = None
        try:
            Variety = [elem.text.replace('تنوع :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'تنوع :' in elem.text][0]
        except:
            Variety = None

        try:
            Ideal = [elem.text.replace('مثالي ل :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'مثالي ل :' in elem.text][0]
        except:
            Ideal = None
        try:
            Shape = [elem.text.replace('الشكل :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'الشكل :' in elem.text][0]
        except:
            Shape = None
        try:
            Material = [elem.text.replace('المواد :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'المواد :' in elem.text][0]
        except:
            Material = None
        try:
            Pot_Plate = [elem.text.replace('قاعدة الوعاء :', '').strip() for elem in
                       driver.find_elements_by_css_selector('div.single-product-tables > div') if
                       'قاعدة الوعاء :' in elem.text][0]
        except:
            Pot_Plate = None

        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = Color
        sh[f'G{num}'] = Variety
        sh[f'H{num}'] = code
        sh[f'J{num}'] = high
        sh[f'H{num}'] = Diameter
        sh[f'I{num}'] = loning
        sh[f'J{num}'] = wegd
        sh[f'K{num}'] = Ideal
        sh[f'L{num}'] = Shape
        sh[f'M{num}'] = Material
        sh[f'N{num}'] = Pot_Plate
        sh[f'O{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'P{num}')
        """
        sh[f'Q{num}'] = name
        sh[f'R{num}'] = price
        sh[f'S{num}'] = state
        sh[f'T{num}'] = seller
        sh[f'U{num}'] = Color
        sh[f'V{num}'] = Variety
        sh[f'W{num}'] = high
        sh[f'X{num}'] = Diameter
        sh[f'Y{num}'] = loning
        sh[f'Z{num}'] = wegd
        sh[f'AA{num}'] = Ideal
        sh[f'AB{num}'] = Shape
        sh[f'AC{num}'] = Material
        sh[f'AD{num}'] = Pot_Plate
        sh[f'AE{num}'] = des

        num += 1
        print(num)
    except:
        pass
sheet.save(path)
'''
'''
('https://mashatel.me/category/128', 'GARDEN FURNITURE')

urll = ['https://mashatel.me/product/13442', 'https://mashatel.me/product/7636', 'https://mashatel.me/product/7878', 'https://mashatel.me/product/7942', 'https://mashatel.me/product/1532', 'https://mashatel.me/product/8365', 'https://mashatel.me/product/8364', 'https://mashatel.me/product/8074', 'https://mashatel.me/product/8369', 'https://mashatel.me/product/8373', 'https://mashatel.me/product/8366', 'https://mashatel.me/product/8368', 'https://mashatel.me/product/8370', 'https://mashatel.me/product/1531', 'https://mashatel.me/product/1533', 'https://mashatel.me/product/1534', 'https://mashatel.me/product/8376', 'https://mashatel.me/product/8374', 'https://mashatel.me/product/8375']

num = 1
"""
sh[f'B{num}'] = 'الاسم'
sh[f'C{num}'] = "السعر"
sh[f'D{num}'] = "الحالة"
sh[f'E{num}'] = "البائع"
sh[f'F{num}'] = "العدد"
sh[f'G{num}'] = 'المواد الاوليه'
sh[f'H{num}'] = "المواد الثانوية"
sh[f'J{num}'] = "الارتفاع"
sh[f'H{num}'] = "القطر"
sh[f'I{num}'] = "الطول"
sh[f'J{num}'] = "العرض"
sh[f'K{num}'] = "الكود"
sh[f'L{num}'] = "اللون"
sh[f'M{num}'] = "المساحه"
sh[f'N{num}'] = "الوصف"

"""
sh[f'Q{num}'] = 'name'
sh[f'R{num}'] = 'price'
sh[f'S{num}'] = 'state'
sh[f'T{num}'] = 'seller'
sh[f'U{num}'] = 'number'
sh[f'V{num}'] = 'Material'
sh[f'W{num}'] = 'high'
sh[f'X{num}'] = 'Diameter'
sh[f'Y{num}'] = 'loning'
sh[f'Z{num}'] = 'wegd'
sh[f'AA{num}'] = 'Secondary Material'
sh[f'AB{num}'] = 'code'
sh[f'AC{num}'] = 'color'
sh[f'AD{num}'] = 'area'
sh[f'AE{num}'] = 'des'

driver.get(urll[0])
sleep(8)
num = 2
for u in urll:
    driver.get(u)
    sleep(2)
    try:
        name = driver.find_element_by_css_selector('div.product-right > h2').text
        try:
            price = driver.find_element_by_css_selector('div.product-right > h3').text
        except:
            price = None
        try:
            main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
        except:
            main_url = None
        try:
            state = driver.find_element_by_css_selector('.is').text
        except:
            state = None
        try:
            seller = driver.find_element_by_css_selector('.vendor-name').text
        except:
            seller = None
        try:
            des = driver.find_element_by_css_selector('#top-home').text
        except:
            des = None
        #######################################################################################################
        """try:
            number_arbic = [elem.text.replace('عدد العناصر : ', '') for elem in
                            driver.find_elements_by_css_selector('div.single-product-tables > div') if
                            'عدد العناصر : ' in elem.text][0]
        except:
            number_arbic = None
        try:
            source = [elem.text.replace('المواد الأولية : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'المواد الأولية : ' in elem.text][0]
        except:
            source = None
        try:
            source_2 = [elem.text.replace('المواد الثانوية : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'المواد الثانوية : ' in elem.text][0]
        except:
            source_2 = None
        try:
            color = [elem.text.replace('لون النسيج : ', '') for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'لون النسيج : ' in elem.text][0]
        except:
            color = None
        try:
            high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'الارتفاع (سم) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('القطر(سم) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'القطر(سم) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('الطول (سم) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'الطول (سم) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('العرض(سم) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'العرض(سم) : ' in elem.text][0]
        except:
            wegd = None
        try:
            bar = [elem.text.replace('بائع رمز المسلسل وعاء : ', '') for elem in
                   driver.find_elements_by_css_selector('div.single-product-tables > div') if
                   'بائع رمز المسلسل وعاء : ' in elem.text][0]
        except:
            bar = None

        try:
            area = [elem.text.replace('متر مرب(مساحة) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'متر مرب(مساحة) : ' in elem.text][0]
        except:
            area = None"""
        ##############################################################################################################################################################################
        try:
            number_arbic = [elem.text.replace('Number of Items : ', '') for elem in
                            driver.find_elements_by_css_selector('div.single-product-tables > div') if
                            'Number of Items : ' in elem.text][0]
        except:
            number_arbic = None
        try:
            source = [elem.text.replace('Primary Material : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Primary Material : ' in elem.text][0]
        except:
            source = None
        try:
            source_2 = [elem.text.replace('Secondary Material : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Secondary Material : ' in elem.text][0]
        except:
            source_2 = None
        try:
            color = [elem.text.replace('Fabric Color : ', '') for elem in
                     driver.find_elements_by_css_selector('div.single-product-tables > div') if
                     'Fabric Color : ' in elem.text][0]
        except:
            color = None
        try:
            high = [elem.text.replace('Height (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Height (cm) : ' in elem.text][0]
        except:
            high = None
        try:
            Diameter = [elem.text.replace('Diameter (cm) : ', '') for elem in
                        driver.find_elements_by_css_selector('div.single-product-tables > div') if
                        'Diameter (cm) : ' in elem.text][0]
        except:
            Diameter = None
        try:
            loning = [elem.text.replace('Length (cm) : ', '') for elem in
                      driver.find_elements_by_css_selector('div.single-product-tables > div') if
                      'Length (cm) : ' in elem.text][0]
        except:
            loning = None
        try:
            wegd = [elem.text.replace('Width (cm) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Width (cm) : ' in elem.text][0]
        except:
            wegd = None
        try:
            bar = [elem.text.replace('Vendor Serial Code : ', '') for elem in
                   driver.find_elements_by_css_selector('div.single-product-tables > div') if
                   'Vendor Serial Code : ' in elem.text][0]
        except:
            bar = None
        try:
            area = [elem.text.replace('Area(Sq.m) : ', '') for elem in
                    driver.find_elements_by_css_selector('div.single-product-tables > div') if
                    'Area(Sq.m) : ' in elem.text][0]
        except:
            area = None
        """
        sh[f'B{num}'] = name
        sh[f'C{num}'] = price
        sh[f'D{num}'] = state
        sh[f'E{num}'] = seller
        sh[f'F{num}'] = number_arbic
        sh[f'G{num}'] = source
        sh[f'H{num}'] = source_2
        sh[f'J{num}'] = high
        sh[f'H{num}'] = Diameter
        sh[f'I{num}'] = loning
        sh[f'J{num}'] = wegd
        sh[f'K{num}'] = bar
        sh[f'L{num}'] = color
        sh[f'M{num}'] = area
        sh[f'N{num}'] = des
        res = s.get(main_url)
        image_file = BytesIO(res.content)
        img = Image(image_file)
        img.width = 90
        img.height = 75
        sh.row_dimensions[num].height = 56
        sh.add_image(img, f'P{num}')
        """
        sh[f'Q{num}'] = name
        sh[f'R{num}'] = price
        sh[f'S{num}'] = state
        sh[f'T{num}'] = seller
        sh[f'U{num}'] = number_arbic
        sh[f'V{num}'] = source
        sh[f'W{num}'] = high
        sh[f'X{num}'] = Diameter
        sh[f'Y{num}'] = loning
        sh[f'Z{num}'] = wegd
        sh[f'AA{num}'] = source_2
        sh[f'AB{num}'] = bar
        sh[f'AC{num}'] = color
        sh[f'AD{num}'] = area
        sh[f'AE{num}'] = des

        num += 1
        print(num)
    except Exception as e:
        print(e)
sheet.save(path)



'''

'''
driver.get('https://mashatel.me/category/156')
sleep(2)
product_url =  []
while True:
[product_url.append(prod.get_attribute('href')) for prod in
  driver.find_elements_by_css_selector('div.product-detail > div > a') if
  prod.get_attribute('href') not in product_url]
print(len(product_url))
try:
 driver.find_element_by_css_selector('i.fa.fa-chevron-right').click()
 sleep(2)
except Exception as e:
 print(e)
 break


 elements = [ele for ele in driver.find_elements_by_css_selector('ul.pagination > li.page-item') if ele.text.isnumeric()]
 for ele in elements:
     nex = driver.find_element_by_css_selector('ul.pagination > li.page-item.active').text
     if ele.text == elements[-1].text:
         u = False
         break
     elif int(ele.text) == int(nex) + 1:
         try:
             ele.click()
             print('clicked')
             sleep(3)
             break
         except Exception as e:
             print(e)
             u = False
             break

name = driver.find_element_by_css_selector('div.product-right > h2').text
price = driver.find_element_by_css_selector('div.product-right > h3').text
main_url = driver.find_element_by_css_selector('img.image_zoom_cls-0').get_attribute('src')
state = driver.find_element_by_css_selector('.is').text
seller = driver.find_element_by_css_selector('.vendor-name').text

#############################################################################################3
try:
number_arbic = [elem.text.replace('عدد العناصر : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'عدد العناصر : ' in elem.text][0]
except:
number_arbic = None
try:
source = [elem.text.replace('المواد الأولية : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'المواد الأولية : ' in elem.text][0]
except:
source = None
try:
source_2 = [elem.text.replace('المواد الثانوية : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'المواد الثانوية : ' in elem.text][0]
except:
source_2 = None
try:
color = [elem.text.replace('لون النسيج : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'لون النسيج : ' in elem.text][0]
except:
color = None
try:
high = [elem.text.replace('الارتفاع (سم) : ', '') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'الارتفاع (سم) : ' in elem.text][0]
except:
high = None
try:
Diameter = [elem.text.replace('القطر(سم) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'القطر(سم) : ' in elem.text][0]
except:
Diameter = None
try:
loning = [elem.text.replace('الطول (سم) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'الطول (سم) : ' in elem.text][0]
except:
loning = None
try:
wegd = [elem.text.replace('العرض(سم) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'العرض(سم) : ' in elem.text][0]
except:
wegd = None
try:
bar = [elem.text.replace('بائع رمز المسلسل وعاء : ', '') for elem in
    driver.find_elements_by_css_selector('div.single-product-tables > div') if
    'بائع رمز المسلسل وعاء : ' in elem.text][0]
except:
bar = None
try:
des = driver.find_element_by_css_selector('#top-home').text
except:
des = None
try:
area = [elem.text.replace('متر مرب(مساحة) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'متر مرب(مساحة) : ' in elem.text]
except:
area = None
##############################################################################################################################################################################
try:
number_arbic = [elem.text.replace('Number of Items : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Number of Items : ' in elem.text][0]
except:
number_arbic = None
try:
source = [elem.text.replace('Primary Material : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Primary Material : ' in elem.text][0]
except:
source = None
try:
source_2 = [elem.text.replace('Secondary Material : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Secondary Material : ' in elem.text][0]
except:
source_2 = None
try:
color = [elem.text.replace('Fabric Color : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Fabric Color : ' in elem.text][0]
except:
color = None
try:
high = [elem.text.replace('Height (cm) : ', '') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Height (cm) : ' in elem.text][0]
except:
high = None
try:
Diameter = [elem.text.replace('Diameter (cm) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Diameter (cm) : ' in elem.text][0]
except:
Diameter = None
try:
loning = [elem.text.replace('Length (cm) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Length (cm) : ' in elem.text][0]
except:
loning = None
try:
wegd = [elem.text.replace('Width (cm) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Width (cm) : ' in elem.text][0]
except:
wegd = None
try:
bar = [elem.text.replace('Vendor Serial Code : ', '') for elem in
    driver.find_elements_by_css_selector('div.single-product-tables > div') if
    'Vendor Serial Code : ' in elem.text][0]
except:
bar = None
try:
area = [elem.text.replace('Area(Sq.m) : ','') for elem in driver.find_elements_by_css_selector('div.single-product-tables > div') if 'Area(Sq.m) : ' in elem.text][0]
except:
area = None
'''

'''
[('https://mashatel.me/category/156', 'DISINFECTANT'), ('https://mashatel.me/category/161', 'PREMIUM COLLECTION'), ('https://mashatel.me/category/26', 'INDOOR PLANTS'),
('https://mashatel.me/category/27', 'OUTDOOR PLANTS'), ('https://mashatel.me/category/130', 'WHOLESALE FLOWERS'), ('https://mashatel.me/category/76', 'POTS & VASES'),
('https://mashatel.me/category/97', 'FLOWERING PLANTS'), ('https://mashatel.me/category/56', 'ARTIFICIAL PLANTS'), ('https://mashatel.me/category/93', 'OFFICE PLANTS'),
('https://mashatel.me/category/32', 'GARDENING ACCESSORIES'), ('https://mashatel.me/category/83', 'SOIL FERTILIZER PESTICIDE'), ('https://mashatel.me/category/125', 'MEASURING INSTRUMENTS'),
('https://mashatel.me/category/82', 'SEEDS'), ('https://mashatel.me/category/92', 'HYDROPONIC SYSTEM'), ('https://mashatel.me/category/55', 'GARDEN DECORATION'),
('https://mashatel.me/category/128', 'GARDEN FURNITURE')]'''