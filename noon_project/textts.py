from requests_html import HTMLSession, HTML
import requests
from time import sleep
# pip install fake-headers
from fake_headers import Headers
from itertools import cycle
# session = requests.Session()
# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
#            'User-Agent': 'Mozilla/S.0 (X11; Linux x86_64) AppleWebKit/S37.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
# session.headers.update(headers)
n = 1
session = HTMLSession()
proxies = {'212.87.220.2:3128', '164.100.130.128:8080', '46.218.155.194:3128', '83.97.23.90:18080', '103.87.170.110:38067',
           '95.174.67.50:18080', '5.202.188.154:3128', '13.251.27.133:3128', '51.75.147.43:3128', '161.202.226.194:80'}
proxy_pool = cycle(proxies)
proxy = next(proxy_pool)
print(len(proxies))
url = 'https://httpbin.org/ip'
# session.proxies = proxy
while True:

    session.headers.update(Headers(headers=True).generate())

    r = session.get('https://www.noon.com/uae-en/N25838878A/p?')

    # r = session.get('https://www.noon.com/uae-en/N25838878A/p?', allow_redirects=True)  # ,proxies=proxyDict)

    if r.status_code != 200:

        for i in range(1, len(proxies) + 1):
            print(proxy)
            print("Request #%d" % i)
            try:
                session.cookies.clear()
                r = session.get('https://www.noon.com/uae-en/N25838878A/p?', proxies={"http": proxy, "https": proxy}, timeout=7)
                print(r)
                print(n, '-',
                      r.html.find('.sellingPriceContainer > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)')[
                          0].text)
                break
            except:
                print("Skipping. Connnection error")
                proxy = next(proxy_pool)
            sleep(5)

        session.cookies.clear()

    else:
        # print(n, '-', HTML(html=r.text).find('.sellingPriceContainer > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)')[0].text)
        print(n, '-',
              r.html.find('.sellingPriceContainer > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)')[0].text)
    n += 1
    sleep(3)


# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     r = session.get(url)
#     proxies = set()
#     for i in r.html.xpath('//tbody/tr'):
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies
#
#
# # proxies = get_proxies()
# proxies = {'164.100.130.128:8080', '46.218.155.194:3128', '83.97.23.90:18080', '103.87.170.110:38067', '95.174.67.50:18080', '5.202.188.154:3128', '13.251.27.133:3128','51.75.147.43:3128', '212.87.220.2:3128', '161.202.226.194:80'}
# proxy_pool = cycle(proxies)
# print(len(proxies))
# url = 'https://httpbin.org/ip'
# proxy_work = set()
# for i in range(1, len(proxies)+1):
#     proxy = next(proxy_pool)
#     print("Request #%d" % i)
#     try:
#         response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=3)
#         print(response.json())
#         print('*************************************************')
#         proxy_work.add(proxy)
#     except:
#         print("Skipping. Connnection error")
#     sleep(5)
# {'origin': '161.202.226.194'}
# {'origin': '212.87.220.2'}

# {'95.174.67.50:18080'}
# {'103.87.170.110:38067'}
# {'212.87.220.2:3128'}
# {'46.218.155.194:3128'}
# {'164.100.130.128:8080', '46.218.155.194:3128', '83.97.23.90:18080', '103.87.170.110:38067', '95.174.67.50:18080', '5.202.188.154:3128', '13.251.27.133:3128','51.75.147.43:3128', '212.87.220.2:3128', '161.202.226.194:80'}
