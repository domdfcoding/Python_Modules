#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  commmon.py		A collection of common python functions
#  
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

from domdf_python_tools.terminal import clear, br

def functions():
	print("""
Current list:
	clear()          Clears the terminal window
	br()             Prints a line break in the terminal
	isint(number)    Check if a number is a integer
	delete(file)     Delete the file in the current directory
	write(var file)  Write a variable to file in the current directory
	gcd(num1, num2)  Find the greatest common divisor of two numbers
	gcd2([num1,num2,...])
					 Find the greatest common diviser of a list of numbers
	lcm([num1,num2,...])
					 Find the lowest common multiple of a list of numbers
	hcf and hcf2     Highest common factor - pseudonyms for gcd
	modInverse(a,m)  Mod inverse of 'a' mod 'm'
	pause()          Pause
	close()          Close
	pexit()          Pause then close
	prt('something') Print on the same line
	crt('something',x)    Print over the content on the line,
					   followed by x number of spaces
	interrupt()      Print what to do to abort the script; 
					   dynamic depending on OS
	restart_program()     Restarts the Program
	splitLen(string,x)    Split a string every x characters
    readOutput(command)   Read the stdout of the command
	timeoutInput(prompt,timeout)     Input with a timeout

	
""")

def restart_program():				# restarts the program
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

import os, sys, msvcrt, time
version = int(sys.version[0])		# Python Version


def clearprint(textToPrint,newline=True):
	clear()
	prt(textToPrint)
	if newline == True:
		sys.stdout.write('\n')

def isint(num):	# Only works with floating point numbers
	if num == int(num):
		return True
	else:
		return False

def delete(filename):	# Delete the file 'filename' in the current directory
	os.remove(os.path.join(os.getcwd(),filename))

def write(var, filename):	# Write a variable to file in the current directory
	with open(os.path.join(os.getcwd(), filename),'w') as f:
		f.write(var)

def read(filename):	# Read a file in the current directory; Untested
	with open(os.path.join(os.getcwd(), filename)) as f:
		return f.read()
		
def append(var, filename):	# Read a file in the current directory; Untested
	with open(os.path.join(os.getcwd(), filename), 'a') as f:
		f.write(var)

from mathematical.utils import gcd, gcd2, lcm, hcf, hcf2, modInverse

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
	
def interrupt():
	print('(Press Ctrl-%s to quit at any time.)' % 'C' if os.name == 'nt' else 'D')
	
def splitLen(string,n):
	return [string[i:i+n] for i in range(0,len(string),n)]

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
			if result[-1] == '\r':   # or \n, whatever Win returns;-)
				print('')
				return 'input'
			time.sleep(0.1)          # just to yield to other processes/threads
		else:
			if time.time() > finishat:
			   print('')
			   return 'no_input'
	
def module_version(x=1):
	module_version = "1.0"
	print("""Python Common Functions Module v1.0
Copyright (C) Dominic Davis-Foster 2014
<domdfcoding@gmail.com>""")
	if x == 1:
		print('Use "functions()" for a full list of functions available.')

# End of module

if __name__ == '__main__':
	module_version(0)
	functions()
	print("Use 'from common import *' to simplify calling the modules.\nThen simply type the function name")  
	pexit()
	
