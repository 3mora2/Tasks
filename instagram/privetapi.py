from instagram_private_api import Client

api = Client(username='201028946519', password='ammar2020')
'''
si/fetch_headers/
{'challenge_type': 'signup', 'guid': '3030c88f016e11eb83185820b17116d5'}
b''
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '4344kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger', 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid=3030c88f016e11eb83185820b17116d5
{'status': 'ok'}
{'status': 'ok'}
POST
accounts/login/
{'device_id': 'android-30305788016e11eb', 'guid': '30305787-016e-11eb-b86f-5820b17116d5', 'adid': '5b846e3a-0121-26c8-dbe4-6e71a2983aab', 'phone_id': '24afa58c-0aa3-3d5b-7b04-84a95d36fe77', '_csrftoken': 'rtyfmPIAM2NmuOSKum29wD4do0po5cJZ', 'username': '201028946519', 'password': 'ammar2020', 'login_attempt_count': '0'}
None
b'ig_sig_key_version=4&signed_body=f80c52e447e8ab457eaf1b494a13ff44f7f73e7ad04372b5054d5cf455cb79c2.%7B%22device_id%22%3A%22android-30305788016e11eb%22%2C%22guid%22%3A%2230305787-016e-11eb-b86f-5820b17116d5%22%2C%22adid%22%3A%225b846e3a-0121-26c8-dbe4-6e71a2983aab%22%2C%22phone_id%22%3A%2224afa58c-0aa3-3d5b-7b04-84a95d36fe77%22%2C%22_csrftoken%22%3A%22rtyfmPIAM2NmuOSKum29wD4do0po5cJZ%22%2C%22username%22%3A%22201028946519%22%2C%22password%22%3A%22ammar2020%22%2C%22login_attempt_count%22%3A%220%22%7D'
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '3971kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger', 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
https://i.instagram.com/api/v1/accounts/login/



si/fetch_headers/
{'challenge_type': 'signup', 'guid': 'ed96c798016e11eb94035820b17116d5'}
https://i.instagram.com/api/v1/si/fetch_headers/
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '3452kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger'}
b''
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '3452kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger', 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid=ed96c798016e11eb94035820b17116d5
POST
{'status': 'ok'}
accounts/login/
{'device_id': 'android-ed967979016e11eb', 'guid': 'ed967978-016e-11eb-ac15-5820b17116d5', 'adid': '5b846e3a-0121-26c8-dbe4-6e71a2983aab', 'phone_id': '4d4f3e2a-6191-1ae1-1cc3-a96aa4907e79', '_csrftoken': 'AsTEWXbrH9SBYk668BvppUY99WZnIl6l', 'username': '201028946519', 'password': 'ammar2020', 'login_attempt_count': '0'}
None
https://i.instagram.com/api/v1/accounts/login/
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '3716kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger'}
b'ig_sig_key_version=4&signed_body=7d6085e354c8eb847d1bd5a0a0667a5c0114d4bb69c27a9d5fabd62fd578d4ef.%7B%22device_id%22%3A%22android-ed967979016e11eb%22%2C%22guid%22%3A%22ed967978-016e-11eb-ac15-5820b17116d5%22%2C%22adid%22%3A%225b846e3a-0121-26c8-dbe4-6e71a2983aab%22%2C%22phone_id%22%3A%224d4f3e2a-6191-1ae1-1cc3-a96aa4907e79%22%2C%22_csrftoken%22%3A%22AsTEWXbrH9SBYk668BvppUY99WZnIl6l%22%2C%22username%22%3A%22201028946519%22%2C%22password%22%3A%22ammar2020%22%2C%22login_attempt_count%22%3A%220%22%7D'
{'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)', 'Connection': 'close', 'Accept': '*/*', 'Accept-Language': 'en-US', 'Accept-Encoding': 'gzip, deflate', 'X-IG-Capabilities': '3brTvw==', 'X-IG-Connection-Type': 'WIFI', 'X-IG-Connection-Speed': '3716kbps', 'X-IG-App-ID': '567067343352427', 'X-IG-Bandwidth-Speed-KBPS': '-1.000', 'X-IG-Bandwidth-TotalBytes-B': '0', 'X-IG-Bandwidth-TotalTime-MS': '0', 'X-FB-HTTP-Engine': 'Liger', 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
https://i.instagram.com/api/v1/accounts/login/
POST
{'logged_in_user': {'pk': 35879687727, 'username': 'gujiyu3', 'full_name': 'Gujiyu', 'is_private': False, 'profile_pic_url': 'https://scontent-frt3-1.cdninstagram.com/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=scontent-frt3-1.cdninstagram.com&_nc_ohc=FvRIGkb-0bMAX8b9Ep7&oh=56267206e0487cb11bca31c4eecd1da8&oe=5F9A258F&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2', 'is_verified': False, 'has_anonymous_profile_picture': True, 'can_boost_post': False, 'is_business': False, 'account_type': 1, 'professional_conversion_suggested_account_type': 2, 'is_call_to_action_enabled': None, 'can_see_organic_insights': False, 'show_insights_terms': False, 'total_igtv_videos': 0, 'reel_auto_archive': 'unset', 'has_placed_orders': False, 'allowed_commenter_type': 'any', 'nametag': {'mode': 0, 'gradient': 0, 'emoji': '😀', 'selfie_sticker': 0}, 'is_using_unified_inbox_for_direct': False, 'interop_messaging_user_fbid': 17842341056199728, 'can_see_primary_country_in_settings': False, 'account_badges': [], 'allow_contacts_sync': False, 'phone_number': '+201028946519', 'country_code': 20, 'national_number': 1028946519}, 'status': 'ok'}
'''

