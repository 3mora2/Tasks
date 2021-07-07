# https://playwright.dev/python/docs/api/class-elementhandle
# import os.path
#
# homedir = os.path.expanduser("~")
# path = homedir + r'\AppData\Local\Google\Chrome\User Data\Default'

from playwright.sync_api import sync_playwright

browser_type = sync_playwright().start().chromium
browser = browser_type.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                              headless=False, )
# ignore_default_args=True,
# args=[
#       '--flag-switches-begin',
#       '--flag-switches-end',
#       '--origin-trial-disabled-features=SecurePaymentConfirmation',
#       "--enable-automation",
#       "--no-first-run",
#       # rf'--user-data-dir={path}',
#       '--profile-directory=Default'
#       ]
#                                                                 )

# b = browser_type.launch_persistent_context(user_data_dir=path
#                                            , headless=False
#                                            , ignore_default_args=[
#                                                                 '--flag-switches-begin',
#                                                                 '--flag-switches-end',
#                                                                 '--origin-trial-disabled-features=SecurePaymentConfirmation',
#                                                                 "--enable-automation",
#                                                                 "--no-first-run",
#                                                                 '--profile-directory=Default'
#                                                             ],
#                                            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
#                                            )
# context = browser.new_context()
# context1 = browser.new_browser_cdp_session()
# context2 = browser.new_page()
# page = context.new_page()
page = browser.new_page()
page.goto('https://sa.iherb.com/')

