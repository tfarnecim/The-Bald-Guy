import pygame
from pygame.locals import *

class BaldGuy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.sprites = []
		self.sprites.append(pygame.image.load('../images/sprites/bald guy/b1.png'))
		self.sprites.append(pygame.image.load('../images/sprites/bald guy/b2.png'))
		self.atual = 0
		self.image = sprites[atual]