d = {
    'family': {'urlName': 'family', 'fieldName': "الفئة",
               'options': [{'title': 'عوائل', 'value': 1, 'where': {'eq': 1}},
                           {'title': 'عزاب', 'value': 0, 'where': {'eq': 0}}]},

    'rent_period': {'urlName': 'rent_type', 'fieldName': "",
                    'options': [{'title': 'الكل', 'value': None}, {'title': 'يومي', 'value': 1, 'where': {'eq': 1}},
                                {'title': 'شهري', 'value': 2, 'where': {'eq': 2}},
                                {'title': 'سنوي', 'value': 3, 'where': {'eq': 3}}]},

    'ketchen': {'urlName': 'kitchen',
                'options': [{'title': 'الكل', 'value': None}, {'title': 'مطبخ موجود', 'value': 1, 'where': {'eq': 1}}]},

    'duplex': {'urlName': 'duplex',
               'options': [{'title': 'الكل', 'value': None}, {'title': 'دوبلكس', 'value': 1, 'where': {'eq': 1}}]},

    'furnished': {'urlName': 'furnished',
                  'options': [{'title': 'الكل', 'value': None}, {'title': 'مؤثثة', 'value': 1, 'where': {'eq': 1}}]},
    'driver': {'urlName': 'driver',
               'options': [{'title': 'الكل', 'value': None}, {'title': 'غرفة سائق', 'value': 1, 'where': {'eq': 1}}]},
    'maid': {'urlName': 'maid',
             'options': [{'title': 'الكل', 'value': None}, {'title': 'غرفة خادمة', 'value': 1, 'where': {'eq': 1}}]},
    'basement': {'urlName': 'basement',
                 'options': [{'title': 'الكل', 'value': None}, {'title': 'يوجد قبو', 'value': 1, 'where': {'eq': 1}}]},
    'lift': {'urlName': 'lift',
             'options': [{'title': 'الكل', 'value': None}, {'title': 'يوجد مصعد', 'value': 1, 'where': {'eq': 1}}]},
    'pool': {'urlName': 'pool',
             'options': [{'title': 'الكل', 'value': None}, {'title': 'يوجد مسبح', 'value': 1, 'where': {'eq': 1}}]},
    'stairs': {'urlName': 'stairs',
               'options': [{'title': 'الكل', 'value': None},
                           {'title': 'يوجد درج صالة', 'value': 1, 'where': {'eq': 1}}]},
    'fb': {'urlName': 'football',
           'options': [{'title': 'الكل', 'value': None},
                       {'title': 'يوجد ملعب كرة قدم', 'value': 1, 'where': {'eq': 1}}]},
    'vb': {'urlName': 'volleyball',
           'options': [{'title': 'الكل', 'value': None},
                       {'title': 'يوجد ملعب كرة طائرة', 'value': 1, 'where': {'eq': 1}}]},
    'playground': {'urlName': 'playground',
                   'options': [{'title': 'الكل', 'value': None},
                               {'title': 'يوجد ملاهي', 'value': 1, 'where': {'eq': 1}}]},
    'family_section': {'urlName': 'family_section',
                       'options': [{'title': 'الكل', 'value': None},
                                   {'title': 'يوجد قسم عوائل', 'value': 1, 'where': {'eq': 1}}]},
    'type': {'urlName': 'type', 'options': [{'title': 'سكني', 'value': 1, 'where': {'eq': 1}},
                                            {'title': 'تجاري', 'value': 2, 'where': {'eq': 2}}]},
    'car_entrance': {'urlName': 'car_entrance',
                     'options': [{'title': 'الكل', 'value': None},
                                 {'title': 'يوجد مدخل سيارة', 'value': 1, 'where': {'eq': 1}}]},
    'ac': {'urlName': 'ac',
           'options': [{'title': 'الكل', 'value': None}, {'title': 'يوجد مكيف', 'value': 1, 'where': {'eq': 1}}]},
    'extra_unit': {'urlName': 'extra_unit',
                   'options': [{'title': 'الكل', 'value': None},
                               {'title': 'extra unit available', 'value': 1, 'where': {'eq': 1}}]},

    'fl': {'urlName': 'fl',
           'options': [{'title': 'الكل', 'value': None}, {'title': 'دور أرضي', 'value': 1, 'where': {'eq': 1}},
                       {'title': 'دور علوي', 'value': 2, 'where': {'eq': 2}},
                       {'title': 'الدور 3', 'value': 3, 'where': {'eq': 3}},
                       {'title': 'الدور 4', 'value': 4, 'where': {'eq': 4}},
                       {'title': 'الدور 5+ ', 'value': 5, 'where': {'gte': 5}}]},

    'street_direction': {'urlName': 'street_direction', 'fieldName': 'الواجهة',
                         'options': [{'title': 'الكل', 'value': None},
                                     {'title': 'شمال', 'value': 1, 'where': {'eq': 1}},
                                     {'title': 'شرق', 'value': 2, 'where': {'eq': 2}},
                                     {'title': 'غرب', 'value': 3, 'where': {'eq': 3}},
                                     {'title': 'جنوب', 'value': 4, 'where': {'eq': 4}},
                                     {'title': 'شمالي شرقي', 'value': 5, 'where': {'eq': 5}},
                                     {'title': 'جنوب شرقي', 'value': 6, 'where': {'eq': 6}},
                                     {'title': 'جنوب غربي', 'value': 7, 'where': {'eq': 7}},
                                     {'title': 'شمال غربي', 'value': 8, 'where': {'eq': 8}},
                                     {'title': '3 شوارع', 'value': 9, 'where': {'eq': 9}},
                                     {'title': '4 شوارع', 'value': 10, 'where': {'eq': 10}}]},

}

