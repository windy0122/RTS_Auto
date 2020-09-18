from tools.test_receipt import TestHttpRequest
import unittest
from tools.project_path import *
import HTMLTestRunner_cn
from tools.do_email import DoEmail


# def run(test_data):
#     for item in test_data:
#         # print(item['case_id'])
#         print('现在正在执行的测试用例是:{0}'.format(item['title']))
#         res = HttpRequest().http_request(item['url'], json.dumps(eval(item['data'])),
#                                          item['http_method'], eval(item['header']))
#         print('请求的结果是：{0}'.format(res.json()))
#         DoExcel().write_back('D:/Api_Auto/test_data/uat_data.xlsx', 'login', int(item['case_id'])+1, str(res.json()))
#
#
# test_data_login = DoExcel.get_data('D:/Api_Auto/test_data/uat_data.xlsx', 'login')
# run(test_data_login)

suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path, 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file, title='自动化测试', description='测试报告', tester='吴迪')
    runner.run(suite)

# DoEmail().send_email()

