#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid
from datetime import datetime


nowtime = '{:%H:%M:%S}'.format(datetime.now())

SMTP_server = "mail.ismylife.me"
me = "nasa@ismylife.me"
you = "gra230434@gmail.com"

SUBJECT = "Hello! Python send mail"
TEXT = "Python send email TEST. \n{0}".format(nowtime)

message = MIMEMultipart('alternative')
message['From'] = me
message['To'] = you
message['Subject'] = SUBJECT
message['Message-Id'] = make_msgid(domain='ismylife.me')
message.attach(MIMEText(TEXT, 'plain'))

try:
    mail = smtplib.SMTP_SSL('mail.ismylife.me', port='465')
    mail.set_debuglevel(1)
    mail.ehlo()
    mail.login('admin@ismylife.me', 'Mailadmin')
    mail.sendmail(me, you, message.as_string())
    print("send mail success")
except smtplib.SMTPException:
    print("Error: fail")
mail.quit()
