from requests_html import HTMLSession

s = HTMLSession()
from openpyxl import Workbook

book = Workbook()
sheet = book.active
# 1615619 1615969 1590517
# while True:
#     try:
#         r = s.post("https://www.azhar.eg/DesktopModules/NatigaSecWebService/WebService1.asmx/GetNatiga3ItemWithStringNational", headers={
#             "accept": "application/json, text/javascript, */*; q=0.01",
#             "content-type": "application/json; charset=UTF-8",
#             "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
#             "sec-ch-ua-mobile": "?0"
#         },
#                    data="{'ItemId':30402081204085,'SeatNo':130101}"
#                    )
#         print('- DOne')
#         break
#     except:
#         pass
# import requests
#
# s = requests.session()
n = 2
# for i in range(1659169, 1659372):
for i in range(1009169, 1590608+1)[::-1]:
    r = s.post("http://natega.dostor.org/Home/Result", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Alt-Used": "natega.dostor.org:443",
        "Upgrade-Insecure-Requests": "1"
    },
               data=f"seating_no={i}"
               )
    try:
        # sheet.cell(n, 1).value = i
        # sheet.cell(n, 2).value = r.html.find('#tab-list-active + span')[0].text
        # sheet.cell(n, 3).value = r.html.find('li>h1')[2].text
        # sheet.cell(n, 4).value = r.html.find('.resultItem > #tab + span')[0].text
        # sheet.cell(n, 5).value = r.html.find('.resultItem > #tab + span')[1].text
        # sheet.cell(n, 6).value = r.html.find('.resultItem > #tab + span')[2].text
        # sheet.cell(n, 7).value = r.html.find('.resultItem > #tab + span')[3].text
        # sheet.cell(n, 8).value = r.html.find('.resultItem > #tab + span')[4].text
        # n += 1
        print(r.html.find('#tab-list-active + span')[0].text, [i.text for i in r.html.find('.resultItem > #tab + span')], i)
        # print(r.html.find('.resultItem > #tab + span')[0].text, r.html.find('.resultItem > #tab + span')[2].text, r.html.find('li>h1')[2].text,
        #       r.html.find('#tab-list-active + span')[0].text, i)
    except:
        pass
