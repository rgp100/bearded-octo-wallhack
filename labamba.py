import pygame
import sys

pygame.mixer.init()
pygame.mixer.music.load("LaBamba.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
else:
	sys.exit()
