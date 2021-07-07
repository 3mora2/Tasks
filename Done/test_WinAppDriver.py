# import win32com.shell.shell as shell
# commands = '''
# reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
# '''
# commands2 = '''
# reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowAllTrustedApps" /d "1"
# '''
# shell.ShellExecuteEx(lpVerb='runas', lpFile='C:\WINDOWS\system32\cmd.exe', lpParameters='/c '+commands)

from appium import webdriver

desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities=desired_caps)
