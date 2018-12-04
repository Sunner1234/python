from chardet import detect
count,blanks = 0,0
with open("a.txt",'rb') as fp:
	#检测文件编码，编码信息保存到code中
	code = detect(fp.read())['encoding']
	print(code) #detect 是以一个字典序 保存的是文件的保存信息（以某种代码保存 比如ASCII码）


#引用第三方库：chardet
# pip install chardet  命令指示符自动安装chardet包 
with open("a.txt",'r',encoding=code) as fp: #‘r’是以源文件的方式进行读取
	while True:
		line = fp.readline()
		if not line:
			break
		# if(len(line)-1)==0:#判断空白行是否存在
		# 	blanks+=1      #如果存在+1
		# print(len(line.strip()))   #line.strip()作为判断真正意义上的空行
		# if not len(line.strip()):
		if len(line.strip()) == 0:
			blanks+=1
		count+=1
print(count,blanks)
