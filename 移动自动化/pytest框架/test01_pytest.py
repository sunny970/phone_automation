import pytest

def test01():
    print("正在整理1.....")

def test02():
    print("正在整理2.....")

def setup():
    print("setup")

def teardown():
    print("teardown")

if __name__ == '__main__':
    # pytest.main("-s test01_pytest.py")
    pytest.main(["-s","test01_pytest.py"])
    # pytest.main()










