from time import sleep

from playwright.sync_api import sync_playwright
# 1s = 1000ms
browser_type = sync_playwright().start().chromium
browser = browser_type.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", headless=False)
page = browser.new_page()
page.goto('https://www.google.com/preferences#languages')
# input('- ')
# txt = 'شركات مياة بمصر'
# page.goto(f'https://www.google.com/maps/search/{txt}')
# while True:
#     num_scroll = 0
#     while True:
#         try:
#             page.click('.wo1ice-loading', timeout=2 * 1000)
#             sleep(2)
#             num_scroll += 1
#
#             if num_scroll > 5:
#                 print('- Break Scroll..')
#
#             if num_scroll == 8:
#                 break
#         except:
#             break
#
#     sleep(2)
#     num_pl = len(page.query_selector_all('div.section-layout.section-scrollbox div > a'))
#     if num_pl == 0:
#         break

    # for element in page.query_selector_all('div.section-layout.section-scrollbox div > a'):
    #     print(element.get_attribute('href'))
    #
    # try:
    #     if page.get_attribute('button[jsaction="pane.paginationSection.nextPage"]', 'disabled') == 'true':
    #         break
    #
    #     try:
    #         page.click('*[aria-label="الصفحة التالية"]')
    #     except:
    #         page.click('button[jsaction="pane.paginationSection.nextPage"]')
    #     sleep(4)
    # except:
    #     break