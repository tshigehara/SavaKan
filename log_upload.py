import os
import datetime
import shutil
import re
from models import upload_file

file_path = "/home/pi/minecraft2/logs"
# Main starts here
######
#
######
if __name__ == "__main__":
	#os.listdir(file_path)
	regex = re.compile(r'gz')

	txtfiles = []
	files = []
	for filename in os.listdir(file_path):
		if os.path.isfile(os.path.join(file_path, filename)):
			files.append(filename)
		
	
	regex = re.compile(r'(.gz)$')
	for name in files:
		if regex.search(name):
			txtfiles.append(name)
			print(file_path + '/' + name)
			upload_file(file_path + '/' + name)
			os.remove(file_path + '/' + name)
		
	
	
	#upload_file('/home/pi/minecraft2/logs/*.gz')
	print("Uploaded to S3 successfully")
 
