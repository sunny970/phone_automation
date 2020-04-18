from selenium.webdriver.common.by import By

from test_base.base_action import BaseAction

class WyPage(BaseAction):

    wy_button = (By.XPATH,"text,网易云")
    search_button = (By.XPATH,"text,搜索")
    input_button = (By.XPATH,"text,En")
    item = (By.ID,'com.netease.cloudmusic:id/songNameAndInfoArea')


    # 点击网易云音乐
    def click_wy(self):
        self.click(self.wy_button)
    # 点击搜索
    def click_search(self):
        self.click(self.search_button)
    # 输入歌名
    def input_words(self,text):
        self.input_text(self.input_button,text)
    # 点击enter
    def click_enter(self):
        self.driver.keyevent(66)
    # 点击进行播放
    def click_play(self):
        self.click(self.item)
    # 点击桌面查看歌词
    def view_lyric(self):
        self.click(self.item)
    # 截图
    def get_pic(self):
        self.get_screenshot("网易")