# # def move(n, a, b, c):
# #     if n == 1:
# #         print(a, '--->', c)
# #
# #     else:
# #         move(n-1, a, c, b)
# #         print(a, '--->', c)
# #         move(n-1, b, a, c)
# #
# #
# # move(3, 'A', 'B', 'C')
#
# # L1 = [1]
# # L2 = [1]
# #
# # print(L1 + L2)
#
# # 杨辉三角
# # def triangles():
# #     line = [1]         # 第一行就一个元素1
# #     while True:
# #         yield line
# #         # 生成下一行，表达式为 : [1] + 上一行的两个元素之和 + [1]
# #         line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
# #
# #
# # n = 0
# # results = []
# # for t in triangles():
# #     results.append(t)
# #     n = n + 1
# #     if n == 10:
# #         break
# #
# # for t in results:
# #     print(t)
#
#
# # def f(x):
# #     return x * x
# #
# #
# # r = map(f, [1,2,3,4,5,6,7])
# # print(list(r))
#
# # def char2num(s):
# #     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# #     return digits[s]
# #
# #
# # print(char2num('2'))
#
# # a = 'hello'
# # b = 'world'
# # print(a.replace(a[:3], ''))
#
# # coins = [2, 3, 10]
# #
# # count = 0
# # for i in coins:
# #     if i > 2:
# #         if i % 2 == 0:
# #             count += (i//2)
# #         else:
# #             count =+ ((i//2)+1)
# #     else:
# #         count += 1
# #
# # print(count)
#
#
# # class Fib(object):
# #     def __init__(self):
# #         self.a, self.b = 0, 1
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         self.a, self.b = self.b, self.a+self.b
# #         if self.a > 1000:
# #             raise StopIteration
# #         return self.a
# #
# #
# # if __name__ == '__main__':
# #
# #     for i in Fib():
# #         print(i)
#
#
# # __getitem__
# # class Fib(object):
# #     def __getitem__(self, n):
# #         a, b = 1, 1
# #         for x in range(n):
# #             a, b = b, a+b
# #         return a
# #
# #
# # if __name__ == '__main__':
# #     f = Fib()
# #     print(f[5])         # 8
# #     print(f[0:5])       # 'slice' object cannot be interpreted as an integer
#
#
# # 判断传入参数
# # class Fib(object):
# #     def __getitem__(self, n):
# #         if isinstance(n, int):
# #             a, b = 1, 1
# #             for i in range(n):
# #                 a, b = b, a+b
# #             return a
# #
# #         if isinstance(n, slice):
# #             start = n.start
# #             stop = n.stop
# #             if start is None:
# #                 start = 0
# #             a, b = 1, 1
# #             L = []
# #             for x in range(stop):
# #                 if x >= start:
# #                     L.append(a)
# #                 a, b = b, a+b
# #             return L
# #
# #
# # if __name__ == '__main__':
# #     f = Fib()
# #     print(f[0:5])       # [1, 1, 2, 3, 5]
#
#
# # __getattr__
#
# # class Student(object):
# #     def __init__(self):
# #         self.name = '吴迪'
# #
# #     def __getattr__(self, attr):
# #         if attr == 'score':
# #             return 99
# #
# #
# # if __name__ == '__main__':
# #     s = Student()
# #     print(s.name)
# #     print(s.score)
#
#
# # def numberOfSteps(num: int) -> int:
# #     n = 0
# #     num_new = num
# #     while num_new != 0:
# #         if num % 2 == 0:
# #             n += 1
# #             num_new = num_new // 2
# #         else:
# #             n += 1
# #             num_new = num_new - 1
# #     return n
# #
# #
# # print(numberOfSteps(14))
#
# # 装饰器
#
# import logging
#
#
# # def use_logging(func):
# #
# #     def wrapper(*args, **kwargs):
# #         logging.warning('%s is running' % func.__name__)
# #         return func(*args, **kwargs)
# #
# #     return wrapper
# #
# #
# # @use_logging
# # def foo(name):
# #     print('i am ' + name)
# #
# #
# # foo('wudi')
#
#
# # 带参数的装饰器
#
# # def use_logging(level):
# #
# #     def decorator(func):
# #
# #         def wrapper(*args, **kwargs):
# #             if level == 'warning':
# #                 logging.warning('%s is running' % func.__name__)
# #             elif level == 'info':
# #                 logging.info('%s is running' % func.__name__)
# #             return func(*args, **kwargs)
# #
# #         return wrapper
# #
# #     return decorator
# #
# #
# # @use_logging('warning')
# # def foo(name):
# #     print('i am ' + name)
# #
# #
# # foo('wudi')
#
#
# # 上下文文件管理器
#
# # class MyOpen(object):
# #     def __init__(self, file_name, open_method, encoding='utf-8'):
# #         self.file_name = file_name
# #         self.open_method = open_method
# #         self.encoding = encoding
# #
# #     def __enter__(self):
# #         # noinspection PyTypeChecker
# #         # noinspection PyUnresolvedReferences
# #         self.f = open(self.file_name, self.open_method, encoding=self.encoding)
# #         return self.f
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         # exc_type, exc_val, exc_tb可以提取异常信息
# #         print(exc_type)
# #         print(exc_val)
# #         print(exc_tb)
# #         self.f.close()
# #
# #
# # with MyOpen('test.txt', 'r') as f:
# #     content = f.read()
# #     print(content)
# #     print(name)
# #     '''
# #     Traceback (most recent call last):
# #     <class 'NameError'>
# #     name 'name' is not defined
# #     <traceback object at 0x0000024B65F5A4C0>
# #     File "E:/Web_Auto_Xiaomi/exercise.py", line 240, in <module>
# #     print(name)
# #     NameError: name 'name' is not defined
# #     '''
#
#
# import requests
# import json
# #
# # url = 'https://uatleague.round-table-union.com/api/rts/member/membershipCard/deleteMembershipCard/V141'
# #
# # header = {'content-type': 'application/json',
# #           'version': '1.4.1',
# #           'platform': 'iOS',
# #           'tk': '4b755461-1bfa-4f3d-9945-5ce7f46aa105'}
# #
# # data = {
# #          "customerId": "463765417308680192",
# #          "customerType": "0",
# #          "receiptItem": [{
# #           "serviceEmployee": [],
# #           "itemSubName": "洗洗洗洗",
# #           "itemName": "洗吹",
# #           "itemCount": 1,
# #           "itemPrice": "20.00",
# #           "itemSubId": "463767356746289152",
# #           "itemNameId": "5",
# #           "countingPayment": [{
# #            "customerCardId": "503612192538357760",
# #            "cardType": "2",
# #            "cardCount": "1"
# #           }]
# #          }],
# #          "gender": "0",
# #          "receiptPayment": [],
# #          "billingTime": 1600237002307.178
# # }
# #
#
# # payload = {'membershipCardId': '504291768767737856'}
# #
# # r = requests.get(url, headers=header, params=payload)
# # # #
# # # res = json.loads(r.text)
# # # print(payload)
# # print(r.url)
# # print(r.json())
# # for i in res['val']:
# #     print(i['cardType'])
# #
# # # for i in r.json()['val']:
# # #     if i['cardType'] == '1':
# # #         print('true')
# # #     else:
# # #         print('false')
# #
# # # Li = [1, 2, 3, 4, 5]
# # # n = 6
# # # if n in Li:
# # #     print(n)
# #
# #
# # # res = {
# # #         "msg": "操作成功",
# # #         "requestUUID": "JY-7959f4aae4d63b20e69ccd77eb342fb7",
# # #         "responseTime": "2020-09-17 11:27:59",
# # #         "ret": "0",
# # #         "success": "0",
# # #         "val": [{
# # #             "addCashEventStatus": "0",
# # #             "applicableItemId": "5",
# # #             "applicableItemName": "洗吹",
# # #             "applicableSpecificItemId": "",
# # #             "applicableSpecificItemName": "全部洗吹项目",
# # #             "averagePrice": "20.00",
# # #             "balanceAmount": "0",
# # #             "balanceGiftAmount": "0",
# # #             "balanceRechargeAmount": "0",
# # #             "balanceTimes": "100",
# # #             "cardName": "计次卡测试",
# # #             "cardType": "2",
# # #             "deleteYn": "1",
# # #             "enjoyDiscount": "",
# # #             "expireTime": "253402271999000",
# # #             "giftAmount": "",
# # #             "lastAveragePrice": "20.00",
# # #             "memberCardTemplateId": "503611922391625728",
# # #             "membershipCardCode": "VIP00030",
# # #             "membershipCardId": "503931087002398720",
# # #             "membershipCardStatus": "1",
# # #             "purchasePrice": "2000.0000",
# # #             "purchaseTimes": "100",
# # #             "rechargeAmount": "",
# # #             "upgradeYn": "0",
# # #             "useMonth": "9999"
# # #         }, {
# # #             "addCashEventStatus": "0",
# # #             "applicableItemId": "",
# # #             "applicableItemName": "",
# # #             "applicableSpecificItemId": "",
# # #             "applicableSpecificItemName": "",
# # #             "averagePrice": "",
# # #             "balanceAmount": "0",
# # #             "balanceGiftAmount": "0",
# # #             "balanceRechargeAmount": "0",
# # #             "balanceTimes": "0",
# # #             "cardName": "年卡1",
# # #             "cardType": "3",
# # #             "deleteYn": "1",
# # #             "enjoyDiscount": "95",
# # #             "expireTime": "1631807999000",
# # #             "giftAmount": "",
# # #             "lastAveragePrice": "",
# # #             "memberCardTemplateId": "463767922616791040",
# # #             "membershipCardCode": "VIP00031",
# # #             "membershipCardId": "503931208406528000",
# # #             "membershipCardStatus": "1",
# # #             "purchasePrice": "1000.0000",
# # #             "purchaseTimes": "0",
# # #             "rechargeAmount": "",
# # #             "upgradeYn": "0",
# # #             "useMonth": "12"
# # #         }]
# # #     }
# # #
# # # for i in res['val']:
# # #     print(i['cardType'])
#
#
# from tools.project_path import *
# from tools.do_excel import DoExcel
# import logging
#
# # res_val2 = {
# #         'msg': '操作成功',
# #         'requestUUID': 'JY-0278a8f73dab0a6a746652f59ceab323',
# #         'responseTime': '2020-09-18 10:06:01',
# #         'ret': '0',
# #         'success': '0',
# #         'val': [{
# #             'addCashEventStatus': '0',
# #             'applicableItemId': '',
# #             'applicableItemName': '',
# #             'applicableSpecificItemId': '',
# #             'applicableSpecificItemName': '',
# #             'averagePrice': '',
# #             'balanceAmount': '1000.0000',
# #             'balanceGiftAmount': '0.0000',
# #             'balanceRechargeAmount': '1000.0000',
# #             'balanceTimes': '',
# #             'cardName': '储值卡xyz',
# #             'cardType': '1',
# #             'deleteYn': '1',
# #             'enjoyDiscount': '70',
# #             'expireTime': '253402271999000',
# #             'giftAmount': '0.0000',
# #             'lastAveragePrice': '',
# #             'memberCardTemplateId': '465599316220481536',
# #             'membershipCardCode': 'VIP00134',
# #             'membershipCardId': '504274016766128128',
# #             'membershipCardStatus': '1',
# #             'purchasePrice': '',
# #             'purchaseTimes': '',
# #             'rechargeAmount': '1000.0000',
# #             'upgradeYn': '1',
# #             'useMonth': '9999'
# #         }, {
# #             'addCashEventStatus': '0',
# #             'applicableItemId': '5',
# #             'applicableItemName': '洗吹',
# #             'applicableSpecificItemId': '',
# #             'applicableSpecificItemName': '全部洗吹项目',
# #             'averagePrice': '20.00',
# #             'balanceAmount': '0',
# #             'balanceGiftAmount': '0',
# #             'balanceRechargeAmount': '0',
# #             'balanceTimes': '100',
# #             'cardName': '计次卡测试',
# #             'cardType': '2',
# #             'deleteYn': '1',
# #             'enjoyDiscount': '',
# #             'expireTime': '253402271999000',
# #             'giftAmount': '',
# #             'lastAveragePrice': '20.00',
# #             'memberCardTemplateId': '503611922391625728',
# #             'membershipCardCode': 'VIP00135',
# #             'membershipCardId': '504274018691313664',
# #             'membershipCardStatus': '1',
# #             'purchasePrice': '2000.0000',
# #             'purchaseTimes': '100',
# #             'rechargeAmount': '',
# #             'upgradeYn': '0',
# #             'useMonth': '9999'
# #         }, {
# #             'addCashEventStatus': '0',
# #             'applicableItemId': '',
# #             'applicableItemName': '',
# #             'applicableSpecificItemId': '',
# #             'applicableSpecificItemName': '',
# #             'averagePrice': '',
# #             'balanceAmount': '0',
# #             'balanceGiftAmount': '0',
# #             'balanceRechargeAmount': '0',
# #             'balanceTimes': '0',
# #             'cardName': '年卡1',
# #             'cardType': '3',
# #             'deleteYn': '1',
# #             'enjoyDiscount': '95',
# #             'expireTime': '1631807999000',
# #             'giftAmount': '',
# #             'lastAveragePrice': '',
# #             'memberCardTemplateId': '463767922616791040',
# #             'membershipCardCode': 'VIP00136',
# #             'membershipCardId': '504274020767494144',
# #             'membershipCardStatus': '1',
# #             'purchasePrice': '1000.0000',
# #             'purchaseTimes': '0',
# #             'rechargeAmount': '',
# #             'upgradeYn': '0',
# #             'useMonth': '12'
# #         }]
# #     }
# #
# # res_val = {
# #                 'msg': '操作成功',
# #                 'requestUUID': 'JY-3f2cd2afd6422b3e14c59db75ef1101c',
# #                 'responseTime': '2020-09-18 10:59:04',
# #                 'ret': '0',
# #                 'success': '0',
# #                 'val': {
# #                     'id': '504287373267169280'
# #                 }
# #             }
# #
# # # print('val' in res_val_1 and 'cardType' in res_val_1['val'][0])
# # if isinstance(res_val['val'], list):
# #     for i in range(len(res_val['val'])):
# #         if res_val['val'][i]['cardType'] == '1':
# #             print('hahah')
#
# # if isinstance(res_val['val'], list):
# #     print('是个list')
# # else:
# #     print('不是list')
#
#
# # for i in range(len(res_val['val'])):
# #     if res_val['val'][i]['cardType'] == '1':
# #         DoExcel.write_back_init(test_data_path, 'init', 2, res_val['val'][i]['membershipCardId'])
# #     elif res_val['val'][i]['cardType'] == '2':
# #         DoExcel.write_back_init(test_data_path, 'init', 3, res_val['val'][i]['membershipCardId'])
# #     elif res_val['val'][i]['cardType'] == '3':
# #         DoExcel.write_back_init(test_data_path, 'init', 4, res_val['val'][i]['membershipCardId'])
# #     else:
# #         logging.info('顾客没有卡')
#
#
# import requests
# from tools.do_excel_for import DoExcelFor
#
#
# def get_excel_data():
#     test_data = DoExcelFor.get_data(test_data_path)
#     print(test_data)

# import time
# import datetime
#
# print(round(time.time() * 1000))
#
# print(datetime.datetime.now())



