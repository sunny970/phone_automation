import pytest

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_read_yml import yml_read

def data_with_key(key):
    return yml_read("search_data")[key]



class TestSearch:
    def setup(self):

        self.driver = init_driver()

        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("text",data_with_key("test_search1"))
    def test_search(self,text):
        self.search_page.click_search()
        self.search_page.input_content(text)

        self.search_page.get_screenshot("aaa")

        self.search_page.click_back_s()
        self.driver.keyevent(4)
