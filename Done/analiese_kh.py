import json
import pprint

program = 0
programs = ['program', 'برمجه', 'برنامج', 'تطوير', 'تطبيق',  'فلتر', 'flutter']
flutter = 0
flutters = ['flutter', 'فلتر', 'فلاتر', 'تطبيق', 'اندرويد']
python = 0
pythons = ['python', 'بايثون', 'بيثون']
extract = 0
extracts = ['web scr', 'استخراج', 'كشط', 'سحب', 'داتا من موقع', 'اسكراب']


def check(lists, text, p):
    for txt in lists:
        if txt in text:
            print('--')
            p += 1
            return p
    return p


with open('khamsat_data.json') as f:
    data = json.load(f)

for element in data:
    element = element['title']
    program = check(programs, element, program)
    flutter = check(flutters, element, flutter)
    python = check(pythons, element, python)
    extract = check(extracts, element, extract)

print('prog', program)
print('flutter', flutter)
print('python', python)
print('extract', extract)
''':
prog 929
flutter 758
python 37
extract 31
'''