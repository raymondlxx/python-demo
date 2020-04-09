# python-demo


## what does file_categorizer do:
1. loop all the files in the current folder
2. if the current file's extension is not .MOV, skip(continue)
3. get the create time from the current file, and format it as yyyyMMdd as createTimeFolder.
4. create the folder createTimeFolder if it does not exists
5. move the current file into the new folder:createTimeFolder


## what does merge_two_folder.py do:
1.loop all the files in the source folder
2.skip those files whose extension is unsupported
3.if the file exists in the destination folder/{file_type}/modified_date/filename, check whether they have the same md5sum.
if True, skip.
if False, rename the file to md5.{file's extension}
4. move the file to the destination folder.

this script is designed for the purpose: categorize my photos according to the date the folder was taken.
