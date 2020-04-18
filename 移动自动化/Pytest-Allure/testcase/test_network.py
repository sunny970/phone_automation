import time
from time import sleep

import allure
import pytest
from base.base_driver import init_driver
from page.network_page import Network_Page


class Test_Network:
    def setup(self):
        self.driver = init_driver()
        self.network_page = Network_Page(self.driver)
    # @allure.title("标题")
    @allure.feature("一级标题")
    @allure.story("二级标题")
    @allure.description("测试描述")
    @allure.link(url='http://www.baidu.com',name="error_link")
    # 连接allure.link    allure.issue   allure.testcase
    @allure.severity(allure.severity_level.BLOCKER)
    # 优先级(严重级别): BLOCKER    CRITICAL   NORMAL   MINOR  TRIVIAL
    @allure.step(title="2G测试")
    @pytest.mark.run(order=2)
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

    @allure.step(title="3G测试")
    def test_network_3g(self):
        # 点击更多
        # allure.attach("","")添加附件
        allure.attach("找到xx1按钮点击","点击更多")
        self.network_page.click_more()
        # 点击移动网络
        allure.attach( "找到xx2按钮点击","点击移动网络")
        self.network_page.click_move_network()
        # 点击首选类型
        allure.attach( "找到xx3按钮点击","点击首选类型")
        self.network_page.click_first_type()
        # 点击3G
        allure.attach( "找到xx4按钮点击","点击3G")
        allure.attach("图片", open("./image/"+ xxxx +".png","rb").read(),allure.attachment_type.PNG)  # 上传图片
        self.network_page.click_3g()

        now_time = time.strftime('%Y-%m-%d %H-%M-%S')
        self.driver.get_screenshot_as_file('./image/%s.png' % now_time)

        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)

if __name__ == '__main__':
    pytest.main()


