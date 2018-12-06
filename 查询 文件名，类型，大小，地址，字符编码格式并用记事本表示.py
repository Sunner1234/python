#python换行用"\n" 
#python语言查询 文件名，类型，大小，地址，字符编码格式并用记事本表示


import os
from chardet import detect
#获取文件查询并记录文本文件行数和空白行 strip（）表示真正意义上的空白行
def get_file_info(file_path):
	with open(file_path,"rb") as fp:
		encode = detect(fp.read())['encoding']
		info.write("Encoding:"+str(encode)+"\\")

	line_count,blank_count = 0,0
	with open(file_path,'r',encoding=encode) as fp:
		while True:
				line = fp.readline()
				if not line:
					break
				line_count+=1
				if not len(line.strip()):
					blank_count+=1
	info.write(str(line_count)+"Lines("+str(blank_count)+"blanks)"+"\n")			
# a = os.path.isfile(r"C:\Users\Administrator\Desktop\root\a.txt")
#获取文件查询并记录文件地址，大小，文件数并用“-”分隔
root_path = os.getcwd()
dir_count,file_count = 0,0.
info = open("file_info.txt",'w')
for root,dirs,files in os.walk(root_path):
	if not os.path.isfile(root):
		# print(root)
		dir_count+=1
	for f in files:
		file_path = os.path.join(root,f)
		if os.path.isfile(file_path):
				file_count+=1
		info.write("Filename"+os.path.splitext(f)[0]+"\n")
		info.write("Type"+os.path.splitext(f)[1]+"\n")
		info.write("Size:"+str(os.path.getsize(file_path))+"Bytes"+"\n") #获取文件大小
		info.write("Location:"+root+"\n")
		get_file_info(file_path)
		info.write("-"*60+"\n")
		# print(f)                                        #所有子包下的文件
info.write(str(dir_count-1)+"Folders"+"\n")                              #-1的意思是不包括root(所在文件夹位置)
info.write(str(file_count)+"Files"+"\n")

#查询子文件夹里的子文件并记录
root_path = os.getcwd()
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):
	current_path = root.split("\\")
	level = len(current_path) - offset
	info.write("\t"*level+"\\"+current_path[-1]+"\n")
	for f in files:
		info.write("\t"*(level+1)+f+"\n")











# with open("a.txt","rb") as fp:
# 	encode = detect(fp.read())['encoding']
# 	print("Encoding:",encode)

# line_count,blank_count = 0,0
# with open("a.txt") as fp:
# 	while True:
# 		line = fp.readline()
# 		if not line:
# 			break
# 		line_count+=1
# 		if not len(line.strip()):
# 			blank_count+=1
# print(line_count,"Lines(",blank_count,"blanks)")			
