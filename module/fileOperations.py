import os, sys, msvcrt, time
version = int(sys.version[0])		# Python Version

def delete(filename):	# Delete the file 'filename' in the current directory
	os.remove(os.path.join(os.getcwd(),filename))

def write(var, filename):	# Write a variable to file in the current directory
	with open(os.path.join(os.getcwd(), filename),'w') as f:
		f.write(var)

def read(filename):	# Read a file in the current directory; Untested
	with open(os.path.join(os.getcwd(), filename)) as f:
		return f.read()
		
def append(var, filename):	# Read a file in the current directory; Untested
	with open(os.path.join(os.getcwd(), filename), 'a') as f:
		f.write(var)
