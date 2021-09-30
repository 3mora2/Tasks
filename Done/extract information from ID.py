from datetime import datetime

governorates = {'01': 'Cairo',
                '02': 'Alexandria',
                '03': 'Port Said',
                '04': 'Suez',
                '11': 'Damietta',
                '12': 'Dakahlia',
                '13': 'Ash Sharqia',
                '14': 'Kaliobeya',
                '15': 'Kafr El - Sheikh',
                '16': 'Gharbia',
                '17': 'Monoufia',
                '18': 'El Beheira',
                '19': 'Ismailia',
                '21': 'Giza',
                '22': 'Beni Suef',
                '23': 'Fayoum',
                '24': 'El Menia',
                '25': 'Assiut',
                '26': 'Sohag',
                '27': 'Qena',
                '28': 'Aswan',
                '29': 'Luxor',
                '31': 'Red Sea',
                '32': 'New Valley',
                '33': 'Matrouh',
                '34': 'North Sinai',
                '35': 'South Sinai',
                '88': 'Foreign'}  # national_id_str[7:9]

fake_national_id_message = 'This ID Not Valid'


def extract_birth_century(birth_century_code: int) -> int:
    """
     extract birth century from national id it's in index 0
    :param birth_century_code: one digit
    :return: birth century
    """
    assert type(birth_century_code) == int, 'birth century code must be int value'
    current_century = get_century_from_year(int(datetime.now().year))
    birth_century = birth_century_code + 18
    assert (birth_century >= 19) and (birth_century <= current_century), fake_national_id_message
    return birth_century


def get_century_from_year(year):
    return year // 100 + 1


def convert_birthdate(birthdate: str) -> str:
    """
    Convert birthday in national id from  fromat yymmdd to yyyy - mm - dd format
    it's from index 0 to 6 in EG national id
    :param birthdate: str
            format cyymmdd, c represent birth century code
    :return: str
            yyyy-mm-dd
    """
    assert len(str(birthdate)) == 7, "birthdate must be 7 digit"
    birth_century = extract_birth_century(int(birthdate[0]))
    birth_year = birthdate[1:3]
    birth_month = birthdate[3:5]
    birth_day = birthdate[5:]
    birth_full_year = (birth_century * 100) - 100 + int(birth_year)
    birthdate_str = '{0}-{1}-{2}'.format(birth_full_year, birth_month, birth_day)
    birthdate_date = datetime.strptime(birthdate_str, '%Y-%m-%d')
    assert birthdate_date <= datetime.now() and birthdate_date >= datetime.strptime('1900-01-01',
                                                                                    '%Y-%m-%d'), fake_national_id_message
    return birthdate_str


def get_birth_governorate(birth_governorate_coda: str) -> str:
    """
    :param birth_governorate_coda:
            Index 7 and 8 in EG national id
    :return: str
             Birth governorate

    """
    assert type(birth_governorate_coda) == str, 'Birth governorate coda must be string not integer'
    assert len(birth_governorate_coda) == 2, 'Birth governorate coda must be 2 digit'
    assert birth_governorate_coda in governorates, 'Birth governorate coda not valid'
    return governorates[birth_governorate_coda]


def get_gender(gender_code: int) -> str:
    """
    :param gender_code:
            Index 12 in EG National ID

    :return: str
            Gender
    """
    assert type(gender_code) == int and gender_code > 0 and gender_code <= 9, 'gender code not valid'
    if gender_code % 2 == 0:
        return 'Female'
    else:
        return 'Male'


def extract_info_from_national_id(national_id: int):
    assert type(national_id) == int, "National ID must be Numbers not string"
    assert len(str(national_id)) == 14, "National ID must be 14 Number "
    national_id_str = str(national_id)
    info = {}

    info['birth_century'] = extract_birth_century(int(national_id_str[0]))
    info['date_of_birth'] = convert_birthdate(national_id_str[0:7])
    info['birth_governorate'] = get_birth_governorate(national_id_str[7:9])
    info['sequence_in_computer'] = national_id_str[9:13]  # random
    info['gender'] = get_gender(int(national_id_str[12]))
    # last_number = national_id_str[13]
    return info


def print_info(information):
    print('Birth Century :', information['birth_century'])
    print('Date Of Birth :', information['date_of_birth'])
    print('Birth Governorate :', information['birth_governorate'])
    print('Gender :', information['gender'])


if __name__ == '__main__':
    info = extract_info_from_national_id(30301010290154)
    print_info(info)

    '''
national_id_str[0] 3
national_id_str[1:7] birthdate
national_id_str[7:9] get_birth_governorate
national_id_str[9:13] random
national_id_str[12] 1, 9
national_id_str[13] random

self.century = int(self.id_number[0])
self.year = int(self.id_number[1:3])
self.month = int(self.id_number[3:5])
self.day = int(self.id_number[5:7])
self.governorate = int(self.id_number[7:9])
self.unique_num = int(self.id_number[9:13])
self.verification_digit = int(self.id_number[13])
    '''
from lib.national_id import NationalID
instance = NationalID("30301010290154")
print(instance.get_info())