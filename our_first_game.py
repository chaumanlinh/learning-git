# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:30:19 2021

@author: elias
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:30:15 2021

@author: elias
"""

import pygame
import math
import random

class Ball:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.r = radius
        self.s = screen
        self.c = color
       
    def draw(self):
        pygame.draw.circle(self.s, self.c, [self.x, self.y], self.r)
       
    def getCoords(self):
        return (self.x, self.y)
       

class PlayerBall(Ball):
    def move(self, mv_type):
        vel = 3
        if mv_type == 'UP':
            self.y -= vel
        elif mv_type == 'DOWN':
            self.y += vel
        elif mv_type == 'RIGHT':
            self.x += vel
        elif mv_type == 'LEFT':
            self.x -= vel
           
        if self.x - self.r < 0:
            self.x = self.r
        elif self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
        if self.y - self.r < 0:
            self.y = self.r
        elif self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
           
    def checkContact(self, greenBall):
        # if contact, return 1, otherwise return 0
        d = math.sqrt((self.y-greenBall.y)**2 + (self.x-greenBall.x)**2)
        if d < self.r + greenBall.r:
            greenBall.vy = 2
            greenBall.vx = 2
            return 1
        return 0


class cpuBall(Ball):
    def __init__(self, x, y, radius, color, screen):
        Ball.__init__(self, x, y, radius, color, screen)
        self.vy = random.randint(0, 4) - 2
        self.vx = random.randint(0, 4) - 2
        while self.vy == 0 or self.vx == 0:
            self.vy = random.randint(0, 4) - 2
            self.vx = random.randint(0, 4) - 2
           
    def move(self):
        self.x += self.vx
        self.y += self.vy
       
        multiplier = 1.1
       
        if self.x - self.r < 0:
            self.x = self.r
            self.vx *= -1*multiplier
        elif self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
            self.vx *= -1*multiplier
        if self.y - self.r < 0:
            self.y = self.r
            self.vy *= -1*multiplier
        elif self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
            self.vy *= -1*multiplier
           
        if self.vx > 8 or self.vy > 8:
            self.vx = 8
            self.vy = 8

WIDTH = 400
HEIGHT = 300
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False
clock = pygame.time.Clock()

playerBall1 = PlayerBall(100, 100, 20, (255, 0, 0), screen)
greenBall = cpuBall(100, 100, 20, (0, 255, 0), screen)
redBall = cpuBall(100, 100, 20, (255, 0, 0), screen)
blueBall = cpuBall(100, 100, 20, (0, 0, 255), screen)

myFont = pygame.font.SysFont('monospace', 15)

health = 100

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((255, 255, 255))
   
    pressed = pygame.key.get_pressed()
   
    if pressed[pygame.K_UP]:
        playerBall1.move('UP')
    if pressed[pygame.K_DOWN]:
        playerBall1.move('DOWN')
    if pressed[pygame.K_LEFT]:
        playerBall1.move('LEFT')
    if pressed[pygame.K_RIGHT]:
        playerBall1.move('RIGHT')
   
    # ball1.draw()
    playerBall1.draw()
    greenBall.draw()
    blueBall.draw()
    blueBall.move()
    greenBall.move()
    health -= playerBall1.checkContact(greenBall)
    if health <= 0:
        game_over = True
   
    label = myFont.render(f'Health = {health}', 1, (0,0,0))
    screen.blit(label, (10, HEIGHT - 20))
   
    pygame.display.flip()
    clock.tick(60)
    
    a = 10