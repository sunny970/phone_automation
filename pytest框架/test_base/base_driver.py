import os

from appium import webdriver

def init_Android_driver():
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = '10.28.161.211:5555'
    desired_caps['appPackage'] = 'com.oppo.launcher3'
    desired_caps['appActivity'] = '.Launcher'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noRest'] = True
    desired_caps['automationName'] = 'uiautomator2'

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    return driver


def init_Ios_driver():
    desired_caps = {}

    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'iPhone 8'
    # desired_caps['app'] = os.path.abspath('com.xx.xx')
    # desired_caps['app'] = 'com.oppo.launcher3'
    desired_caps['appPackage'] = 'com.oppo.launcher3'
    desired_caps['appActivity'] = '.Launcher'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noRest'] = True
    desired_caps['automationName'] = 'uiautomator2'

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    return driver
if __name__ == '__main__':
    init_Android_driver()