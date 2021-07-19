#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import smtplib

############################邮件内容#############################
CONTEXT = "发送内容"
THEME = "邮件主题"
#################################################################


##############################配置###############################
FROM = ''        #发送者邮箱
PASSWORD = ''    #邮箱授权密码
TO = 'gir'        #接收者邮箱
HOST = 'smtp.163.com'            #SMTP服务器
PORT = '465'                     #SMTP服务器SSL端口
#################################################################


#############################代码区###############################
def sent_email(theme,context): 
    smtp_obj = smtplib.SMTP_SSL(HOST)
    smtp_obj.connect(HOST, port=PORT)
    res_smtp = smtp_obj.login(user=FROM, password=PASSWORD)
    msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(theme), '', context])
    smtp_obj.sendmail(from_addr=FROM, to_addrs=TO, msg=msg.encode('utf-8'))

sent_email(theme=THEME,context=CONTEXT)

#################################################################

