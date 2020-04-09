from __future__ import with_statement
import os,shutil,time
from datetime import date

#
def getFolderNameFromFileModifyTime(path):
	mtime = os.path.getmtime(current_file_path)
	current_file_date = date.fromtimestamp(mtime)
	return current_file_date.strftime("%Y%m%d")
def getFolderNameFromFileCreateTime(path):
	mtime = os.path.getctime(current_file_path)
	current_file_date = date.fromtimestamp(mtime)
	return current_file_date.strftime("%Y%m%d")


# print(os.path.getmtime("test.txt"))
# print(os.path.normpath("."))
# print(os.path.realpath("."))

current_path = os.path.realpath(".")

for root, dirs, files in os.walk(current_path):
	for file in files:

		print("file:"+file)
		current_file_path = os.path.join(root,file)

		filename, file_extension = os.path.splitext(current_file_path)
		
		if(file_extension != ".MOV"):
			continue

		folder_name = getFolderNameFromFileCreateTime(current_file_path)
		print("folder_name:"+folder_name)
		folder_path = os.path.join(current_path,folder_name)
		print("folder_path:"+folder_path)
		if(not os.path.exists(folder_path)):
			os.mkdir(folder_path)
		dest_file_path = os.path.join(folder_path,file)
		print("dest_file_path:"+dest_file_path)
		shutil.move(current_file_path,dest_file_path)
		print("------------------")





