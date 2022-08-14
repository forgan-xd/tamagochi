from platform import python_branch
import pygame
pygame.init
icon = pygame.image.load('logo ramirez.jpg')
pygame.display.set_icon(icon)
ventana= pygame.display.set_mode((1366,768)) #resolucion
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
pygame.display.set_caption("FORGANGOCHI") #titulo
#Logo


