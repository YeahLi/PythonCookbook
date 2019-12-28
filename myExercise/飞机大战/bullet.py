import pygame
from gameitem import *


class Bullet(GameItem):
	"""docstring for bullet"""
	def __init__(self, screen, harm, x, y, pic, size):
		super(Bullet, self).__init__(screen, x, y, pic, size)
		self.harm = harm

	def isHit(self, plane):
		return self.x > plane.x and self.x < (plane.x + plane.size[0]) and self.y >= plane.y and (self.y < plane.y+plane.size[1])
