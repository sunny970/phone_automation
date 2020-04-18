





class Display_Page:
    def __init__(self,driver):
        self.driver = driver

    def click_search(self):
        self.driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()

    def input_words(self,text):
        self.driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys(text)

    def back_a(self):
        self.driver.keyevent(4)


