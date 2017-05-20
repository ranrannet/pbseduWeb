import unittest

from other.HTMLTestRunner import HTMLTestRunner
from send_email import sendEmail
from test_mathfunc import TestMathFunc
from test_course import test_course
from test_detail import test_detail
from test_index import test_index
from test_search import test_search

# 自动化测试入口
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_course))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_detail))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_index))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_search))


    with open('HTMLReport.html', 'w', encoding='utf8') as f:
        runner = HTMLTestRunner(stream=f,
                                title='鹏云课堂网站自动化测试',
                                description='鹏云课堂网站自动化测试',
                                verbosity=2
                                )
        runner.run(suite)


    # 发送邮件
    authInfo = {}
    authInfo['server'] = 'smtp.163.com'
    authInfo['user'] = 'wangrannet@163.com'
    authInfo['password'] = 'ranrannet'
    fromAdd = 'wangrannet@163.com'
    toAdd = ['943187376@qq.com']
    subject = '鹏云课堂网站自动化测试'
    plainText = '鹏云课堂网站自动化测试，详情请下载附件'
    sendEmail(authInfo, fromAdd, toAdd, subject, plainText)
