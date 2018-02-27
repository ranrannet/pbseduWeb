import unittest

from send_email import sendEmail
from test_case.test_course import test_course
from test_case.test_detail import test_detail
from test_case.test_index import test_index
from test_case.test_search import test_search

# 自动化测试入口
from util.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_course))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_detail))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_index))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_search))

    with open('HTMLReport.html', 'w', encoding='UTF-8') as f:
        runner = HTMLTestRunner(stream=f,
                                title='7Fresh-App自动化测试',
                                description='7Fresh-App自动化测试',
                                verbosity=2
                                )
        runner.run(suite)

    # 发送邮件
    authInfo = {'server': 'smtp.163.com', 'user': 'wangrannet@163.com', 'password': 'baobei_123'}
    fromAdd = 'wangrannet@163.com'
    toAdd = ['943187376@qq.com']
    subject = '7Fresh-App自动化测试'
    plainText = '7Fresh-App自动化测试，详情请下载附件'
    sendEmail(authInfo, fromAdd, toAdd, subject, plainText)
