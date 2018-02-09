import requests
import json
import time
import curses
import os
from Recorder import record_audio, read_audio
from PythonApplication2 import startup
from decoder import decode_text
from terminal import access_terminal
from transcribe import transcribe_file
from multiprocessing import Process, Manager, Lock

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
 

def RecognizeSpeechGoogle(AUDIO_FILENAME, num_seconds, WINDOW):
 
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME, WINDOW)
 
    # reading audio
    
    # defining headers for HTTP request
    text = transcribe_file(AUDIO_FILENAME, WINDOW)
    
    return text
    	
def display_welcoming(WINDOW):
	WINDOW.clear()
	WINDOW.addstr("Enter a command:")
	WINDOW.addstr("\nA: access archive")
	WINDOW.addstr("\nQ: recognize and respond using Google")
	curses.cbreak()
	key = WINDOW.getkey()
	if str(key) == 'a' :
		access_terminal(WINDOW)
		    
	if str(key) == 'q':
		text =  RecognizeSpeechGoogle('myspeech.wav', 5, WINDOW)
		WINDOW.addstr("\nYou said: {}".format(text))
		output = decode_text(text,WINDOW)
		os.system("espeak 'placeholder {}'".format(output))
		WINDOW.addstr("\nBest Guess: {}".format(output))
		WINDOW.refresh()
		time.sleep(5)

	
def main(win):
	startup()
	time.sleep(10)
	while 1:
		display_welcoming(win)
		

	
startup()
