from selenium.webdriver.common.by import By

from base_action import BaseAction

class WyPage(BaseAction):

    search_button = (By.XPATH,"text,搜索")
    input_button = (By.XPATH,"text,搜索")


    # 点击搜索
    def click_search(self):
        self.click(self.search_button)
    # 输入歌名
    def input_words(self,text):
        self.input_text(self.input_button,text)
    # 截图
    def get_pic(self):
        self.get_screenshot("网易")

#
# delimitter$$
# create procedure myproc_a(a int)
# begin
# declare i int;
# set i=1;
# while i<=a do
#     insert into xxx values(x,x,x);
# set i=i+1;
# end while;
# end$$
#
# call myproc_a(10);



