from appium import webdriver
import pytest

class Test01(object):
    # 初始化
    def setup_class(self):
        print("setup执行")
        desired_caps = { }

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.208.101:5555'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 创建手机对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        # 设置隐式等待
        self.driver.implicitly_wait(10)

    # 参数化
    # @pytest.mark.parametrize(("key1","key2"), [("value1", "value2"),("x","x")])  # -->多个参数
    @pytest.mark.parametrize("keys",["1","2","5"])  # -->单个参数
    def test_001(self,keys):
        print("测试执行%s" % keys)
        driver = self.driver
        driver.start_activity('com.android.settings','.Settings')
        driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()
        driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys(keys)

    def teardown_class(self):
        print("teardown执行")
        self.driver.keyevent(3)
        self.driver.quit()




if __name__ == '__main__':
    pytest.main()