from appium import webdriver

desired_capab = {
    'platformName': 'Android',
    'platformVersion': '5.1.1'
}
desired = {
    'platformName': "Android",
    'platformVersion': "8",
    # 'deviceName': "Android Emulator",
    'app': "ApiDemos.apk",
    'appPackage': "io.appium.android.apis",
    'appActivity': ".view.TextFields",
    'automationName': "UiAutomator2"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
