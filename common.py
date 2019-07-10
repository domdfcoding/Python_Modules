#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  commmon.py
"""
Python Common Functions Module v1.0
A collection of common python functions
"""
#  Copyright (C) Dominic Davis-Foster 2014 <domdfcoding@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# Portions of code from http://inventwithpython.com/hacking (BSD Licensed)   
#

import os, sys, msvcrt, time

# Imports for legacy support
from domdf_python_tools.terminal import clear, br, pyversion
from mathematical.utils import *


def functions():
	print("""
	pause()          Pause
	close()          Close
	pexit()          Pause then close
	prt('something') Print on the same line
	crt('something',x)    Print over the content on the line,
					   followed by x number of spaces
	restart_program()     Restarts the Program

	readOutput(command)   Read the stdout of the command
	timeoutInput(prompt,timeout)     Input with a timeout
""")

def restart_program():				# restarts the program
	"""Restarts the current program.
	Note: this function does not return. Any cleanup action (like
	saving data) must be done before calling this function."""
	python = sys.executable
	os.execl(python, python, * sys.argv)


version = pyversion		# Python Version


def clearprint(textToPrint,newline=True):
	clear()
	prt(textToPrint)
	if newline == True:
		sys.stdout.write('\n')

def pause():
	os.system('pause')

def close(message=''):
	if message == '':
		raise SystemExit
	else:
		sys.exit(message)
	
def pexit(message=''):
	pause()
	close(message)

def prt(somethingToPrint):
	sys.stdout.write(somethingToPrint)
	sys.stdout.flush()

def crt(somethingToPrint, num=4):
	print('\r' + somethingToPrint + ' '*num)
	
def readOutput(command):
	import subprocess
	return subprocess.Popen(command,stdout=subprocess.PIPE).stdout.readline()

def timeoutInput(prompt, timeout=30.0):
	sys.stdout.write(prompt)
	finishat = time.time() + timeout
	result = []
	while True:
		if msvcrt.kbhit():
			result.append(msvcrt.getche())
			if result[-1] == '\r':  # or \n, whatever Win returns
				print('')
				return 'input'
			time.sleep(0.1)  # just to yield to other processes/threads
		else:
			if time.time() > finishat:
				print('')
				return 'no_input'
