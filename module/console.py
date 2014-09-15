import os, sys, msvcrt, time
version = int(sys.version[0])		# Python Version

def clear():								# clear the display
	os.system('cls' if os.name == 'nt' else 'clear')
	# works for Windows and UNIX, but does not clear Python Shell
	
def br():									# Line Break
	print("")
	
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
	
def interrupt():
	print('(Press Ctrl-%s to quit at any time.)' % 'C' if os.name == 'nt' else 'D')

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
