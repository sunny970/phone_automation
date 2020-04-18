import time
from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

x = 600
y = 988
int(x)
int(y)

desired_caps = { }
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'
# desired_caps['deviceName'] = '10.4.226.163:5555'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# print(driver.current_package)
# print(driver.current_activity)
# driver.start_activity("com.android.settings",".Settings")
sleep(2)
# driver.find_element_by_xpath("//*[contains(@text,'应用')]").click()
# sleep(5)
# driver.swipe(300,900,300,100)


# 滑动swipe(初始x,初始y,目标x,目标y,滑动时间(默认None))-->具有惯性
print(time.time())
driver.swipe(500,450,100,450)
print(time.time())
sleep(5)
driver.swipe(100,450,500,450)

# # scroll 滑动:从元素一滑动到元素二  -->具有惯性
# ele1 = driver.find_element_by_xpath("//*[contains(@text,'相机')]")
# ele2 = driver.find_element_by_xpath("//*[contains(@text,'图库')]")
# driver.scroll(ele1,ele2)
# sleep(3)

# # drag_and_drop  滑动:从元素一滑动到元素二  -->无惯性
# ele1 = driver.find_element_by_xpath("//*[contains(@text,'相机')]")
# ele2 = driver.find_element_by_xpath("//*[contains(@text,'短信')]")
# driver.drag_and_drop(ele1,ele2)
# driver.drag_and_drop(ele1,ele2)
# driver.drag_and_drop(ele1,ele2)
# driver.drag_and_drop(ele1,ele2)
# sleep(3)
# WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'关于手机')]")).click()
#
# print(driver.find_elements_by_class_name('android.widget.TextView'))
# for i in driver.find_elements_by_class_name('android.widget.TextView'):
#     # if i.text == '6.0':
#     if "6.0" in i.text:
#         print("yes")
#         break
# else:
#     print("no")

# # 持续滑动知道找到控件点击停止
# while True:
#     try:
#         driver.find_element_by_xpath("//*[contains(@text,'Launcher3')]").click()
#         break
#     except Exception:
#         driver.swipe(300,900,300,500,5000)

# driver.quit()
