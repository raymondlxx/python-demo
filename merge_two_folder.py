#This program move the source folder to the destination folder.
#if the file exists in the destination folder, and they have the same md5sum. skip;
#otherwise, rename the source file to the md5sum.

import os,sys
import hashlib
import os,shutil,time
from datetime import date

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

video_extensions = [".MOV"]
photo_extensions = [".JPG"]
supported_extension = video_extensions+photo_extensions
#
def getFolderNameFromFileModifyTime(current_file_path):
	mtime = os.path.getmtime(current_file_path)
	current_file_date = date.fromtimestamp(mtime)
	return current_file_date.strftime("%Y%m%d")

def getFolderNameFromFileCreateTime(current_file_path):
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

def printProgress(msg):
	sys.stdout.write('{0}\r'.format(msg))
	sys.stdout.flush()


def moveAndMerge(source,dest):
	totalFile = 0
	unsupported={}
	skiped={}
	renamed={}
	passReport={}
	destExists={}

	for root,dirs,files in os.walk(source):

		for file in files:
			totalFile+=1

			current_file_path = os.path.join(root,file)
			source_file_md5 = md5(current_file_path)

			filename, file_extension = os.path.splitext(current_file_path)
			
			if(isExtensionSupported(file_extension) is False):
				if(file_extension not in unsupported.keys()):
					unsupported[file_extension]=0
				unsupported[file_extension]+=1
				continue

			if(file_extension not in passReport.keys()):
				passReport[file_extension]=0
			passReport[file_extension]+=1

			#video, photo etc
			file_category = getFileType(file_extension)
			file_category_path = os.path.join(dest,file_category)
			if(os.path.exists(file_category_path) is False):
				#print("create folder:"+file_category_path)
				os.mkdir(file_category_path)

			#yyyyMMdd
			modifyTimeFolderName = getFolderNameFromFileModifyTime(current_file_path)

			dest_folder_path = os.path.join(file_category_path,modifyTimeFolderName)
			if(os.path.exists(dest_folder_path) is False):
				#print("create folder:"+dest_folder_path)
				os.mkdir(dest_folder_path)
			
			dest_file_path = os.path.join(dest_folder_path,file)
			if(os.path.exists(dest_file_path) is True):
				#print("dest file exists:"+dest_file_path)
				dest_file_md5 = md5(dest_file_path)
				if(source_file_md5 == dest_file_md5):
					#skip
					if(file_extension not in skiped.keys()):
						skiped[file_extension]=0
					skiped[file_extension]+=1
					#print("dest_file_md5:"+dest_file_md5)
				else:
					if(file_extension not in renamed.keys()):
						renamed[file_extension]=0
					renamed[file_extension]+=1
					#rename
					dest_file_path = os.path.join(dest_folder_path,dest_file_md5+""+file_extension)
					#print("rename to:"+dest_file_path)
			#else:
				#print(current_file_path+" to:"+dest_file_path)
				#shutil.move(current_file_path,dest_file_path)

			printProgress(">>>>>>totalFile:"+str(totalFile)+", unsupported"+str(unsupported)+", renamed:"+str(renamed)+", skiped:"+str(skiped))




#moveAndMerge("/Users/leolee/photo","/Volumes/PHOTO")
moveAndMerge("/Volumes/NIKON D7000/DCIM","/Volumes/PHOTO")
print("end")