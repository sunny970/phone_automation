from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platdormVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# print(driver.current_package)
# print(driver.current_activity)
driver.start_activity('com.android.settings','.ChooseLockPattern')
# TouchAction(driver).press(x=210,y=258).move_to(x=90,y=0).move_to(x=90,y=0).move_to(x=0,y=90).move_to(x=0,y=90).move_to(x=-90,y=0).move_to(x=0,y=-90).perform()
# TouchAction(driver)\
#     .press(x=210,y=258)\
#     .move_to(x=300,y=258)\
#     .move_to(x=390,y=258)\
#     .move_to(x=390,y=348)\
#     .move_to(x=390,y=438)\
#     .move_to(x=300,y=438)\
#     .move_to(x=300,y=348)\
#     .move_to(x=210,y=438)\
#     .release().perform()

(TouchAction(driver)
 .press(x=210,y=258)
 .move_to(x=300,y=258)
 .move_to(x=390,y=258)
 .move_to(x=390,y=348)
 .move_to(x=390,y=438)
 .move_to(x=300,y=438)
 .move_to(x=300,y=348)
 .move_to(x=210,y=438)
 .release().perform())






































































