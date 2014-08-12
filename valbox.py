import sys; version = int((sys.version) [0])		# Determines Python version
if version == 2:
	import Tkinter as tkinter
	from Tkinter import *
	#from Tkinter import simpledialog
elif version == 3:
	import tkinter
	from tkinter import *
	#from tkinter import simpledialog

class inputDialog:

	def __init__(self, parent, position, windowname, label):

		top = self.top = Toplevel(parent)
		
		self.top.title(windowname) # Sets windowname
			
		self.top.bind("<Return>", lambda x: self.ok())
		self.top.bind("<Escape>", lambda x: root.destroy())
	
		if position == 'top':
			Label(top, text=label).grid(row=1, column=2)
		elif position == 'left':
			Label(top, text='', font=("Helvetica", 3)).grid(row=0, column=3)
			Label(top, text=label).grid(row=2, column=1)

		self.e = Entry(top,takefocus=1)
		self.e.grid(row=2, column=2)	# creates entry field
		self.e.focus_set()
		
		# Prevents the window from being closed
		self.top.protocol("WM_DELETE_WINDOW", root.destroy)
		
		Label(top, text='', font=("Helvetica", 3)).grid(row=3)
		
		b = Button(top, text="OK", command=self.ok)
		b.grid(row=4,column=1,columnspan=2, sticky=N)

	def ok(self):

		print("value is " + self.e.get())
		self.result = self.e.get()
		self.top.destroy()

root = Tk()
root.withdraw()

def valbox(position='top', windowname="Value", label="Value", cancel='quit'): 
	""" quit to close; return to continue program.
	if using return, cancel the operation if None returned.
	e.g. variable=valbox(); if variable != None: do something with variable """
	d = inputDialog(root, position, windowname, label)
	root.wait_window(d.top)
	try:
		return d.result
	except AttributeError:
		if cancel == 'quit': raise SystemExit
		elif cancel == 'return': return None
