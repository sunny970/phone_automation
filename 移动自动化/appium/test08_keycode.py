from time import sleep

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# print(driver.current_package)
# print(driver.current_activity)
# driver.start_activity('com.Android.settings','.Settings')
for i in range(3):
    driver.keyevent(24)
    sleep(1)
for i in range(2):
    driver.keyevent(25)
    sleep(1)

driver.open_notifications()
sleep(1)
driver.keyevent(4)

print(driver.network_connection)

driver.set_network_connection(0)

# driver.start_activity('com.android.settings','.Settings')
# driver.get_screenshot_as_file("./设置元素/xxx.png")

# driver.find_element_by_xpath("//*[contains(@content-desc,'应用')]").click()
driver.keyevent(84)


sleep(5)
driver.keyevent(3)