OTHER_VALIDATION = {'age': 'سنين', 'area': 'م²', 'street_width': "م"}

api_data = {"id": 3573512, "imgs": ["503553979_1633333302784.jpg"],
            "has_video": 0, "videos": None, "address": "شارع الحسين بن علي ، حي المصيف ، الرياض ، الرياض",
            "content": "دبوس مثبّت\nhttps://maps.app.goo.gl/HHASX3AHB3feWcYq8\n\n\n\nفيلا للبيع بحي النرجس الكيلو الرابع شمال طريق💮💐💐💐\n الملك سلمان عمر الفيلا ٥🌺\nللبيع فيلا في حي النرجس ⁦🏵️⁩\nدور ارضي و٤شقق \nالدور لأرضي استقبال بالكامل مجلس مقلط صاله ٤غرفه نوم مع دورات مياه وصاله السطح 🌹\nكل شقة ٣غرفه نوم وصاله ومطبخ ٢دورات 🍀\n سنوات بناء شخصي ⁦❄️⁩\nمساحة الأرض ( ٧٥٠ م ) تقع على شارعين ( ٢٠ شمالي ) ( ١٥💐 شرقي ) ( ٣عدات كهرباء ١٥٠ - ١٥٠ - ١٠٠ )( عداد مياه ٣ شرائح ) \nالفيلا عبارة عن ٣ أدوار وهي 🌷\nالدور الأرضي : عبارة عن ملحق + بوفيه وحمام + مجلس رجال + مقلط + مغاسل وحمام رجال + مجلس حريم + صاله عائله + مغاسل وحمام حريم + ٤ غرف نوم ( غرفتين ماستر ، غرفتين✨ بدون ماستر) + حمام + غرفة شغاله + غرفة سواق + مطبخ + جلسة خارجية بقسم الحريم يوجد معها حمام 🌼\nشقة مسروقة مدخل جانبي وهي عبارة عن ٣ غرف وصاله ومطبخ🌸 و٢ حمام🍁 \nالدور الأول : عبارة عن شقتين مليسة ومسبكة كهرباء كل شقة🌿 عبارة عن مجلس رجال ومقلط  وصاله و٣ غرف نوم ومطبخ🌿 ومستودع و٢ حمام ⁦🏵️⁩\nالدور الثاني ( السطح ) شقة وهي عبارة عن مجلس رجال وصاله و٣ غرف نوم وغرفة شغاله وحوش مستقل ومستودع خارجي🥀\nالفيلا ساكن ولازم موعد مباشر مع المالك🌼 \nحدالبيع ٥مليون 🌱\nالبيع مع لاثاث 🌸\nالتواصل على الرقم 👈 0548341526🌷\n🥀0548341526🌺",
            "price": 5000000, "refresh": 1633579079, "category": 3,
            "path": "/فلل-للبيع/الرياض/شمال-الرياض/حي-المصيف/شارع-الحسين-بن-علي-حي-المصيف-الرياض-الرياض-3573512",
            "title": "فيلا للبيع في شارع الحسين بن علي ، حي المصيف ، الرياض ، الرياض", "rent_period": 3,
            "district": "حي المصيف", "direction": "شمال الرياض", "city": "الرياض", "direction_id": 4,
            "district_id": 556, "city_id": 21, "user_id": 1741562,
            "uri": "شارع-الحسين-بن-علي-حي-المصيف-الرياض-الرياض-3573512",
            "status": 0, "ac": 1, "age": 4, "apts": 4, "area": 750, "backyard": 1, "basement": 1, "beds": 5,
            "car_entrance": 1,
            "driver": 1, "duplex": 1, "extra_unit": 1, "family": 1, "family_section": None, "fb": None, "fl": 2,
            "furnished": 1,
            "ketchen": 1, "lift": 0, "livings": 3, "maid": 1, "meter_price": 6667, "playground": None, "pool": 0,
            "rooms": None,
            "stairs": 0, "stores": None, "street_direction": 1, "street_width": 20, "tent": 1, "trees": None,
            "type": None,
            "vb": None,
            "wc": 5, "wells": None, "premium": 0, "location": {"lat": 24.766001, "lng": 46.682158}}

for key in api_data.keys():
    value = api_data[key]
    if key in OTHER_VALIDATION.keys():
        print(value, OTHER_VALIDATION.get(key))
    else:
        options = d.get(key, {}).get('options')
        if options:
            result = list(filter(lambda x: value is not None and (x.get('value') == value), options))
            if result:
                result = result[0]
                print(key, value, result.get('title'))
