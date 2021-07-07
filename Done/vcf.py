from PyPDF2 import PdfFileReader
import re

pdf_fil = input('Enter PDF name : ')
# 'Issue-713_compressed.pdf'
l = []
with open(pdf_fil, 'rb') as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    for page in range(0, number_of_pages):
        p = pdf.getPage(page).extractText()
        l += re.findall(r'\d{10,11}', p)
        print(len(l))
l = list(set(l))
print('*********************************************')
print(len(l))

with open(pdf_fil.replace('.pdf', '.vcf'), 'w') as output:
    for e in l:
        print(e)
        output.write("BEGIN:VCARD\n")
        output.write("VERSION:3.0\n")
        # output.write("N:" + row[1] + ";" + row[0] + ";;;\n")
        # output.write("FN:" + row[0] + row[1] + "\n")
        output.write("TEL;TYPE=HOME,VOICE:" + str(e) + "\n")
        output.write("END:VCARD\n")
