# import os , sys
# sys.path.append(os.getcwd())

from time import sleep
import pytest
from base.base_driver import init_driver
class Test_Display:
    def setup(self):
        self.driver = init_driver()

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


