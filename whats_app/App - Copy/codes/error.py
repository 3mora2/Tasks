from datetime import datetime


def error_Text(error):
    with open('log.log', 'a+', encoding="utf-8") as f:
        f.write(f'{datetime.now()}: {str(error)} \n')