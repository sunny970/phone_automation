from selenium.webdriver.common.by import By


class Display_Page:

    search = By.XPATH,"//*[contains(@content-desc,'搜索')]"
    search_A = By.XPATH,"//*[contains(@text,'搜索')]"



    def __init__(self,driver):
        self.driver = driver

    def find_element_a(self,loc):
        return self.driver.find_element(loc[0],loc[1])

    def click_search(self):
        self.find_element_a(self.search).click()
        # self.driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()

    def input_words(self,text):
        self.find_element_a(self.search_A).send_keys(text)
        # self.driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys(text)

    def back_a(self):
        self.driver.keyevent(4)


