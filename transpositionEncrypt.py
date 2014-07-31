#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Transposition Cipher Encryption
# http://inventwithpython.com/hacking (BSD Licensed)

import os, sys, time

import sys; version = int((sys.version) [0])		# Determines Python version
err = 'N'; print 'Trying to update modules: ',
for module in ('common', 'pyperclip', 'EXIF', 'caesarCipher', 'mbox', 'reverseCipher', 'transpositionEncrypt'):
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
		print '/nUnable to update module' + module; err = 'Y'
	import importlib
	try:
		importlib.import_module(module)
	except ImportError:
		quit()
if err != 'Y': 	print 'Done'
import pyperclip
from common import *

filepath = os.path.realpath(__file__)
clear()

def MESSAGE():
	message = input('Message: ')	# The string to be excrypted or decrypted
	if message == '': print('Enter a message!'); os.system(filepath)
	clear()							# Clears the screen for security
	return message
	
def KEY(): # The excryption/decryption key
	while True:		# Only proceed is a valid key is given
		print('Choose an encryption key.')
		try: key = int(input('Encryption Key: ')); break	# Gets Key
		except ValueError: 		# If the key is not a number ask again
			clear(); print('Invalid Key')
	return key

def encryptMessage(key, message):
	clear()
	# Each string in ciphertext represents a column in the grid.
	ciphertext = [''] * key

	# Loop through each column in ciphertext.
	for col in range(key):
		pointer = col

		# Keep looping until pointer goes past the length of the message.
		while pointer < len(message):
			# Place the character at pointer in message at the end of the
			# current column in the ciphertext list.
			ciphertext[col] += message[pointer]

			# move pointer over
			pointer += key

	# Convert the ciphertext list into a single string value and return it.
	return ''.join(ciphertext)

def main():
	myMessage = MESSAGE()							# Determines the message
	while True:	
		myKey = KEY()									# Determines the key
		if 0 < myKey < len(myMessage):
			break
		else:
			clear(); print('Invalid Key')
	ciphertext = encryptMessage(myKey, myMessage)	# The encryption

	"""Print the encrypted string in ciphertext to the screen, with
	a | (called "pipe" character) before and after it in case there are 
	spaces at the end of the encrypted message."""
	print('|' + ciphertext + '|')

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


# If transpositionEncrypt.py is run (instead of imported as a module) call the main() function.
if __name__ == '__main__':
	main()
