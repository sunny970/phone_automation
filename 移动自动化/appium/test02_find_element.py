from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 初始化
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'

# 创建手机对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# 打开应用对象
driver.start_activity('com.android.settings','.Settings')
# 查找元素
# driver.implicitly_wait(10)
# driver.find_element_by_id('com.android.settings:id/search').click()
sleep(10)
# driver.find_element_by_class_name('android.widget.ImageButton').click()
# sleep(2)
# driver.find_element_by_xpath("//*[contains(@content-desc,'收起')]").click()
# 设置超时等待
ele = WebDriverWait(driver,10).until(lambda x:x.find_element_by_class_name("android.widget.ImageButton"))
ele.click()


# driver.back()
# driver.back()
# driver.back()















