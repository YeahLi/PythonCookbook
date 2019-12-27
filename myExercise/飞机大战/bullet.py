import pygame
from gameitem import *


class Bullet(GameItem):
	"""docstring for bullet"""
	def __init__(self, screen, harm, x, y, pic, size):
		super(Bullet, self).__init__(screen, x, y, pic, size)
		self.harm = harm

	def hit(self):
		pass