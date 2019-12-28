# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from plane import *

def control(hero):
    for event in pygame.event.get():
        #Keyboard listening

        if event.type == QUIT:
            print("exit")
            exit()
        '''
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero.move(-5,0)
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move(5,0)
            elif event.key == K_SPACE:
                hero.fire()
        '''

    if hero.hp > 0:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            pass
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if hero.x<=(480-hero.size[0]):
                hero.move(5,0)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if hero.x>=0:
                hero.move(-5,0)
        if keys[pygame.K_SPACE]:
            hero.fire()  

        if keys[pygame.K_b]:
            hero.explosion()    

def main():

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)
    
    #enable key hold feature
    #pygame.key.set_repeat(10)
    
    #draw frequency
    clock = pygame.time.Clock()

    #2. 创建一个和窗口大小的图片，用来充当背景
    background_pic = pygame.image.load("./feiji/background.png")

    hero = Hero(screen, 100, 210, 700, "./feiji/hero1.png", (100,124), "./feiji/bullet.png")
    
    enemy =  Enemy(screen, 10, 0, 0, "./feiji/enemy1.png", (70,90), "./feiji/bullet1.png")

    #3. 把背景图片放到窗口中显示
    while True:        
        #显示背景
        screen.blit(background_pic, (0,0))
        #显示飞机
        if hero.hp <= 0 and not hero.isExplosionDone:
            hero.display()
            hero.explosion()
        elif hero.hp > 0:
            hero.display()
            
        #显示飞机射出的子弹
        remove_list = []
        for item in hero.bullet_list:
            if item.x<0 or item.x>480 or item.y<0 or item.y>852:
                #hero.bullet_list.remove(item) #循环中删除 list 元素会漏删
                remove_list.append(item)
            elif item.isHit(enemy):
                enemy.hp -= item.harm
                remove_list.append(item)
            else:
                item.display()
                item.move(0, -10)

        for i in remove_list:
            hero.bullet_list.remove(i)
            i = None
        #显示敌机
        #if not enemy.isExplosionDone:
        if enemy.hp > 0:
            enemy.display()
            enemy.enemyAI(hero)
        elif enemy.hp <= 0 and not enemy.isExplosionDone:
            enemy.display()
            enemy.explosion()
        

        control(hero)
        
        pygame.display.update()
        
        clock.tick(60)

if __name__ == '__main__':
    main()