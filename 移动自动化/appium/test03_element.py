from time import sleep

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'
desired_caps['unicodekeyboard'] = True
desired_caps['resetkeyboard'] = True
# 创建手机对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# 打开应用对象
driver.start_activity('com.android.settings','.Settings')
sleep(5)
# driver.find_element_by_id('com.android.settings:id/search').click()
# ele = driver.find_element_by_xpath("//*[contains(@text,'搜索…')]")
# ele.send_keys('s')
# sleep(3)
# ele.clear()
# driver.find_element_by_id('android:id/search_close_btn').click()

# eles = driver.find_elements_by_id('com.android.settings:id/title')
# for i in eles:
#     print(i.text)

# eles = driver.find_elements_by_id('com.android.settings:id/title')[3]
# print(eles.get_attribute('name'))
# print(eles.get_attribute('text'))
# print(eles.get_attribute('class'))
# print(eles.get_attribute('classname'))
# print(eles.get_attribute('resourceid'))
#
# print(eles.location)