from os import walk
import pygame
import sys
import glob

#uses the glob module to create a list of all the 
#files within the music directory
f = glob.glob('./Music/*.mp3') 

#print f, type(f)

#initiates the mixer
pygame.mixer.init()

#loads all of the tracks from 'f' into the queue
for efe in f:
	pygame.mixer.music.load(efe)

#begins to play the queue
pygame.mixer.music.play()

#when the queue runs out...exit.
while pygame.mixer.music.get_busy() == True:
	continue
else:
	sys.exit()

print pygame.mixer.music.get_queue()
