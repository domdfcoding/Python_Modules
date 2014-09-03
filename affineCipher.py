#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Affine Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys, random, time

version = int((sys.version) [0])		# Determines Python version
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
			urllib.urlretrieve(address, name)
		except socket.gaierror or LookupError:
			print('\nUnable to update module ' + module); err = 'Y'
		import importlib
		try:
			globals()[module] = importlib.import_module(module)
		except ImportError:
			sys.exit()
	if err != 'Y': 	print('Done')
else:
	import pyperclip
from common import *


def MESSAGE():
	clear()
	message = input('Message: ')	# The string to be excrypted or decrypted
	if message == '': print('Enter a message!'); os.system(filepath)
	clear()							# Clears the screen for security
	return message
	
	
def KEY(): # The excryption/decryption key
	myMode = MODE()
	while True:		# Only proceed is a valid key is given
		print('Choose an encryption key. Enter "0" for a random key.')
		try: key = int(input('Encryption Key: ')); clear()# Gets Key
		except ValueError: 		# If the key is not a number ask again
			clear(); print('Invalid Key')
		if key == 0:
			key = getRandomKey()	
		keyA = key // len(SYMBOLS)
		keyB = key % len(SYMBOLS)
		if checkKeys(keyA, keyB, myMode) != None:
			break
		else:
			print('Please enter a valid key')
	return (keyA, keyB, myMode, key)
	
	
def MODE(): # Tells the program whether to encrypt or decrypt
	while True:
		print('Would you like to encrypt or decrypt?'); imp = input()
		if imp.lower().startswith('e'):
			mode = 'encrypt'
			clear(); break
		elif imp.lower().startswith('d'):
			mode = 'decrypt'
			clear(); break
		else: clear(); print('Invalid Mode')
	return mode
	

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front


def main():
	#myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
	myMessage = MESSAGE()
	#myKey = 2023
	#myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
	
	keyA, keyB, myMode, myKey = KEY()
	
	if myMode == 'encrypt':
		translated = encryptMessage(myMessage, keyA, keyB)
	elif myMode == 'decrypt':
		translated = decryptMessage(myMessage, keyA, keyB)
	print('Key: %s' % (myKey))
	print('%sed text:' % (myMode.title()))
	print(translated)
	pyperclip.copy(translated)
	write(translated, 'cipher.txt')

	print("The full %sed text has been copied to the clipboard \n and is also present as a text file in this folder." % (myMode))

	count = 20		# Waits 20 seconds before purge
	while count > 0:
		print('\rCopy NOW! Purging in ' + str(count) + ' seconds!     ',  end=''),
		sys.stdout.flush()
		time.sleep(1)
		count = count - 1

	pyperclip.copy('')	# clears clipboard
	delete("cipher.txt")	# Deletes encrypted file
	clear()				# Clears the screen for security
	raise SystemExit

def getKeyParts(key):			# Legacy function
	keyA = key // len(SYMBOLS)
	keyB = key % len(SYMBOLS)
	return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
	if keyA % len(SYMBOLS) == 1 and mode == 'encrypt':
		print('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
		return None
	if keyB == 0 and mode == 'encrypt':
		print('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
		return None
	if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
		print('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
		return None
	if gcd(keyA, len(SYMBOLS)) != 1:
		print('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))
		return None
	return 'Valid'


def encryptMessage(message, keyA, keyB):
	ciphertext = ''
	for symbol in message:
		if symbol in SYMBOLS:
			# encrypt this symbol
			symIndex = SYMBOLS.find(symbol)
			ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
		else:
			ciphertext += symbol # just append this symbol unencrypted
	return ciphertext


def decryptMessage(message, keyA, keyB):
	plaintext = ''
	modInverseOfKeyA = modInverse(keyA, len(SYMBOLS))

	for symbol in message:
		if symbol in SYMBOLS:
			# decrypt this symbol
			symIndex = SYMBOLS.find(symbol)
			plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
		else:
			plaintext += symbol # just append this symbol undecrypted
	return plaintext


def getRandomKey():
	while True:
		keyA = random.randint(2, len(SYMBOLS))
		keyB = random.randint(2, len(SYMBOLS))
		if gcd(keyA, len(SYMBOLS)) == 1:
			return keyA * len(SYMBOLS) + keyB


# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
	main()
	pause()
