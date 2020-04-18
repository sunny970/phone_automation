import pytest

class Test01(object):
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")

class Test02(object):
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup1")

    def teardown(self):
        print("teardown1")

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")

if __name__ == '__main__':
    pytest.main(["-s","test02_setup&teardown.py"])









