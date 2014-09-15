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

import os

def module_version(x=1):
	module_version = "1.0"
	print("""Python Common Functions Module v1.0
Copyright (C) Dominic Davis-Foster 2014
<domdfcoding@gmail.com>""")
	if x == 1:
		print('Use "functions()" for a full list of functions available.')

def splitLen(string,n):
	return [string[i:i+n] for i in range(0,len(string),n)]

def readOutput(command):
	import subprocess
	return subprocess.Popen(command,stdout=subprocess.PIPE).stdout.readline()

def restart_program():				# restarts the program
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

import maths, console, EXIF, fileOperations, mbox, valbox


# End of module

if __name__ == '__main__':
	module_version(0)
	functions()
	print("Use 'from common import *' to simplify calling the modules.\nThen simply type the function name")  
	pexit()
	
