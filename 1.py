import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):
	current_dir = root
	path_list = current_dir.split("\\")
	indent_level = len(path_list) - offset
	print("\t"*indent_level,"\\"+path_list[-1])
	# print(length,len(length))   #len()显示列表长度
	for f in files:
		filename = os.path.splitext(f)[0]   #输出文件名取第0个文件赋予filename名字 
		print("\t"*(indent_level+1),filename)







	

	
