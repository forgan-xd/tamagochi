import pygame
pygame.init

runnin = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    