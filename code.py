import hashlib
import sys
import bcrypt
from Crypto.Cipher import AES
from math import fmod
from AES import *

def cipher(clair):
	m = bcrypt.hashpw(clair, bcrypt.gensalt())
	return m

def userConnected(db,user,pwd):
	users = db.select_users()
	for row in users:
		if(row[0] == user and row[1] == pwd):
			return True;

def addCredentials(db, user,pw, appId, appPw, appName):
	cipher = AESCipher(pw)
	db.insert_creds(cipher.encrypt(appId), cipher.encrypt(appPw), cipher.encrypt(appName), user)
	print("cred ajoutes")

def afficherCreds(db, user, pw):
	creds = db.select_creds(user)
	cipher = AESCipher(pw)
	for cred in creds:
		print("ID application : " + cipher.decrypt(cred[0]) + "\n")
		print("Mot de passe application : " + cipher.decrypt(cred[1]) + "\n")
		print("Nom application : " + cipher.decrypt(cred[2]) + "\n")

def padding(text):
	val = fmod(len(text),16)
	padded = text + " "*int(16-val)
	return padded

	
	
