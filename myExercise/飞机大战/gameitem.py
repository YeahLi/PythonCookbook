import pygame

class GameItem(object):
	"""docstring for GameItem"""
	def __init__(self, screen, x, y, pic, size):
		super(GameItem, self).__init__()
		self.screen = screen
		self.x = x
		self.y = y
		self.pic = pygame.image.load(pic)
		self.size = size

	def move(self, speed_x, speed_y):
		self.x += speed_x
		self.y += speed_y

	def display(self):
		self.screen.blit(self.pic, (self.x, self.y))