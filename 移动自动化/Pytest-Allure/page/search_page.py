import os , sys

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):


    # search_botton = (By.XPATH, "//*[contains(@content-desc,'搜索')]")
    search_botton = (By.XPATH, "content-desc,搜索")
    # input_botton = (By.XPATH, "//*[contains(@text,'搜索')]")
    input_botton = (By.XPATH, "text,搜索")
    # back_botton = (By.XPATH, "//*[contains(@content-desc,'收起')]")
    back_botton = (By.XPATH, "content-desc,收起")


    def click_search(self):
        self.click(self.search_botton)


    def input_content(self,text):
        self.input_text(self.input_botton,text)


    def click_back_s(self):
        self.click_back(self.back_botton)
