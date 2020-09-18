from ddt import ddt, data   # 数据类型必须是列表嵌套列表，或者列表嵌套字典
import unittest
from tools.http_request import HttpRequest
import tools.api_logging
import tools.project_path as tool_path
from tools.do_excel import DoExcel
import logging
from tools.common import StartBefore

# my_logger = MyLog()
test_data = DoExcel.get_data(tool_path.test_data_path)


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_receipt(self, item):
        res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'], eval(item['header']))
        res_val = res.json()
        # print(res_val)
        try:
            self.assertEqual('0', res.json()['success'])
            print(res.json())
            TestResult = 'PASS'

            # 将新建的顾客写入到test文件的init表中
            if 'id' in res_val['val']:
                StartBefore().write_back_init(tool_path.test_data_path, 'init', 1, res.json()['val']['id'])

            # 通过顾客卡接口，将顾客卡id，写入到init表中
            StartBefore().write_customer_card_id(res_val)

        except AssertionError as e:
            TestResult = 'FAILED'
            logging.exception('执行出错：{0}'.format(e))
            print(res.json())
            raise e
        finally:
            StartBefore.write_back(tool_path.test_data_path, item['sheet_name'], int(item['case_id']) + 1, str(res.json()),TestResult)
            logging.info('获取的结果是：{0}'.format(res.json()['msg']))










