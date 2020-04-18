from appium import webdriver

def init_driver(port):
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = "8.1"
    desired_caps['deviceName'] = '10.19.42.87:5555'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # desired_caps['appPackage'] = 'com.netease.cloudmusic'
    # desired_caps['appActivity'] = '.activity.MainActivity'
    # desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True
    desired_caps['automationName'] = 'uiautomator2'

    driver = webdriver.Remote("http://localhost:"+ port +"/wd/hub",desired_caps)
    return driver
if __name__ == '__main__':
    init_driver("4723")