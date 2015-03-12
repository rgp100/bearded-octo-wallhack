from os import walk
import pygame
import glob

def generate_songlist():
	#uses the glob module to create a list of all the 
	#files within the music directory
	songlist = glob.glob('./Music/*.mp3') 
	return songlist

songlist = generate_songlist()
print songlist

"""
pygame.mixer.init()
pygame.mixer.music.load('LaBamba.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
else:
	pygame.mixer.quit()
"""


