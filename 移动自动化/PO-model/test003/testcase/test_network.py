from time import sleep
import pytest
from base.base_driver import init_driver
from page.network_page import Network_Page


class Test_Network:
    def setup(self):
        self.driver = init_driver()
        self.network_page = Network_Page(self.driver)

    def test_network_2g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型
        self.network_page.click_first_type()
        # 点击2G
        self.network_page.click_2g()


        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_network_3g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型
        self.network_page.click_first_type()
        # 点击3G
        self.network_page.click_3g()


        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)

if __name__ == '__main__':
    pytest.main()


