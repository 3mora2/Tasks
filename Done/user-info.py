import requests,json,re


strHtml = requests.get(f"https://www.instagram.com/chhc/?__a=1").text
resp = json.loads(strHtml)
user = resp['graphql']['user']
bio = user['biography']
external_url = user['external_url']
followed_by = user['edge_followed_by']['count']
follow = user['edge_follow']['count']
full_name = user['full_name']
user_id = user['id']
is_business_account = user['is_business_account']
is_joined_recently = user['is_joined_recently']
business_category_name = user['business_category_name']
category_id = user['category_id']
overall_category_name = user['overall_category_name']
username = user['username']
connected_fb_page = user['connected_fb_page']
is_private = user['is_private']
posts = user['edge_owner_to_timeline_media']['count']
has_channel = user['has_channel']
country_block = user['country_block']
followed_by_viewer = user['followed_by_viewer']
follows_viewer = user['follows_viewer']
has_ar_effects = user['has_ar_effects']
has_blocked_viewer = user['has_blocked_viewer']
highlight_reel_count = user['highlight_reel_count']
has_requested_viewer = user['has_requested_viewer']
user_id = user['id']
is_business_account = user['is_business_account']
is_joined_recently = user['is_joined_recently']
business_category_name = user['business_category_name']
category_id = user['category_id']
overall_category_name = user['overall_category_name']
category_enum = user['category_enum']
is_verified = user['is_verified']
mutual_followed_by = user['edge_mutual_followed_by']['count']
profile_pic_url_hd = user['profile_pic_url_hd']
requested_by_viewer = user['requested_by_viewer']
felix_video_timeline = user['edge_felix_video_timeline']['count']
saved_media = user['edge_saved_media']['count']
media_collections = user['edge_media_collections']['count']
if re.search(r'[\w\.-]+@[\w-]+\.[\w-]+', bio):
    email = re.search(r'[\w\.-]+@[\w-]+\.[\w-]+', bio).group(0)
elif re.search(r'[\w\.-]+@[\w-]+\.[\w-]+', full_name):
    email = re.search(r'[\w\.-]+@[\w-]+\.[\w-]+', full_name).group(0)
else:
    email = None
print(f'username:{username} is_business_account:{is_business_account} email:{email} ')
