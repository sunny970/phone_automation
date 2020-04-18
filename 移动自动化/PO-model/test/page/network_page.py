
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class Network_Page(BaseAction):

    more = (By.XPATH,"//*[contains(@text,'更多')]")
    move_network = (By.XPATH, "//*[contains(@text,'移动网络')]")
    first_chose = (By.XPATH, "//*[contains(@text,'首选网络类型')]")
    two_G = (By.XPATH, "//*[contains(@text,'2G')]")
    three_G = (By.XPATH, "//*[contains(@text,'3G')]")


    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)

        # self.driver = driver

    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])




    # 点击更多
    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.find_element(self.more).click()
        self.click(self.more)

    # 点击移动网络
    def click_move_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.find_element(self.move_network).click()
        self.click(self.move_network)

    # 点击首选类型
    def click_first_type(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.find_element(self.first_chose).click()
        self.click(self.first_chose)

    # 点击2G
    def click_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        # self.find_element(self.two_G).click()
        self.click(self.two_G)

    # 点击3G
    def click_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        # self.find_element(self.three_G).click()
        self.click(self.three_G)

