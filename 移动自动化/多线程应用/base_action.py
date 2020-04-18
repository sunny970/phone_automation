from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    def make_xpath_with_unit_feature(self,loc):

        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(',')
        feature = ""
        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        return feature

    def make_xpath_with_feature(self,loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""
        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)
        feature = feature.rstrip("and ")
        loc = feature_start + feature + feature_end
        return loc

    def find_element(self,loc,timeout=20.0,poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(by,value))

    def find_elements(self,loc,timeout=5.0,poll=0.1):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(by,value))

    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)

    def scroll_page_once(self, diretion='down'):
        window_size = self.driver.get_window_size()
        window_height = window_size["height"]
        window_width = window_size['width']
        up_y = window_height * 0.25
        down_y = up_y * 3
        left_x = window_width * 0.25
        rigth_x = left_x * 3
        center_x = window_width * 0.5
        center_y = window_height * 0.5
        if diretion == "down":
            self.driver.swipe(center_x, down_y, center_x, up_y)
        elif diretion == 'up':
            self.driver.swipe(center_x, up_y, center_x, down_y)
        elif diretion == 'left':
            self.driver.swipe(left_x, center_y, rigth_x, center_y)
        elif diretion == 'right':
            self.driver.swipe(rigth_x, center_y, left_x, center_y)
        else:
            raise Exception('请输入正确的diretion参数')

    def get_screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./" + file_name + ".png")

    def find_toast(self, message, timeout=5.0, poll=0.1):
        message = "//*[contains(@text,'" + message + "')]"
        toast = self.find_element((By.XPATH, message), timeout, poll)
        return toast.text

    def is_toast_exist(self, message, timeout=5.0, poll=0.1):
        try:
            self.find_toast(message, timeout, poll)
            return True
        except Exception:
            return False
