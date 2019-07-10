import os
import json
import requests



#help(os)

print(os.path.exists('/home/matar/Download'))



# create new directory
def create_new_dir(directory):
	if not os.path.exists(directory) :
		print('Creating a direcoty ' + directory)
		os.makedirs(directory)


def pwd():
	return os.getcwd()

 
dir1 = '/home/matar/Downloads/tempMatar'
create_new_dir(dir1)
