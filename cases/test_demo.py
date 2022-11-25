import pytest
import requests


@pytest.mark.P1
class TestDemo:

    def test_demo(self):
        """请求百度"""
        res = requests.get("http://www.baidu.com")
        assert res.status_code == 200
