import unittest, logging

from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestIHRMLoginPara(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()  # 初始化登录类

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        # 调用封装的登录接口
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登陆: {}'.format(jsonData))  # 日志输出格式化只能用{}，不可用
        # 断言
        assert_common(self, response, http_code, success, code, message)

