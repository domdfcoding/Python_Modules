#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# reverseCipher.py
#
# http://inventwithpython.com/hacking (BSD Licensed)
#
#

import time, os

import sys; version = int((sys.version) [0])		# Determines Python version
try:
	from common import *
except ImportError:
	
	if version == 2:
		import urllib
	elif version == 3:
		import urllib.request as urllib
	urllib.urlretrieve ("https://www.dropbox.com/s/osqppbk7z15oloi/common.py?dl=1", "common.py")
	from common import *
try:
	import pyperclip
except ImportError:
	
	if version == 2:
		import urllib
	elif version == 3:
		import urllib.request as urllib
	urllib.urlretrieve ("https://www.dropbox.com/s/kaegxps1soimg30/pyperclip.py?dl=1", "pyperclip.py")
	import pyperclip

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
	quit()				# Closes the program

if __name__ == '__main__':
	main()
