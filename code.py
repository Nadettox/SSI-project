import hashlib
import sys
import bcrypt

def cipher(clair):
	m = bcrypt.hashpw(clair, bcrypt.gensalt())
	return m

def getUser(f,user):
	fi = open(f,"r")
	for line in fi:
		creds = line.split(':')
		if creds[0] == user:
			print(creds[1]) 

def writeId(f,lg,pw):
	fi = open(f,"a")
	str1 = cipher(pw)
	fi.write(str(lg)+':'+str1+'\n')



