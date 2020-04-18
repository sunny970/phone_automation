from time import sleep

import pytest

from test_base.base_yml_read import yml_read
from test_base.base_driver import init_Android_driver
from test_page.wy_page import WyPage

def data_with_key(key):
    return yml_read("data_wy",key)

class TestWy:
    def setup(self):
        self.driver = init_Android_driver()
        self.wy_page = WyPage(self.driver)

    @pytest.mark.parametrize('args',data_with_key('test_search_play_song'))
    def test_search_play_song(self,args):
        pass
        # 点击网易云音乐
        self.wy_page.click_wy()
        # 点击搜索
        self.wy_page.click_search()
        # 输入歌名
        self.wy_page.input_words(args["input_words"])
        # 点击enter
        self.wy_page.click_enter()
        # 点击进行播放
        self.wy_page.click_play()
        # 点击桌面查看歌词
        self.wy_page.view_lyric()
        # 截图
        self.wy_page.get_pic()

    def teardown(self):
        sleep(3)
        self.driver.keyevent(3)
