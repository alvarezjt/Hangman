'''
pygame.ini() returns a tuple you can print to determine if the initialization was successful.

'''
import pygame as pygame
import pygame.display as pygamedisplay
import pygame.event as pygameevent

#Color Constants
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorRed = (254, 0, 0)
colorGreen = (0, 254, 0)
colorBlue = (0, 0, 254)

pygame.init()
gameDisplay = pygamedisplay.set_mode((800,600))
pygamedisplay.update() # pygamedisplay.flip() can be used alternatively
pygamedisplay.set_caption('Slither')

RunGame = True

while RunGame:
	for event in pygameevent.get():
		print(event)
		if event.type == pygame.QUIT:
			RunGame = False
	gameDisplay.fill(colorWhite)
	pygamedisplay.update()
pygame.quit()
quit