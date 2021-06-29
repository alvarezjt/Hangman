'''
pygame.ini() returns a tuple you can print to determine if the initialization was successful.

'''
import pygame as pygame
import pygame.display as pygamedisplay
import pygame.event as pygameevent

pygame.init()
gameDisplay = pygamedisplay.set_mode((800,600))
pygamedisplay.update() # pygamedisplay.flip() can be used alternatively
pygamedisplay.set_caption('Slither')

RunGame = True

while RunGame:
	for event in pygameevent.get():
		print(event)
pygame.quit()
quit