import tkinter as tk


class AESCipher:
	def __init__(self, key):
		self.key = hashlib.md5(key).hexdigest()[:BS]

