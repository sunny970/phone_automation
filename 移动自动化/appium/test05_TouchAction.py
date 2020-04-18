from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
driver.start_activity('com.android.settings','.Settings')

# driver.swipe(500,450,100,450)
# ele = driver.find_element_by_xpath("//*[contains(@text,'Discard')]")
# TouchAction(driver).press(ele).wait(5000).release().perform()
# TouchAction(driver).press(x=500,y=900).wait(5000).release().perform()

# ele = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# TouchAction(driver).tap(ele).perform()
# TouchAction(driver).tap(x=400,y=500).perform()

# driver.swipe(300,0,300,400)
# TouchAction(driver).tap(x=300,y=10).tap(x=300,y=170).perform()
# driver.back()

# driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
# ele = driver.find_element_by_xpath("//*[contains(@text,'Wired')]")
# TouchAction(driver).long_press(ele).perform()




































