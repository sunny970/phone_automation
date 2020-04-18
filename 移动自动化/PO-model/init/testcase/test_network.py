from time import sleep

import pytest
from base.base_driver import init_driver

class Test_Network:
    def setup(self):
        self.driver = init_driver()

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

    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)

if __name__ == '__main__':
    pytest.main()


