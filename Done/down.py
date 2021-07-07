from msedge.selenium_tools import Edge, EdgeOptions
import re
import requests

options = EdgeOptions()
options.use_chromium = True
#options.add_argument("headless")
options.add_argument("disable-gpu")
# options.add_argument("--user-data-dir=Edge-data")
driver = Edge(options=options)
driver.get('https://www.pexels.com/photo/sky-blue-windy-flag-54097/?fbclid=IwAR3m9NOtj2DGwakkHa9iwRTJ4vk2MM69LxpybI2SuDBcnibi-5bXz4s1jbA')
driver.find_element_by_class_name('js-photo-page-image-download-link')






#'https%3A%2F%2Fnayn.co%2Fwp-content%2Fuploads%2F2019%2F10%2F5bb58adffa65096b3e6469cb_1538624223786.jpg'.replace('%2F','/').replace('%3A',':')




'''
driver.get('https://www.pexels.com/video/a-man-counting-cash-money-and-put-it-into-record-3196002')

u = 'view-source:' + driver.find_element_by_class_name('js-photo-page-video-iframe').get_attribute('src')
driver.get(u)
url = re.findall(
    'https://vod[A-z0-9://?-?]{,}.?[A-z0-9://-]{,}.[A-z0-9://-]{,}.[A-z0-9://?-?=~%-]{,}.[A-z0-9://?-?=~%-]{,}.[A-z0-9://?-?=~%-]*',
    driver.page_source)[-1]
d = requests.get(url)
with open(f'1.{url.split(".")[-1]}', 'wb') as f:
    f.write(d.content)
'''