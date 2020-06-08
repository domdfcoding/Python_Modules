#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Caesar Cipher  
# http://inventwithpython.com/hacking (BSD Licensed) 
#

import os
import sys
import time

from domdf_python_tools.paths import delete, write

import pyperclip
from common import clear

clear()

filepath = os.path.realpath(__file__)

# Every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def MESSAGE():
	clear()
	message = ''

	while not message:
		message = input('Message: ')  # The string to be encrypted or decrypted
		if message == '':
			print('Enter a message!')
	clear()  # Clears the screen for security
	message = message.upper()  # Capitalise the string in message
	return message


def KEY():  # The excryption/decryption key
	global LETTERS
	while True:  # Only proceed is a valid key is given
		print('Choose an encryption key between 0 and ' + str(len(LETTERS) - 1))
		try:
			inp = int(input('Encryption Key: '))  # Gets Key
		except ValueError:  # If the key is not a number ask again
			clear()
			print('Invalid Key')
		# Checks that the key is valid and clears the screen for security
		if 0 <= inp <= (len(LETTERS) - 1):
			key = inp
			clear()
			break
		else:  # If the key is out of range ask again
			clear()
			print('Invalid Key')
	return key


def MODE():  # Tells the program whether to encrypt or decrypt
	while True:
		print('Would you like to encrypt or decrypt?')
		imp = input()
		if imp.lower()[0] in ('e', 'd'):
			mode = imp.lower()[0]
			clear()
			break
		else:
			clear()
			print('Invalid Mode')
	return mode


def encrypt(key, message, mode):
	global LETTERS
	translated = ''  # Stores the encrypted/decrypted form of the message

	# Run the encryption/decryption code on each symbol in the message string
	for symbol in message:
		if symbol in LETTERS:
			# Get the encrypted or decrypted number for this symbol
			num = LETTERS.find(symbol)
			if mode == 'e':
				num = num + key
			elif mode == 'd':
				num = num - key

			# handle the wrap around if num is larger than the length of LETTERS or less than 0
			if num >= len(LETTERS):
				num = num - len(LETTERS)
			elif num < 0:
				num = num + len(LETTERS)

			# add encrypted/decrypted number's symbol at the end of translated
			translated = translated + LETTERS[num]

		else:
			# just add the symbol without encrypting or decrypting
			translated = translated + symbol
	return translated


def main():
	message = MESSAGE()
	key = KEY()
	mode = MODE()
	ciphertext = encrypt(key, message, mode)

	print(ciphertext)

	# copy the encrypted/decrypted string to the clipboard
	pyperclip.copy(ciphertext)

	write(ciphertext, 'cipher.txt')

	print("""The message has been copied to the clipboard
and is also present as a text file in this folder.""")

	count = 20  # Waits 20 seconds before purge
	while count > 0:
		print('\rCopy NOW! Purging in ' + str(count) + ' seconds!', end='')
		sys.stdout.flush()
		time.sleep(1)
		count = count - 1

	pyperclip.copy('')  # clears clipboard
	delete("cipher.txt")  # Deletes encrypted file
	clear()  # Clears the screen for security
	quit()  # Closes the program


if __name__ == '__main__':
	main()
