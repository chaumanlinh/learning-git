# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:30:19 2021

@author: elias
"""

WIDTH = 400
HEIGHT = 300

def myFunc(x, y, z):
    var = x**2
    return var + y

import pygame

class Ball:
    def __init__(self, x_coord, y_coord, radius, screen, velocity = 1):
        self.x = x_coord
        self.y = y_coord
        self.r = radius
        self.v = velocity
        self.screen = screen
        
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.r)
        
# Inheritance
class PlayerBall(Ball):
        
    def move(self, mv_type):
        if mv_type == 'UP':
            self.y -= 1*self.v
        elif mv_type == 'RIGHT':
            self.x += 1*self.v
        elif mv_type == 'DOWN':
            self.y += 1*self.v
        elif mv_type == 'LEFT':
            self.x -= 1*self.v
            
        if self.x - self.r < 0:
            self.x = self.r
        elif self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
        if self.y - self.r < 0:
            self.y = self.r
        elif self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
    
    def check_wall_collision(self):
        if self.x - self.r < 0:
            self.r -= 5
        elif self.x + self.r > WIDTH:
            self.r -= 5
        if self.y - self.r < 0:
            self.r -= 5
        elif self.y + self.r > HEIGHT:
            self.r -= 5
    
        
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False

clock = pygame.time.Clock()

ball1 = PlayerBall(100, 100, 20, screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        ball1.v = 3
    if pressed[pygame.K_UP]:
        ball1.move('UP')
    if pressed[pygame.K_RIGHT]:
        ball1.move('RIGHT')
    if pressed[pygame.K_DOWN]:
        ball1.move('DOWN')
    if pressed[pygame.K_LEFT]:
        ball1.move('LEFT')
    ball1.check_wall_collision()
    # ball1.health_update()
    ball1.draw()
    # ball1.move('DOWN')
    # ball1.move('RIGHT')
    pygame.display.flip()
    clock.tick(60)