#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# reverseCipher.py
#
# http://inventwithpython.com/hacking (BSD Licensed)
#
#

from domdf_python_tools.paths import delete, write

# remember to add ,end='' if using python 3
import pyperclip
from common import *

clear()


def MESSAGE():
	clear()
	message = ''

	while not message:
		message = input('Message: ')  # The string to be encrypted or decrypted
		if message == '':
			print('Enter a message!')
	clear()  # Clears the screen for security
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

	count = 20  # Waits 20 seconds before purge
	while count > 0:
		print('\rCopy NOW! Purging in ' + str(count) + ' seconds!', end=''),
		sys.stdout.flush()
		time.sleep(1)
		count = count - 1

	pyperclip.copy('')  # clears clipboard
	delete("cipher.txt")  # Deletes encrypted file
	clear()  # Clears the screen for security
	sys.exit()  # Closes the program


if __name__ == '__main__':
	main()
