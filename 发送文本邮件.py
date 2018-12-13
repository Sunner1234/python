# POP: Post Office Protocal
# SMTP: Simple Mail Transfer Protocal
# MIME: Multipurpose Internet Mail Extension 
#发送文本文件
import smtplib 
from email.mime.text import MIMEText

from_addr = "1789304318@qq.com"  #发送人
#to_addr = "51277241@qq.com"    #收件人
# to_addr = "1747220367@qq.com"  #孙培华
to_addr = "1789304318@qq.com"  #刘龙龙

contents = "<h1>哈哈哈！！！！你好玩啊</h1>"         #内容
msg = MIMEText(contents,'html','utf-8')  #类，类里的参数 格式utf-8
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Test"
print(msg)
psw = 'hcuexzccxgrhhjii'                   #密码
SMTP_server = "smtp.qq.com"      #设置服务器地址
# with open("test.html",'r',encoding="utf-8") as fp:
# 	contents = fp.read()

server = smtplib.SMTP(SMTP_server,25)     #套接字包括，地址、端口
server.login(from_addr,psw)      #登录账号密码
server.sendmail(from_addr,to_addr,msg.as_string()) #把文件传送出去的方法 要把msg转换成string或者object对象
server.quit()                    #退出服务器