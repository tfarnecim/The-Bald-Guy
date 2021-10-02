import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

x = 320
y = 0

Vv = 0
Vl = 0
Ab = 1
Al = 0

while 1:

	relogio.tick(60)
	tela.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		if event.type == KEYDOWN:
			if event.key == K_w:
				Vv = -20
	

	#Testando se o bloco verde já chegou no chão
	if(y >= 450 and Vv >= 0):
		Vv = -(int(Vv/2.1))
		y = 450
	else:
		y+=Vv
		Vv+=Ab

	#Testando se esta tentando mover o bloco verde para os lados
	if(pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d]):
		if(pygame.key.get_pressed()[K_a]):
			Al = -1
		else:
			Al = 1
	else:
		Al = 0

	Vl += Al
	x+=Vl

	#Testando se o bloco verde bate nos cantos da tela
	if(x >= 610 or x <= 30):
		if(x >= 610):
			x = 610
		else:
			x = 30
		Vl = -int(Vl/1.5)

	pygame.draw.circle(tela,(0,255,0),(x,y),30)
	pygame.display.update()	