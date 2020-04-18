
import pytest
class Test001(object):


    def test001(self):
        print("111")


    def test002(self):
        print("222")
        assert 1

    @pytest.mark.skipif(True,reason="不想测试了")
    def test003(self):
        print("333")
        assert True

    def test004(self):
        print("444")

if __name__ == '__main__':
    pytest.main()
