# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
from plane import *

def control(hero):
    for event in pygame.event.get():
        #Keyboard listening
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero.move(-5,0)
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero.move(5,0)
            elif event.key == K_SPACE:
                print("fire")
                hero.fire()    

def main():

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background_pic = pygame.image.load("./feiji/background.png")

    hero = Hero(screen, 100, 210, 700, "./feiji/hero1.png", (100,124), "./feiji/bullet.png")
    
    enemy =  Enemy(screen, 10, 0, 0, "./feiji/enemy1.png", (70,90), "./feiji/bullet1.png")

    #3. 把背景图片放到窗口中显示
    while True:
        #显示背景
        screen.blit(background_pic, (0,0))
        #显示飞机
        hero.display()
        #显示飞机射出的子弹
        for item in hero.bullet_list:
            item.display()
            item.move(0, -10)
        #显示敌机
        enemy.display()
        enemy.enemyAI()

        pygame.display.update()

        #必须要有事件监听不然上面图片无法显示
        control(hero)
        
        time.sleep(0.01)

if __name__ == '__main__':
    main()