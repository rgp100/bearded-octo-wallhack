import subprocess
import pygame

#all mp3's on the system will have their path in a file named mp3s.dat in the pwd
def produceMP3file():
	subprocess.call(["find ~ -name '*.mp3' >> mp3s.dat", ], shell=True)
	
produceMP3file() #produces file mp3s.dat
songlist = []

def play_song(track):
	pygame.mixer.init()
	pygame.mixer.music.load(track)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	else:
		pygame.mixer.quit()

def get_tracks():
	theFile = open('mp3s.dat','r')
	for line in theFile:
		songlist.append(line)
	count = 0
	for item in songlist:
		songlist[count]=songlist[count].rstrip()
		count = count + 1
	theFile.close()

def song_loop():
	while (len(songlist) != 0):
		play_song(songlist[0])
		songlist.pop(0)
		print songlist
#-------------------^Working^------------------------------------

get_tracks()
song_loop()

