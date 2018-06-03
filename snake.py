import pygame
from random import choice
window = pygame.display.set_mode((400,400))
caption = "Hello Pygame!"
pygame.display.set_caption(caption)

screen = pygame.Surface((400, 400))

###Class For Target
class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = pygame.image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

##Class for snake palyer
class Snake:
	def __init__(self, xpos, ypos, filename):
		#set the positions on coordinate grid
		self.x = xpos
		self.y = ypos
		#load the textures
		self.bitmap = pygame.image.load(filename)
		#make the textures transparent
		self.bitmap.set_colorkey((0,0,0))
		#this list will contain the tail objects (cubics) after hero eat some target
		self.tail = list()
		self.length = 1
		#which side snake will go 1- right, 2-down, 3-left, 4- up
		#This is the maden as list cause the player can give a few commands to move
		#in some directiones before the frame will update
		self.side = [1]
	def render(self):
		#This method will draw the Snake texture on Screen surface
		screen.blit(self.bitmap, (self.x, self.y))
		#if snake have the tail: each object of tail must to be drawen too
		if self.tail:
			for each in self.tail[1:]:
				each.render()
	def check(self, other):
		#if head of snake collides with any other object - method will return True
		if self.x == other.x and self.y == other.y:
			return True
		#Anyway if snake is touching the target with her tail - the target will be eaten too
		if self.tail:
			for each in self.tail[1:]:
				if each.x == other.x and each.y == other.y:
					return True
	def update(self):
		#Everytime of calling of this method will make snake move in direction Self.Side
		if self.side[-1] == 1:
			self.x += 40
		elif self.side[-1] == 2:
			self.y += 40
		elif self.side[-1] == 3:
			self.x -= 40
		elif self.side[-1] == 4:
			self.y -= 40
		#after updating the position, the list will be returned to normal status (len = 1)
		if len(self.side) > 1: self.side.pop(0)
	def correct(self):
		#Calling of this method check that the snake not going behind the game area
		if self.x > 400-40: self.x = 0
		elif self.y > 400-40: self.y = 0
		elif self.x < 0: self.x = 400 -40
		elif self.y < 0: self.y = 400 - 40
	def move(self):
		self.update()
		self.correct()
		self.tail.insert(0, Sprite(self.x, self.y, 'zet.png'))
		while len(self.tail) > self.length: self.tail.pop()
		count = 0
		for each in self.tail:
			count += 1
			each.number = count
	def len(self):
		#Calling of this method is making the snake longer by 1 pt
		self.length += 1



coords = range(0,400-40, 40)
hero = Snake(choice(coords), choice(coords), 'zet.png')
zet = Sprite(choice(coords), choice(coords), 'hero.png')



done = True
while done:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
		if e.type == pygame.KEYDOWN:
			if (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and hero.side[-1] != 3: hero.side.append(1)# = 1
			elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and hero.side[-1] != 4: hero.side.append(2)# = 2
			elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and hero.side[-1] != 1: hero.side.append(3)# = 3
			elif (e.key == pygame.K_w or e.key == pygame.K_UP) and hero.side[-1] != 2: hero.side.append(4)# = 4

	screen.fill((5,5,5))
	zet.render()
	hero.move()
	if hero.check(zet):
		zet.x = choice(coords)
		zet.y = choice(coords)
		hero.len()
	for each in hero.tail[1:]:
		if each.x == hero.x and each.y == hero.y:
			hero.length = each.number
	hero.render()
	window.blit(screen, (0,0))
	pygame.display.flip()
	pygame.time.delay(300)
	if hero.length <= 1:
		caption = "Hello Pygame"
	else: caption = "Your score is %d" %(hero.length -1)
	pygame.display.set_caption(caption)
