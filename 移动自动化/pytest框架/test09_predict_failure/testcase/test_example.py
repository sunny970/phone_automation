

import pytest
class Test001(object):
    # 预计 成功  结果  成功
    # 预计 成功  结果  失败
    # 预计 失败  结果  成功
    # 预计 失败  结果  失败
    @pytest.mark.xfail(False, reason="想让他成功")  # --->结果-成功-pass
    def test001(self):
        print("111")

    @pytest.mark.xfail(False,reason="想让他成功")  # --->结果-失败-fail
    def test003(self):
        print("333")
        assert False

    @pytest.mark.xfail(True,reason="想让他失败")  # --->结果-成功-xpass
    def test004(self):
        print("444")
        assert 1

    @pytest.mark.xfail(True,reason="想让他失败")  # --->结果-失败-xfail
    def test005(self):
        print("555")
        assert 0


if __name__ == '__main__':
    pytest.main()
