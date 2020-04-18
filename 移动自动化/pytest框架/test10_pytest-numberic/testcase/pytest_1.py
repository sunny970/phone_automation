from time import sleep

import pytest
from appium import webdriver


class Test01:

    def setup(self):

        desired_caps = { }

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.208.101:5555'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    @pytest.mark.parametrize("keys", ["1", "2"])
    def test_001(self,keys):
        driver = self.driver
        driver.start_activity('com.android.settings','.Settings')
        driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()
        driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys(keys)

    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)


if __name__ == '__main__':
    pytest.main()