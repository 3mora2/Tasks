# from PyPDF2 import PdfFileReader
# from openpyxl import Workbook
# import re
#
# book = Workbook()
# sheet = book.active
# pdf_fil = input('Enter PDF name : ')
# # 'Issue-713_compressed.pdf'
# l = []
# with open(pdf_fil, 'rb') as f:
#     pdf = PdfFileReader(f)
#     information = pdf.getDocumentInfo()
#     number_of_pages = pdf.getNumPages()
#     for page in range(0, number_of_pages):
#         p = pdf.getPage(page).extractText()
#         l += re.findall(r'\d{10,11}', p)
#         print(len(l))
# i = 1
# l = list(set(l))
# print('*********************************************')
# print(len(l))
# for e in l:
#     sheet[f'A{i}'].value = e
#     print(i, ' - ', e)
#     i += 1
# book.save(pdf_fil.replace('.pdf', '.xlsx'))
from openpyxl import Workbook

import re

text = ''
for file in ['المف الاول.txt', 'الملف الثاني.txt', 'الملف الثالث.txt']:
    book = Workbook()
    sheet = book.active

    with open('11.txt', 'r', encoding='utf-8')as f:
        text += f.read()
phone = re.findall(r'\d{8,10}', text)
print(len(phone))
phone = list(set(phone))
print(len(phone))
i = 2
for e in phone:
    sheet[f'A{i}'].value = e
    print(i, ' - ', e)
    i += 1
book.save(file.replace('.txt', '.xlsx'))

# print(phone)

# re.findall(r'From:[0-9a-zA-Zا-ي]*[ \t\r\f\v]*[0-9a-zA-Zا-ي]*', text)
# re.findall(r'City[0-9a-zA-Zا-ي]*[ \t\r\f\v]*[0-9a-zA-Zا-ي]*', text)
# re.compile('[ا-ي]', re.DEBUG)