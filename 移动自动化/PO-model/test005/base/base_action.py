class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])


    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)