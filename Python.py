<<<<<<< HEAD
import pygame,sys
from pygame import *
=======
from platform import python_branch
import pygame
>>>>>>> 741e988ba5d10048e5105bfa96fa13f38f720244
pygame.init
icon = pygame.image.load('logo ramirez.jpg')#logo
pygame.display.set_caption("FORGANGOCHI") #titulo
pygame.display.set_icon(icon)
ventana= pygame.display.set_mode((1366,768)) #resolucion
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 



    


<<<<<<< HEAD
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() # todo esto es para cerrar la pestaña
=======

>>>>>>> 741e988ba5d10048e5105bfa96fa13f38f720244
