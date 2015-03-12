from os import walk
import pygame
import glob
import sys

def generate_songlist():
	#uses the glob module to create a list of all the 
	#files within the music directory
	songlist = glob.glob('./Music/*.mp3') 
	return songlist

songlist = generate_songlist()
print songlist

def play_song(track):
	pygame.mixer.init()
	pygame.mixer.music.load(track)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	else:
		pygame.mixer.quit()

play_song(songlist[1]) # THIS IS WHERE SYS.ARGV NEEDS TO BE USED IN ORDER TO MAKE A SUCCESSFUL COMMAND LINE PLAYER

"""
pygame.mixer.init()
pygame.mixer.music.load('LaBamba.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
else:
	pygame.mixer.quit()
"""


