import pygame
from gameitem import *
from bullet import *



class Plane(GameItem):
	"""docstring for Plane"""
	def setBulletType(self, bullet_type):
		self.bullet_type = bullet_type

		#根据子弹类型设置不同子弹属性
		if self.bullet_type == "./feiji/bullet.png":
			self.bullet_harm = 3
			self.bullet_size = (22,22)
		elif self.bullet_type == "./feiji/bullet1.png":
			self.bullet_harm = 100
			self.bullet_size = (0,0)
		else:
			self.bullet_harm = 0
			self.bullet_size = (0,0)

	def __init__(self, screen, hp, x, y, pic, size, bullet_type):
		super(Plane, self).__init__(screen, x, y, pic, size)
		
		self.hp = hp
		self.bullet_list = [] #store the fired bullets
		self.bullet_type = bullet_type

		#根据子弹类型设置不同子弹属性
		if self.bullet_type == "./feiji/bullet.png":
			self.bullet_harm = 3
			self.bullet_size = (22,22)
		elif self.bullet_type == "./feiji/bullet1.png":
			self.bullet_harm = 100
			self.bullet_size = (0,0)
		else:
			self.bullet_harm = 0
			self.bullet_size = (0,0)

	
		

class Hero(Plane):
	"""docstring for Hero"""
	def __init__(self, screen, hp, x, y, pic, size, bullet_type):
		super(Hero, self).__init__(screen, hp, x, y, pic, size, bullet_type)
		
		
	def fire(self):
		plane_bullet = Bullet(self.screen, self.bullet_harm, self.x+40, self.y-10, self.bullet_type, self.bullet_size)
		self.bullet_list.append(plane_bullet)

class Enemy(Plane):
	"""docstring for Enemy"""
	def __init__(self, screen, hp, x, y, pic, size, bullet_type):
		super(Enemy, self).__init__(screen, hp, x, y, pic, size, bullet_type)
		
		
	def fire(self):
		plane_bullet = Bullet(self.screen, self.bullet_harm, self.x+40, self.y-10, self.bullet_type, self.bullet_size)
		self.bullet_list.append(plane_bullet)

	def enemyAI(self):
		self.move(1,0)
		#self.fire()