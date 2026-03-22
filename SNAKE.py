import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass 
    pygame.display.update()
    clock.tick(SNAKE_SPEED)