FULL_NAMES = {
    "id": {"gql": "Int", "name": {"ar": "رقم الإعلان", "en": "Listing number"}},
    'refresh': {"gql": "Float", "name": {"ar": "وقت اخ تحديث", "en": "Last update"}},
    "category": {"gql": "Int", "name": {"ar": "نوع العقار", "en": "Category"}},
    'has_img': {"gql": "Int", "name": {"ar": "مصورة", "en": "Has image"}},
    'imgs': {"gql": "[String]", "name": {"ar": "صور الإعلان", "en": "Images"}},
    'has_video': {"gql": "Int", "name": {"ar": "فيديو", "en": "Has video"}},
    'videos': {"gql": "[String]", "name": {"ar": "فيديو الإعلان", "en": "videos"}},
    'imgs_desc': {"gql": "[String]", "name": {"ar": "وصف الصور", "en": "Images description"}},
    'status': {"gql": "Int", "name": {"ar": "الحالة", "en": "Status"},
               "values": {"ar": ["متاح", "مغلق", "مغلق قابل للفتح"], "en": ["Available", "Closed", "Re-openable"]}},
    'premium': {"gql": "Int", "name": {"ar": "مدفوع ام مجاني", "en": "Free or premium"},
                "values": {"ar": ["مجاني", "مدفوع"], "en": ["Free", "Paid"]}},
    'price': {"gql": "Float", "name": {"ar": "السعر", "en": "Price"}},
    'wc': {"gql": "Int", "name": {"ar": "عدد دورات المياه", "en": "WC"}},
    'meter_price': {"gql": "Float", "name": {"ar": "سعر المتر", "en": "Meter price"}},
    "age": {"gql": "Int", "name": {"ar": "عمر العقار اقل من", "en": "Age less than"}},
    'area': {"gql": "Float", "name": {"ar": "المساحة", "en": "Area(m2)"}},
    'fl': {"gql": "Int", "name": {"ar": "الدور", "en": "Floor"}},
    'rent_period': {"gql": "Int", "name": {"ar": "مدة الإيجار", "en": "Rent period"}},
    'beds': {"gql": "Int", "name": {"ar": "عدد غرف النوم", "en": "Bed rooms"}},
    'livings': {"gql": "Int", "name": {"ar": "عدد الصالات", "en": "Living rooms"}},
    'ketchen': {"gql": "Int", "name": {"ar": "مطبخ", "en": "Kitchen"}},
    'men_place': {"gql": "Int", "name": {"ar": "مجلس رجال", "en": "Men majles"}},
    'women_place': {"gql": "Int", "name": {"ar": "مجلس نساء", "en": "Women majles"}},
    'apts': {"gql": "Int", "name": {"ar": "عدد الشقق", "en": "Apartments"}},
    'stores': {"gql": "Int", "name": {"ar": "عدد المحلات", "en": "Stores"}},
    'duplex': {"gql": "Int", "name": {"ar": "دوبلكس", "en": "Duplex"}},
    'furnished': {"gql": "Int", "name": {"ar": "مؤثثة", "en": "Furnished"}},
    'driver': {"gql": "Int", "name": {"ar": "غرفة سائق", "en": "Driver room"}},
    'maid': {"gql": "Int", "name": {"ar": "غرفة خادمة", "en": "Maid room"}},
    'basement': {"gql": "Int", "name": {"ar": "قبو", "en": "Basement"}},
    'lift': {"gql": "Int", "name": {"ar": "مصعد", "en": "Lift"}},
    'pool': {"gql": "Int", "name": {"ar": "مسبح", "en": "Pool"}},
    'stairs': {"gql": "Int", "name": {"ar": "درج صالة", "en": "Stairs"}},
    'fb': {"gql": "Int", "name": {"ar": "ملعب كرة قدم", "en": "Football pitch"}},
    'vb': {"gql": "Int", "name": {"ar": "ملعب كرة طائرة", "en": "Volleyball Court"}},
    'tent': {"gql": "Int", "name": {"ar": "بيت شعر", "en": "Tent"}},
    'rooms': {"gql": "Int", "name": {"ar": "عدد الغرف", "en": "Rooms"}},
    'wells': {"gql": "Int", "name": {"ar": "عدد الآبار", "en": "Wells"}},
    'trees': {"gql": "Int", "name": {"ar": "عدد الأشجار", "en": "Trees"}},
    'backyard': {"gql": "Int", "name": {"ar": "حوش", "en": "Backyard"}},
    'playground': {"gql": "Int", "name": {"ar": "ملاهي", "en": "Playground"}},
    'family': {"gql": "Int", "name": {"ar": "عوائل أم عزاب", "en": "Family or single"}},
    'family_section': {"gql": "Int", "name": {"ar": "قسم عوائل", "en": "Family section"}},
    'street_direction': {"gql": "Int", "name": {"ar": "الواجهة", "en": "Street direction"}},
    'street_width': {"gql": "Int", "name": {"ar": "عرض الشارع", "en": "Street width"}},
    'type': {"gql": "Int", "name": {"ar": "سكني أو تجاري", "en": "Residential and commercial"}},
    'car_entrance': {"gql": "Int", "name": {"ar": "مدخل سيارة", "en": "Car entrance"}},
    'ac': {"gql": "Int", "name": {"ar": "مكيف", "en": "Air conditioned"}},
    'location': {"gql": "Location", "name": {"ar": "الموقع", "en": "Location"}},
    'address': {"gql": "String", "name": {"ar": "العنوان", "en": "Status"}},
    'content': {"gql": "String", "name": {"ar": "الحالة", "en": "Address"}},
    'services': {"gql": "[Service]", "name": {"ar": "الخدمات", "en": "Services"}},
    'uri': {"gql": "String", "name": {"ar": "الرابط", "en": "Url"}},
    'city_id': {"gql": "Int", "name": {"ar": "رقم المدينة", "en": "City ID"}},
    'direction_id': {"gql": "Int", "name": {"ar": "رقم الاتجاه", "en": "Direction ID"}},
    'district_id': {"gql": "Int", "name": {"ar": "رقم الحي", "en": "District ID"}},
    'province_id': {"gql": "Int", "name": {"ar": "رقم المحافظة", "en": "Province ID"}},
    'views': {"gql": "Int", "name": {"ar": "المشاهدات", "en": "Views"}},
    'user': {"gql": "ListingUser", "name": {"ar": "المستخدم", "en": "User"}},
    'user_id': {"gql": "Int", "name": {"ar": "رقم المستخدم", "en": "User ID"}},
    'user_type': {"gql": "Int", "name": {"ar": "مستخدم ام سمسار", "en": "user or agent"}},
    'extra_unit': {"gql": "Int", "name": {"ar": "ملحق", "en": "Extra unit"}},

    'path': {"gql": "String", "name": {"ar": "المسار", "en": "Path"}},
    'title': {"gql": "String", "name": {"ar": "العنوان", "en": "Title"}},
    'district': {"gql": "String", "name": {"ar": "الحي", "en": "District"}},
    'direction': {"gql": "String", "name": {"ar": "الاتجاه", "en": "Direction"}},
    'city': {"gql": "String", "name": {"ar": "المدينة", "en": "City"}}


}

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
    print(key, FULL_NAMES.get(key).get('name').get('ar'))
