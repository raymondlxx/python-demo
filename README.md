# python-demo


what does file_categorizer do:
1. loop all the files int the current folder
2. if the current file's extension is not .MOV, skip(continue)
3. get the create time from the current file, and format it as yyyyMMdd as createTimeFolder.
4. create the folder createTimeFolder if it does not exists
5. move the current file into the new folder:createTimeFolder
