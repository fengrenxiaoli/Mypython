from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


#输入Email地址和口令
#from_addr=input('From: ')
from_addr='fengrenxiaoli@163.com'
#password=input('Password: ')
password='1100YiWangNian'
#输入收件人地址
#to_addr=input('To: ')
to_addr='18734250451m0@sina.cn'
#输入SMTP服务器地址
#smtp_server=input('SMTP server:')
smtp_server='smtp.163.com'

#纯文本邮件
#msg=MIMEText('hello,send by Python...','plain','utf-8')
#html邮件
msg=MIMEText('<html><head><title>hh</title></head><body><a href="http://www.python.org">Python</a><p>hello world!</p></body></html>','html','utf-8')
msg['From']=_format_addr('我<%s>'%from_addr)
msg['To']=_format_addr('你<%s>'%to_addr)
msg['Subject']=Header('hello','utf-8').encode()


import smtplib
server=smtplib.SMTP(smtp_server,25)
#SMTP协议默认端口是25
server.set_debuglevel(1)
#server.login(base64.decodestring(from_addr),base64.decodestring(password))
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

