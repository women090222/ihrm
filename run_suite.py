import unittest

from script.test_emp import TestIHRMEmp
from script.test_login import TestIHRMLogin
import app
import time
from tools.HTMLTestRunnerCN import HTMLTestReportCN
from script.login import Login
from script.test_login import TestIHRMLogin

# 1.初始化测试套件
suite = unittest.TestSuite()
# 2.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# suite.addTest(unittest.makeSuite(TestIHRMLogin))

# 3.使用HTMLTestRunner执行测试套件,生成测试报告
report_path = app.BASE_DIR + '/report/ihrm{}.html'.format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:
    # 初始化HTMLRunner
    runner = HTMLTestReportCN(f, verbosity=2, title='IHRM人力资源接口测试', description='V1.0.0')
    # 使用Runner运行测试套件
    runner.run(suite)
