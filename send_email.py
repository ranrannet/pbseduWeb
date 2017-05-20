#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
#   程序：Python SMTP 发送带附件电子邮件
#   作者：Jason Hu
#   日期：2016-06-01
#   语言：Python
#   说明：Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
# ---------------------------------------------------------------------

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import smtplib


def sendEmail(authInfo, fromAdd, toAdd, subject, plainText):
    strFrom = fromAdd
    strTo = '; '.join(toAdd)

    server = authInfo.get('server')
    smtpPort = 25
    # sslPort = 465
    user = authInfo.get('user')
    passwd = authInfo.get('password')

    if not (server and user and passwd):
        print('incomplete login info, exit now')
        return

    # 设定root信息
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = '%s<%s>' % (Header('测试', 'utf-8'), strFrom)
    msgRoot['To'] = strTo

    # 邮件正文内容
    msgText = MIMEText(plainText, 'plain', 'utf-8')
    msgRoot.attach(msgText)

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)



    # 设定内置图片信息
    fp = open('/Users/wangranran/PycharmProjects/PbseduWeb/HTMLReport.html', 'rb')
    msgImage = MIMEText(fp.read(), 'base64', 'gb3212')

    msgImage["Content-Type"] = 'application/octet-stream'
    # filename可自定义，供邮件中显示
    msgImage["Content-Disposition"] = 'attachment; filename="HTMLReport.html"'
    fp.close()
    msgImage.add_header('Content-ID', '<pic_attach>')
    msgAlternative.attach(msgImage)

    try:
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(server, smtpPort)
        # 设定调试级别，依情况而定
        # smtp.set_debuglevel(1)
        smtp.login(user, passwd)
        smtp.sendmail(strFrom, toAdd, msgRoot.as_string())
        smtp.quit()
        print("邮件发送成功!")
    except Exception as e:
        print("失败：" + str(e));


# if __name__ == '__main__':
#     authInfo = {}
#     authInfo['server'] = 'smtp.163.com'
#     authInfo['user'] = 'wangrannet@163.com'
#     authInfo['password'] = 'ranrannet'
#     fromAdd = 'wangrannet@163.com'
#     toAdd = ['943187376@qq.com']
#     subject = 'Email Subject'
#     plainText = 'Email Content'
#     sendEmail(authInfo, fromAdd, toAdd, subject, plainText)
