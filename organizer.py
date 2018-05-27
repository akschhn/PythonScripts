# Steps : Check if Images Folder exists , else create ; 
#        Check if songs Folder exists , else create ;
# 		 Check if documents Folder exists , else create ; // Etc
# 		 Now read all the files of Downloads directory and based on their type
#		 move them to their respective folders	

import os
import shutil
homeDir = os.path.expanduser('~')
seperator = "/"
checkDirectoryNm = "Downloads"
downloadsDir = homeDir + seperator + checkDirectoryNm
if os.path.isdir(downloadsDir) :
	directories = ["Images", "Songs", "Videos", "Pem", "Coding", "Docs", "Compressed", "Patches", "Sheets", "Mixed"]

	# Create the required directories
	for directoryName in directories:
		directoryPath = downloadsDir + seperator + directoryName 		
		if not os.path.isdir(directoryPath) :
			os.makedirs(directoryPath)
			print("Created "+ directoryPath + " directory")

	# Loop through the files in main directory and move them 
	# to the required directory
	for file in os.listdir(downloadsDir) :
		fromDirPath = downloadsDir + seperator + file
		if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".webp") :
			toMoveDir = downloadsDir + seperator + "Images"
			shutil.move(fromDirPath, toMoveDir)	
		elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") :
			toMoveDir = downloadsDir + seperator + "Docs"
			shutil.move(fromDirPath, toMoveDir)	
		elif file.endswith(".pem") :
			toMoveDir = downloadsDir + seperator + "Pem"
			shutil.move(fromDirPath, toMoveDir)	
		elif file.endswith(".xlsx") or file.endswith(".csv") :
			toMoveDir = downloadsDir + seperator + "Sheets"
			shutil.move(fromDirPath, toMoveDir)	
		elif file.endswith(".patch") :
			toMoveDir = downloadsDir + seperator + "Patches"
			shutil.move(fromDirPath, toMoveDir)		
		elif file.endswith(".sh") or file.endswith(".gz") or file.endswith(".zip") or file.endswith(".pkg") or file.endswith(".dmg") or file.endswith(".jar") or file.endswith(".tgz") :
			toMoveDir = downloadsDir + seperator + "Compressed"
			shutil.move(fromDirPath, toMoveDir)				
		elif file.endswith(".webm") or file.endswith(".mp4") :
			toMoveDir = downloadsDir + seperator + "Videos"
			shutil.move(fromDirPath, toMoveDir)	
		elif file.endswith(".xml") or file.endswith(".js") or file.endswith(".xml") or file.endswith(".html") or file.endswith(".properties") or file.endswith(".java") or file.endswith(".py") or file.endswith(".conf") or file.endswith(".sbt") or file.endswith(".htm") :	
			toMoveDir = downloadsDir + seperator + "Coding"
			shutil.move(fromDirPath, toMoveDir)			
