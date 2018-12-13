# POP: Post Office Protocal
# SMTP: Simple Mail Transfer Protocal
# MIME: Multipurpose Internet Mail Extension 
#发送文本文件
import smtplib 
from email.mime.text import MIMEText
from email.header import Header  #收件人 发件人的主题信息
from email.mime.multipart import MIMEMultipart  #对象适用于创建附件 multipart带附件的邮件
from email.mime.base import MIMEBase            #每一个mimebase都对应一个一个附件
from email import encoders
def add_attachment(file):
	with open(file,'r') as fp:
		mime = MIMEBase('application','octect-string',filename = file)            #application指一个应用文件 以octect-string 8进制字符传送
		mime.add_header("Content-Disposition",'attachment',filename = file)             #文件头部对内容进行描述 attachment解释接收到的8进制字符
		mime.add_header("Content-ID","<0>")       
		mime.add_header("X-attachment-Id","0")           #告诉浏览器 用什么指定的应用程序打开接收到的文件
		mime.set_payload(fp.read())
		encoders.encode_base64(mime)                      #encode_base64()一种编码格式类似于utf-8
		att_msg.attach(mime)
from_addr = "1789304318@qq.com"         #发送人
# to_addr = "1016709328@qq.com"         #王晨
# to_addr = "1536854522@qq.com"           #萌老师
# to_addr = "1747220367@qq.com"         #孙培华
# to_addr = "425045826@qq.com"   		#刘龙龙
to_addr = "1789304318@qq.com"  		#收件人
server_adder = "smtp.qq.com"
psw = 'hcuexzccxgrhhjii'                   #密码
#创建邮件正文对象
contents = "<h1>类好啊</h1>"         	#内容
msg = MIMEText(contents,'html','utf-8')  #类，类里的参数 格式utf-8
# msg['From'] = from_addr
# msg['To'] = to_addr
# msg['Subject'] = "Test"
# print(msg)

#创建带附件的邮件对象
att_msg = MIMEMultipart()
att_msg.attach(msg)  				#将正文添加到带附件的邮件对象
att_msg['From'] = from_addr
att_msg['To'] = to_addr
att_msg['Subject'] = "Test"       #定义主题



#SMTP_server = "smtp.qq.com"      #设置服务器地址
# with open("test.html",'r',encoding="utf-8") as fp:
# 	contents = fp.read()

#批量添加文件
att = ["test.txt","test2.txt"]
for a in att:
	add_attachment(a)

server = smtplib.SMTP(server_adder,25)     #套接字包括，地址、端口
server.login(from_addr,psw)      #登录账号密码
server.sendmail(from_addr,[to_addr],att_msg.as_string()) #把文件传送出去的方法 要把msg转换成string或者object对象
server.quit()                    #退出服务器