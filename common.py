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
    pause()          Pause
    close()          Close
    pexit()          Pause then close
""")

import os

def clear():								# clear the display
	os.system('cls' if os.name == 'nt' else 'clear')
	# works for Windows and UNIX, but does not clear Python Shell
	
def br():									# Line Break
	print("")
	
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
		
def gcd(a, b):
	while a != 0:
		a, b = b % a, a
	return b
	
def pause():
	os.system('pause')

def close():
	raise SystemExit
	
def pexit():
	pause()
	close()
	
def module_version():
	module_version = "1.0"
	print("""
Python Common Functions Module v1.0
Copyright (C) Dominic Davis-Foster 2014
<domdfcoding@gmail.com>
Use "functions()" for a full list of functions available.
""")

# End of module

if __name__ == '__main__':
	module_version()
	functions()
	print("Use 'from common import *' to simplify calling the modules.\nThen simply type the function name")
	pexit()
