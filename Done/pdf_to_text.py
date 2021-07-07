# from requests_html import HTMLSession
#
# session = HTMLSession()
#
# for i in range(2, 12+1):
#     page = 1
#     while True:
#         print('id : ', i, 'page : ', page)
#         url = f'https://www.hespress.com/?action=ajax_listing&type=category&id={i}&paged={page}'
#         # url = 'https://www.hespress.com/?action=ajax_listing&type=category&id={}&paged={}'.format(i, page)
#         # url = 'https://www.hespress.com/?action=ajax_listing&type=category&id='+str(i)+'&paged='+str(page)
#         response = session.get(url)
#         page += 1
#         try:
#             n = len(response.html.find('div.card'))
#         except:
#             n = 0
#
#         if n > 0:
#             for card in response.html.find('div.card'):
#                 cat = card.find('span.cat', first=True).text
#                 link = card.find('a.stretched-link', first=True).attrs['href']
#                 img = card.find('img', first=True).attrs['src']
#                 title = card.find('.card-title', first=True).text
#                 date = card.find('.date-card', first=True).text
#                 print(cat, title, date, link, img)
#         else:
#             break


import fitz  # pymupdf, P
from bidi.algorithm import get_display
import pyarabic.araby as arb


def modify(text_modify):
    text_modify = get_display(text_modify).replace('\n', '///')
    text_list = []
    for text_1 in text_modify.split(' '):
        text_1 = text_1.strip()
        if 'اال' in text_1:
            text_1 = text_1.replace('اال', 'الا')
        elif 'األ' in text_1:
            text_1 = text_1.replace('األ', 'الأ')
        elif text_1.strip().find('الل') != 0:
            text_1 = text_1.replace('الل', 'لال')

        text_list.append(text_1)

    return ' '.join(text_list).replace('///', '\n')


file = r'C:\Users\3mora\Downloads\2.pdf'
# file = r'13.5.21.COVID-19.pdf'
with fitz.open(file) as doc:
    text = ""
    for page in doc:
        text += page.getText()
        # print(page.get_text("rawdict"))
    json_ = page.get_text("json")
    print(page.apply_redactions())
    # with open('k.html', 'w') as d:
    #     d.write(page.get_text("xhtml"))
    # for i in ["text", "html", "json", "rawjson", "xhtml", "xml", "dict", "rawdict", "words", "blocks"]:
    #     print(i, page.get_text(i)[:500])
    #     print('-' * 200)
# print(modify(text))
# print(modify(text))

# print(text)

# list_t = text[text.find('ميلاقأو تلاامع ')+15:].strip().split(' \n')
# n = 0
# p = []
# o = []
# for t in range(0, len(list_t)):
#     te = list_t[t].strip().replace("'", "").replace('-', '')
#     if te == '':
#         p.append(list_t[t].strip())
#     elif arb.is_arabicstring(te):
#         if te.isnumeric():
#
#             p.append(list_t[t].strip())
#         else:
#             p.append(list_t[t].strip()[::-1])
#             if len(p) > 4:
#                 p.remove('')
#             o.append(p)
#             p = []
#     else:
#         if te.isnumeric():
#
#             p.append(list_t[t].strip())
#         else:
#             p = []
#             p.append(list_t[t].strip())
# encoding = 'cp1256'
