


class Network_Page:
    def __init__(self,driver):
        self.driver = driver

    # 点击更多
    def click_more(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
    # 点击移动网络
    def click_move_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    # 点击首选类型
    def click_first_type(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
    # 点击2G
    def click_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
    # 点击3G
    def click_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()