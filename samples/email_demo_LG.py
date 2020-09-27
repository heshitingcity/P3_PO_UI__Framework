import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config_utils import local_config
# from common import zip_utils

# current_path = os.path.abspath(os.path.dirname(__file__))
# smtp_file_path = os.path.join( current_path , '..' , 'reports/禅道自动化测试报告V1.1/禅道自动化测试报告.zip' )
smtp_server = 'smtp.qq.com'
smtp_sender = '279129436@qq.com'
smtp_senderpassword = 'wkyzjxjytrdjcaed'
smtp_receiver = '279129436@qq.com'
smtp_cc = 'liu_qaz@163.com'
smtp_subject = '禅道自动化测试报告'
smtp_body = '来自python的邮件配置'
# smtp_file = smtp_file_path
#邮件消息体
msg = MIMEText(smtp_body, "html", "utf-8") #邮件信息对象
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject
#
# msg = MIMEMultipart()
# with open(smtp_file, 'rb') as f:
#     mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
#     mime.add_header('Content-Disposition', 'attachment',
#                     filename=('gb2312', '', smtp_file.split('/')[-1]))
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)
#
# msg.attach(MIMEText(smtp_body, "html", "utf-8"))
# msg['from'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject


#发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)  #465
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())
