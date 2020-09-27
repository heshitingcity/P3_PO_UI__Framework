# encoding: utf-8
#@author: newdream_daliu
#@file: test_mail.py
#@time: 2020-08-16 16:43
#@desc:测试邮件
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config_utils import local_config

# 发送邮件的条件：邮件头--邮件内容---发送
#邮件的类型：普通文本邮件，带附件的邮件

#账户信息，标题
smtp_server = 'smtp.qq.com'
smtp_sender = '279129436@qq.com'
smtp_senderpassword = 'byjmnnovsmxlbhec'
smtp_receiver = '279129436@qq.com,3048903923@qq.com,540628236@qq.com' #收件人
smtp_cc = '1064055110@qq.com' #抄送人
smtp_subject = '禅道UI自动化测试报告'
smtp_body =  ' 新梦想测试开发P3班_PO模式，报告邮件'

    # self.smtp_file = smtp_fil-e_path
#消息体 发送普通 邮件，只有正文，没有附件
# msg = MIMEText(smtp_body, "html", "utf-8")
# msg['from'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject
# #


#发送带附件为邮件
smtp_file='D:/P3_PO_UI_Test_Framework/reports/禅道UI自动化测试报告.zip'
msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition', 'attachment',
                    filename=('gb2312', '', smtp_file.split('/')[-1]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

msg.attach(MIMEText(smtp_body, "html", "utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject



#发送
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',') + smtp_cc.split(','),msg.as_string())
