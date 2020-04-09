from __future__ import with_statement
import os,shutil,time
from datetime import date

video_extensions = [".MOV"]
photo_extensions = [".JPG"]
supported_extension = video_extensions+photo_extensions
#
def getFolderNameFromFileModifyTime(path):
	mtime = os.path.getmtime(current_file_path)
	current_file_date = date.fromtimestamp(mtime)
	return current_file_date.strftime("%Y%m%d")
def getFolderNameFromFileCreateTime(path):
	mtime = os.path.getctime(current_file_path)
	current_file_date = date.fromtimestamp(mtime)
	return current_file_date.strftime("%Y%m%d")

def isExtensionSupported(ext):
	return ext in supported_extension

def getFileType(ext):
	if(ext in photo_extensions):
		return "photo"
	elif (ext in video_extensions):
		return "video"
	return ext

# print(os.path.getmtime("test.txt"))
# print(os.path.normpath("."))
# print(os.path.realpath("."))

current_path = os.path.realpath(".")

for root, dirs, files in os.walk(current_path):
	for file in files:

		print("file:"+file)
		current_file_path = os.path.join(root,file)

		filename, file_extension = os.path.splitext(current_file_path)
		
		if(isExtensionSupported(file_extension) is False):
			continue

		file_type = getFileType(file_extension)
		file_type_path = os.path.join(current_path,file_type)
		if(not os.path.exists(file_type_path)):
			os.mkdir(file_type_path)

		folder_name = getFolderNameFromFileModifyTime(current_file_path)
		
		
		folder_path = os.path.join(file_type_path,folder_name)
		
		if(not os.path.exists(folder_path)):
			os.mkdir(folder_path)
		dest_file_path = os.path.join(folder_path,file)
		print("dest_file_path:"+dest_file_path)
		#shutil.move(current_file_path,dest_file_path)
		print("------------------")





