import pygame
from pygame.locals import *
from sys import exit

personagem = pygame.sprite.Group()
objetos = pygame.sprite.Group()
bumerangue = pygame.sprite.Group()
largura = 640
altura = 480

#-=-=-=-=-=-=-=-=-=-=-=-=-
#TODAS AS CLASSES DO JOGO
#-=-=-=-=-=-=-=-=-=-=-=-=-

class BaldGuy(pygame.sprite.Sprite):

	def __init__(self):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.sprites = []
		self.sprites.append(pygame.image.load('images/sprites/bg/standing/b1.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/standing/b2.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/jump/b1.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/jump/b2.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/run/b1.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/run/b2.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/run/b3.png'))
		self.sprites.append(pygame.image.load('images/sprites/bg/run/b4.png'))
		
		self.atual = 0
		self.atualcorrida = 0
		self.image = self.sprites[self.atual]
		self.image = pygame.transform.scale(self.image,(32*4,32*4))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (320,0)

		self.x = 320
		self.y = 0
		self.ux = 320
		self.uy = 0

		self.Vv = 0
		self.Vl = 0
		self.Av = 1
		self.atacando = False
		self.pulando = True
		self.direita = True

	def update(self):

		self.entrou = False

		if(self.atacando):
			self.entrou = True
		
		if(self.Vv > 0):#Se ele tá descendo
			self.entrou = True
			self.image = self.sprites[3]
			self.image = pygame.transform.scale(self.image,(32*4,32*4))
			if(not self.direita):
				self.image = pygame.transform.flip(self.image,True,False)

		if(self.Vv < 0 and not self.entrou):#Se ele tá subindo
			self.entrou = True
			self.image = self.sprites[2]
			self.image = pygame.transform.scale(self.image,(32*4,32*4))
			if(not self.direita):
				self.image = pygame.transform.flip(self.image,True,False)


		if(self.Vl > 0 and not self.entrou):#Se ele está correndo para a direita
			self.entrou = True
			self.atualcorrida += 0.25
			if(self.atualcorrida >= 4):
				self.atualcorrida = 0
			self.image = self.sprites[int(self.atualcorrida+4)]
			self.image = pygame.transform.scale(self.image,(32*4,32*4))
			#falta carregar o sprite de corrida aqui dentro
		
		if(self.Vl < 0 and not self.entrou):#Se ele está correndo para a esquerda
			self.entrou = True
			self.atualcorrida += 0.25
			if(self.atualcorrida >= 4):
				self.atualcorrida = 0
			self.image = self.sprites[int(self.atualcorrida+4)]
			self.image = pygame.transform.scale(self.image,(32*4,32*4))
			if(not self.direita):
				self.image = pygame.transform.flip(self.image,True,False)
			#falta carregar o sprite de corrida aqui dentro
		
		if(not self.entrou):
			self.atual += 0.05
			if(self.atual >= 2):
				self.atual = 0
			self.image = self.sprites[int(self.atual)]
			self.image = pygame.transform.scale(self.image,(32*4,32*4))
			if(not self.direita):
				self.image = pygame.transform.flip(self.image,True,False)

		colisoes = pygame.sprite.spritecollide(self, objetos, False)

		cabeca = False

		for obj in colisoes:
			
			ybobj = obj.rect.bottomleft[1]
			ycobj = obj.rect.topleft[1]
			ybbg  = self.uy
			ycbg  = self.uy-32

			if(ybobj < ycbg):#se no ultimo frame o bg estava embaixo do bloco
				self.Vv = (-(self.Vv)/1.5)
				self.uy = self.y
				#print("Y DE BAIXO DO BLOCO = %d"%(ybobj))
				cabeca = True
				self.y = ybobj+1+32*4

			if(ycobj > ybbg):#se no ultimo frame o bg estava em cima do bloco
				#print("COLIDIU")
				self.Vv = 0
				self.uy = self.y
				self.y = ycobj+1
				self.pulando = False

		if(self.pulando or len(colisoes) == 0):
			self.Vv += self.Av

		self.uy = self.y
		self.y += self.Vv

		if cabeca:
			#print("VELOCIDADE = %d"%(self.Vv))
			#print("Y = %d"%(self.y))
			pass
		

		'''

		if(len(colisoes) > 0 and self.Vv >= 0):#atualizando y quando ocorre colisao vertical
			self.Vv = 0
			self.y = colisoes[0].rect.topleft[1]+1
			self.pulando = False
		else:
			self.Vv += self.Av
			self.y += self.Vv

		'''

		self.x += self.Vl

		self.rect.bottomleft = (self.x,self.y)

		if(cabeca):
			pass
			#print("topleft = %d , %d"%(self.rect.topleft[0] , self.rect.topleft[1]))
			#print("bottomright = %d , %d"%(self.rect.bottomright[0] , self.rect.bottomright[1]))

class Chao(pygame.sprite.Sprite):

	def __init__(self, rect):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.sprites = []
		self.sprites.append(pygame.image.load('images/blocks/ground2.png'))
		
		self.atual = 0
		self.image = self.sprites[self.atual]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = rect

#nada feito ainda
class Bumerangue(pygame.sprite.Sprite):

	def __init__(self, rect):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.sprites = []
		self.sprites.append(pygame.image.load('images/sprites/bumerangue/b1.png'))
		self.sprites.append(pygame.image.load('images/sprites/bumerangue/b2.png'))
		self.sprites.append(pygame.image.load('images/sprites/bumerangue/b3.png'))
		self.sprites.append(pygame.image.load('images/sprites/bumerangue/b4.png'))
		
		self.atual = 0
		self.image = self.sprites[self.atual]
		self.image = pygame.transform.scale(self.image,(32*4,32*4))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (320,0)

#-=-=-=-=-=-=-=-=-=-=-=-=-
#TODAS AS CLASSES DO JOGO
#-=-=-=-=-=-=-=-=-=-=-=-=-

#-=-=-=-=-=-=-=-=-=-=-=-=-
#INSTANCIANDO AS CLASSES
#-=-=-=-=-=-=-=-=-=-=-=-=-

baldguy = BaldGuy()
chao = Chao((0,480))
chao2 = Chao((300,200))

personagem.add(baldguy)
objetos.add(chao2)
objetos.add(chao)


#-=-=-=-=-=-=-=-=-=-=-=-=-
#INSTANCIANDO AS CLASSES
#-=-=-=-=-=-=-=-=-=-=-=-=-

#-=-=-=-=-=-=-=-=-=-=-=-=-
#INICIO DO JOGO
#-=-=-=-=-=-=-=-=-=-=-=-=-



pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while 1:

	relogio.tick(30)
	tela.fill((255,255,255))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		if event.type == KEYDOWN:
			if event.key == K_UP and not baldguy.pulando:
				baldguy.Vv = -25
				baldguy.pulando = True

	if pygame.key.get_pressed()[K_LEFT]:
		if baldguy.direita:
			baldguy.image = pygame.transform.flip(baldguy.image,True,False)
		baldguy.direita = False
		baldguy.Vl = -10

	elif pygame.key.get_pressed()[K_RIGHT]:
		if not baldguy.direita:
			baldguy.image = pygame.transform.flip(baldguy.image,True,False)
		baldguy.direita = True
		baldguy.Vl = 10

	else:
		baldguy.Vl = 0

	personagem.draw(tela)
	objetos.draw(tela)
	bumerangue.draw(tela)
	personagem.update()
	objetos.update()
	bumerangue.update()
	pygame.display.update()	