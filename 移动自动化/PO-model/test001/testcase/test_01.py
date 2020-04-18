from time import sleep

import pytest
from appium import webdriver

class Test_setting:
    def setup(self):
        a = {}
        a['platformName'] = 'Android'
        a['platformVersion'] = '6.0'
        a['deviceName'] = '192.168.208.101:5555'
        a['unicodeKeyboard'] = True
        a['resetKeyboard'] = True
        a['appPackage'] = 'com.android.settings'
        a['appActivity'] = '.Settings'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',a)
        self.driver.implicitly_wait(10)
    def test_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def test_mobile_display_input(self):
        self.driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys("hello")
        self.driver.back()
        print("返回...")


    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)

if __name__ == '__main__':
    pytest.main()


