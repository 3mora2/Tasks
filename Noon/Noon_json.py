import requests

# login = 'https://login.noon.partners/en/'

session = requests.session()

# session.headers.update({'__cfduid': 'd84d6c279fc96ad8884d9a354fbadf6231618669042'})

# resp = session.post(login,
#                     data={'email': 'bekj.119@gmail.como', 'password': '11111111111111'},
#                     allow_redirects=True)

r = session.post("https://login.noon.partners/_svc/auth-v1/public/auth/signin", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Locale": "en-ae",
        "X-Platform": "web"
    },
    "referrer": "https://login.noon.partners/en/?page=core",
    "body": "{\"email\":\"ammar@gmail.com\",\"password\":\"1111111111111111111\"}",
    "method": "POST",
    "mode": "cors"
})
#
# await fetch("https://login.noon.partners/_svc/auth-v1/public/auth/signin", {
#     "credentials": "omit",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Content-Type": "application/json",
#         "Cache-Control": "no-cache",
#         "X-Locale": "en-ae",
#         "X-Platform": "web"
#     },
#     "referrer": "https://login.noon.partners/en/?page=core",
#     "body": "{\"email\":\"ammmar@gmail.com\",\"password\":\"11111111111111111111\"}",
#     "method": "POST",
#     "mode": "cors"
# });
'''
__cfduid=d84d6c279fc96ad8884d9a354fbadf6231618669042;
__cf_bm=5e583c28d314487e714a1978e7b917fdd6fae1ed-1618669043-1800-AXtfrqPJTw6T4UQCrgCuXd3DeJIyHS1GAXuoqvkBO/yBRd2mptE6TJ+ggxitJUZ80T1z/uO5RFwkSEenaKhDx4nmWWp7c5cdYS8ZH2gXsYvkbT6kzTPTRL4arKNKBuQ4iQ==
'''
'''
cf-cache-status: DYNAMIC 
cf-ray: 6416474a791041fc-MRS 
cf-request-id: 0981cae28b000041fc25101000000001 
content-length: 1218 
content-type: application/json 
date: Sat, 17 Apr 2021 14:17:42 GMT 
expect-ct: max-age=604800, 
report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct" 
referrer-policy: strict-origin-when-cross-origin 
server: cloudflare 
x-content-type-options: nosniff 
x-envoy-upstream-service-time: 61 
x-frame-options: DENY 
x-xss-protection: 1; 
mode=block
'''
'''
:authority: login.noon.partners :
method: POST :
path: /_svc/auth-v1/public/auth/signin :
scheme: https accept: application/json, text/plain, */* accept-encoding: gzip, deflate, br accept-language: en-US,en;q=0.9 cache-control: no-cache content-length: 60 content-type: application/json cookie: __cfduid=d84d6c279fc96ad8884d9a354fbadf6231618669042; __cf_bm=5e583c28d314487e714a1978e7b917fdd6fae1ed-1618669043-1800-AXtfrqPJTw6T4UQCrgCuXd3DeJIyHS1GAXuoqvkBO/yBRd2mptE6TJ+ggxitJUZ80T1z/uO5RFwkSEenaKhDx4nmWWp7c5cdYS8ZH2gXsYvkbT6kzTPTRL4arKNKBuQ4iQ== origin: https://login.noon.partners referer: https://login.noon.partners/en/ sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90" sec-ch-ua-mobile: ?0 sec-fetch-dest: empty sec-fetch-mode: cors sec-fetch-site: same-origin user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 x-locale: en-ae x-platform: web
'''