import pygame
from gameitem import *
from bullet import *
import random


class Plane(GameItem):
    """docstring for Plane"""

    def __init__(self, screen, hp, x, y, pic, size, bullet_type):
        super(Plane, self).__init__(screen, x, y, pic, size)
        
        self.hp = hp
        self.bullet_list = [] #store the fired bullets
        self.bullet_type = bullet_type

        #根据子弹类型设置不同子弹属性
        if self.bullet_type == "./feiji/bullet.png":
            self.bullet_harm = 10
            self.bullet_size = (22,22)
        elif self.bullet_type == "./feiji/bullet1.png":
            self.bullet_harm = 100
            self.bullet_size = (10,20)
        else:
            self.bullet_harm = 0
            self.bullet_size = (0,0)

        #Explosion image list
        self.explosion_list = []
        if pic == "./feiji/hero1.png":
            self.explosion_list = ["./feiji/hero_blowup_n1.png","./feiji/hero_blowup_n2.png","./feiji/hero_blowup_n3.png","./feiji/hero_blowup_n4.png"]
        elif pic == "./feiji/enemy1.png":
            self.explosion_list = ["./feiji/enemy1_down1.png","./feiji/enemy1_down2.png","./feiji/enemy1_down3.png","./feiji/enemy1_down4.png"]

        self.delay = 0
        self.isExplosioned = False
        self.isExplosionDone = False

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

    def explosion(self):
        
        if not self.isExplosioned:
            self.delay = 0
            self.isExplosioned = True
        
        if not self.isExplosionDone:
            self.delay += 1
            num = self.delay % 600
            if num == 1:
                print("Enter explosion(1)")
                self.pic = pygame.image.load(self.explosion_list[0])
            elif num == 4:
                print("Enter explosion(2)")
                self.pic = pygame.image.load(self.explosion_list[1])
            elif num == 7:
                print("Enter explosion(3)")
                self.pic = pygame.image.load(self.explosion_list[2])
            elif num == 10:
                print("Enter explosion(4)")
                self.pic = pygame.image.load(self.explosion_list[3])
                self.isExplosionDone = True
                self.delay = 0
                print("Explosion Finished")

class Hero(Plane):
    """docstring for Hero"""
    def __init__(self, screen, hp, x, y, pic, size, bullet_type):
        super(Hero, self).__init__(screen, hp, x, y, pic, size, bullet_type)
        
    def fire(self):

        self.delay += 1
        if self.delay == 5:
            plane_bullet = Bullet(self.screen, self.bullet_harm, self.x+40, self.y-10, self.bullet_type, self.bullet_size)
            self.bullet_list.append(plane_bullet)
            self.delay = 0

class Enemy(Plane):
    """docstring for Enemy"""
    def __init__(self, screen, hp, x, y, pic, size, bullet_type):
        super(Enemy, self).__init__(screen, hp, x, y, pic, size, bullet_type)
        self.direction = 1
        
    def fire(self):
        plane_bullet = Bullet(self.screen, self.bullet_harm, self.x+20, self.y+100, self.bullet_type, self.bullet_size)
        self.bullet_list.append(plane_bullet)

    def enemyAI(self, hero):
        if self.x <=0:
            self.direction = 1
        elif self.x >= (480 - self.size[0]):
            self.direction = -1
        
        self.move((6 * self.direction),0)

        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 67:
            self.fire()

        self.hitHero(hero)

    def hitHero(self, hero):
        remove_list = []
        for item in self.bullet_list:
            if item.x<0 or item.x>480 or item.y<0 or item.y>852:
                #hero.bullet_list.remove(item) #循环中删除 list 元素会漏删
                remove_list.append(item)
            elif item.isHit(hero):
                hero.hp -= item.harm
                remove_list.append(item)
            else:
                item.display()
                item.move(0, 10)

        for i in remove_list:
            self.bullet_list.remove(i)
            i = None