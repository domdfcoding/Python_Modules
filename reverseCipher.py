#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# reverseCipher.py
#
# http://inventwithpython.com/hacking (BSD Licensed)
#
#

import os, time

import sys; version = int((sys.version) [0])		# Determines Python version
# remember to add ,end='' if using python 3
if __name__ == '__main__':
	err = 'N'; print('Trying to update modules: ',end=''),
	for module in ('common', 'pyperclip'):
		try:
			import socket
			# Trys to connect to the internet
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(("google.com",80))
			s.close()						# Closes the connection to google
			# Above code from http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
			if version == 2:
				import urllib
			elif version == 3:
				import urllib.request as urllib
			name = module + ".py"
			address = "https://raw.githubusercontent.com/domdfcoding/Python_Modules/master/" + name
			urllib.urlretrieve (address, name)
		except socket.gaierror or LookupError:
			print('\nUnable to update module' + module); err = 'Y'
		import importlib
		try:
			globals()[module] = importlib.import_module(module)
		except ImportError:
			sys.exit()
	if err != 'Y': 	print('Done')
else:
	import pyperclip
from common import *

clear()

def MESSAGE():
	message = input('Message: ')	# The string to be excrypted or decrypted
	if message == '': print('Enter a message!'); os.system(filepath)
	clear()							# Clears the screen for security
	return message

def encryptMessage(message):
	mirrored = ''
	i = len(message) - 1
	while i >= 0:
		mirrored = mirrored + message[i]
		i = i - 1
	return mirrored

def main():
	message = MESSAGE()
	ciphertext = encryptMessage(message)
	print(ciphertext)
	# Copy the encrypted string in ciphertext to the clipboard.
	pyperclip.copy(ciphertext)

	write(ciphertext, 'cipher.txt')

	print("""The message has been copied to the clipboard
and is also present as a text file in this folder.""")

	count = 20		# Waits 20 seconds before purge
	while count > 0:
		print('\rCopy NOW! Purging in ' + str(count) + ' seconds!',  end=''),
		sys.stdout.flush()
		time.sleep(1)
		count = count - 1

	pyperclip.copy('')	# clears clipboard
	delete("cipher.txt")	# Deletes encrypted file
	clear()				# Clears the screen for security
	sys.exit()				# Closes the program

if __name__ == '__main__':
	main()
