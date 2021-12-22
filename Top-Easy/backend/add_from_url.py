import json

from PySide2.QtCore import QThread, Signal
from requests_html import HTMLSession

from aqar_way import OTHER_VALIDATION, VALIDATION

session = HTMLSession()


class AddFromURL(QThread):
    final = Signal(object)

    def run(self):
        response = session.get(self.url)
        # text = response.html.xpath('//script[contains(text(), "window.__store__")]', first=True).attrs['innerText'].replace(
        text = response.html.xpath('//script[contains(text(), "window.__store__")]', first=True).text.replace(
            'window.__store__ = ', '')

        data = json.loads(text)
        data_info = data['listingReducer']['selectedListing']
        user_name = data_info.get('user').get("name")
        try:
            imgs = list(
                map(lambda x: 'https://images.aqar.fm/' + x, data['listingReducer']['selectedListing']['imgs']))
        except:
            imgs = []
        data_info['imgs'] = ', '.join(imgs)

        try:
            videos = list(
                map(lambda x: x.get('video'), data['listingReducer']['selectedListing']['videos']))
        except:
            videos = []
        data_info['videos'] = ', '.join(videos)
        data_info.pop('verified')
        data_info.pop('user')
        data_info.pop('views')
        data_info.pop('links')
        data_info.pop('related')
        user_id = data_info.pop('user_id')
        if data_info['age'] == 0:
            data_info['age'] = 'جديد'
        data_info['location'] = f'lat: {data_info["location"].get("lat")}, lng: {data_info["location"].get("lng")}'
        data_info = self.check_value(data_info)

        self.final.emit({'data_info': data_info, 'user_name': user_name, 'user_id': user_id})

    def check_value(self, data_info):
        for key in data_info.keys():
            value = data_info[key]
            if value in [None, ]:
                continue
            if key in OTHER_VALIDATION.keys():
                data_info[key] = f'{value} {OTHER_VALIDATION.get(key)}'
            elif key in VALIDATION.keys():
                options = VALIDATION.get(key, {}).get('options')
                if options:
                    result = list(filter(lambda x: value is not None and (x.get('value') == value), options))
                    if result:
                        result = result[0]
                        data_info[key] = result.get('title')

        return data_info
