#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math, sys, time
	
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

filepath = os.path.realpath(__file__)
clear()

def MESSAGE():
	message = input('Message: ')	# The string to be excrypted or decrypted
	if message == '': print('Enter the message!'); os.system(filepath)
	clear()							# Clears the screen for security
	return message
	
def KEY(): # The excryption/decryption key
	while True:		# Only proceed is a valid key is given
		print('Choose the encryption key.')
		try: key = int(input('Encryption Key: ')); break	# Gets Key
		except ValueError: 		# If the key is not a number ask again
			clear(); print('Invalid Key')
	return key

def main():
	#myMessage = 'Cenoonommstmme oo snnio. s s c'
	myMessage = MESSAGE()							# Determines the message
	#myKey = 8
	
	while True:	
		myKey = KEY()									# Determines the key
		if 0 < myKey < len(myMessage):
			break
		else:
			clear(); print('Invalid Key')
	
	#print(myMessage + str(myKey)); os.system('pause')
	
	clear()
	plaintext = decryptMessage(myKey, myMessage)	# The decryption

	"""Print the encrypted string in ciphertext to the screen, with
	a | (called "pipe" character) before and after it in case there are 
	spaces at the end of the encrypted message."""
	print('|' + plaintext + '|')

	# Copy the encrypted string in ciphertext to the clipboard.
	pyperclip.copy(plaintext)
	
	write(plaintext, 'cipher.txt')

	print("""The message has been copied to the clipboard
and is also present as a text file in this folder.""")

	count = 20		# Waits 20 seconds before purge
	while count > 0:
		print('\rCopy NOW! Purging in ' + str(count) + ' seconds!',  end=''),
		sys.stdout.flush()
		time.sleep(1)
		count = count - 1

	pyperclip.copy('')		# clears clipboard
	delete("cipher.txt")	# Deletes encrypted file
	clear()					# Clears the screen for security
	quit()					# Closes the program

def decryptMessage(key, message):
	# The transposition decrypt function will simulate the "columns" and
	# "rows" of the grid that the plaintext is written on by using a list
	# of strings. First, we need to calculate a few values.

	# The number of "columns" in our transposition grid:
	numOfColumns = math.ceil(len(message) / key)
	# The number of "rows" in our grid will need:
	numOfRows = key
	# The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	# Each string in plaintext represents a column in the grid.
	plaintext = [''] * numOfColumns

	# The col and row variables point to where in the grid the next
	# character in the encrypted message will go.
	col = 0
	row = 0

	for symbol in message:
		plaintext[col] += symbol
		col += 1 # point to next column

		# If there are no more columns OR we're at a shaded box, go back to
		# the first column and the next row.
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1

	return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
	main()
