import pytest

from test_base.base_read_yml import yml_read

def data_with_key(key):
    return yml_read("data_login",key)



class TestLogin:
    # def setup(self):
    #
    #     self.driver = init_driver()
    #
    #     self.page_login = Pagelogin(self.driver)

    @pytest.mark.parametrize("args",data_with_key("test_case_name_01"))
    def test_login(self,args):
        print(args["username"])
        print(args["password"])

    @pytest.mark.parametrize("args", data_with_key("test_case_name_02"))
    def test_login_up(self, args):
        print(args["username"])
        print(args["password"])
        print(args["number"])


        # self.page_login.click_search()
        # self.page_login.input_content(text)
        # self.page_login.click_back_s()
        # self.driver.keyevent(4)
