from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()

# Open new page
page = context.new_page()

# Go to https://www.google.com/maps/search/%D8%B4%D8%B1%D9%83%D8%A7%D8%AA+%D8%B7%D8%A8%D9%8A%D9%87+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87+%E2%80%AD%E2%80%AD%E2%80%AD/@23.8559847,46.8840292,7z/data=!3m1!4b1
page.goto("https://www.google.com/maps/search/%D8%B4%D8%B1%D9%83%D8%A7%D8%AA+%D8%B7%D8%A8%D9%8A%D9%87+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87+%E2%80%AD%E2%80%AD%E2%80%AD/@23.8559847,46.8840292,7z/data=!3m1!4b1")


# Click [aria-label="الصفحة التالية"]
# with page.expect_navigation(url="https://www.google.com/maps/search/%D8%B4%D8%B1%D9%83%D8%A7%D8%AA+%D8%B7%D8%A8%D9%8A%D9%87+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87+%E2%80%AD%E2%80%AD%E2%80%AD/@23.8559847,46.8840292,7z/data=!3m1!4b1"):
# with page.expect_navigation():
#     page.click("[aria-label=\"الصفحة التالية\"]")

# Click [aria-label="الشركة العربية لتصنيع المنتجات الطبية عنايه"]
# with page.expect_navigation(url="https://www.google.com/maps/place/%D8%A7%D9%84%D8%B4%D8%B1%D9%83%D8%A9+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D8%AA%D8%B5%D9%86%D9%8A%D8%B9+%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA+%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%A9+%D8%B9%D9%86%D8%A7%D9%8A%D9%87%E2%80%AD/@23.8559847,46.8840292,7z/data=!4m9!1m2!2m1!1z2LTYsdmD2KfYqiDYt9io2YrZhyDYp9mE2LPYudmI2K_ZitmHIOKAreKArQ!3m5!1s0x3e2fa11443d567f3:0x144ec6718e7488f7!8m2!3d24.5660198!4d46.8800542!15sCivYtNix2YPYp9iqINi32KjZitmHINin2YTYs9i52YjYr9mK2Ycg4oCt4oCtkgEQY29ycG9yYXRlX29mZmljZQ"):
# with page.expect_navigation():
#     page.click("[aria-label=\"الشركة العربية لتصنيع المنتجات الطبية عنايه\"]")

# Close page
# page.close()

# ---------------------
# context.close()
# browser.close()

