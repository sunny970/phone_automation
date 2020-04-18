import pytest
class Test001(object):

    @pytest.mark.run(order=1)
    def test001(self):
        print("111")

    @pytest.mark.run(order=2)
    def test002(self):
        print("222")

    @pytest.mark.run(order=5)
    def test005(self):
        print("555")

    @pytest.mark.run(order=3)
    def test003(self):
        print("333")

    @pytest.mark.run(order=4)
    def test004(self):
        print("444")

if __name__ == '__main__':
    pytest.main()
