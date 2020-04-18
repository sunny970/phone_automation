import pytest
from appium import webdriver

# 初始化连接手机应用
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
# desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = '192.168.208.101:5555'
# desired_caps['deviceName'] = '10.4.226.163:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 创建手机对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# 截图
driver.get_screenshot_as_file("./image/%s.png")