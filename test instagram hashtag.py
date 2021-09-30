from instagram_private_api import Client, ClientCompatPatch

user_name = '201028946519'
password = 'ammar2020'

api = Client(user_name, password)
results = api.tag_section('كافيهات_جده')
items = results.get('items', [])
