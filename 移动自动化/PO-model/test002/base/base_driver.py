from appium import webdriver

def init_driver():
    a = {}
    a['platformName'] = 'Android'
    a['platformVersion'] = '6.0'
    a['deviceName'] = '192.168.208.101:5555'
    a['unicodeKeyboard'] = True
    a['resetKeyboard'] = True
    a['appPackage'] = 'com.android.settings'
    a['appActivity'] = '.Settings'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', a)
    driver.implicitly_wait(10)
    return driver
if __name__ == '__main__':
    init_driver()