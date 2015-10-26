import os

def findfile(filename,path='.'):
	for x in os.listdir(path):
		if os.path.isdir(os.path.join(path,x)):
			findfile(filename,os.path.join(path,x))
		if x.count(filename)>0 and os.path.isfile(os.path.join(path,x)):
			print(os.path.join(path,x))

findfile('py')