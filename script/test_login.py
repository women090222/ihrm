import unittest, logging

from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
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

    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登录成功接口返回的数据为: {}'.format(jsonData))  # 日志输出格式化只能用{}，不可用
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success的值
        # self.assertEqual(10000, jsonData.get('code'))  # 断言code的值
        # self.assertIn('操作成功', jsonData.get('message'))  # 断言message的值
        assert_common(self, response, 200, True, 10000, '操作成功')

    def test02_username_is_not_exists(self):
        # 调用封装的登录接口
        response = self.login_api.login('13900000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('账号不存在时输出的数据为: {}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_password_is_error(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('密码错误时输出的数据为: {}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        # 调用封装的登录接口
        response = self.login_api.login('131131131!@', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('账号输入特殊字符时输出的数据为: {}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_null(self):
        response = self.login_api.login('', 'error')
        jsonData = response.json()
        logging.info('账号为空时输出的数据为: {}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_password_is_null(self):
        response = self.login_api.login('13800000002', '')
        jsonData = response.json()
        logging.info('密码为空时输出的数据为: {}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_username_have_chinese(self):
        response = self.login_api.login('138你好123123', '123456')
        jsonData = response.json()
        logging.info('账号中有中文输出的数据: {}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test08_username_midder_have_space(self):
        response = self.login_api.login('138   02', '123456')
        jsonData = response.json()
        logging.info('账号中有空格输出的数据: {}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
