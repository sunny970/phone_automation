
import os , sys
sys.path.append(os.getcwd())
import allure
from time import sleep
import pytest

from base.base_driver import init_driver

from page.display_page import Display_Page


class Test_Display:

    def setup(self):
        self.driver = init_driver()
        self.display_page = Display_Page(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    # 严重级别: BLOCKER    CRITICAL   NORMAL   MINOR  TRIVIAL
    def test_mobile_display_input(self):
        # 点击搜索
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_words("hello")
        # 返回
        self.display_page.back_a()
        # self.driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys("hello")
        # self.driver.back()
        print("返回...")


    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)

if __name__ == '__main__':
    pytest.main()


