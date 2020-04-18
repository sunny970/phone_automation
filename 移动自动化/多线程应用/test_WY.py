import threading

import pytest

from base_driver import init_driver
from wy_page import WyPage

# def data_with_key(key):
#     return yml_read("data_wy",key)




class Test_a:


    def do_test_search_play_song(self,port):
        self.driver = init_driver(port)
        wy_page = WyPage(self.driver)
        print(self.driver.device_time)
        # 点击搜索
        wy_page.click_search()
        # 输入歌名
        if port=="4723":
            wy_page.input_words(u"嚣张")
        elif port=="4725":
            wy_page.input_words(u"hello,world")

        # if port == "4723":
        #     # 点击桌面查看歌词
        #     wy_page.view_lyric()
        #
        # elif port == "4724":
        #     # 截图
        #     wy_page.get_pic()

    def test_search_play_song(self):

        ports = ["4723"]
        for i in ports:
            threading.Thread(target=Test_a().do_test_search_play_song,args=(i,)).start()


if __name__ == '__main__':
    pytest.main()
