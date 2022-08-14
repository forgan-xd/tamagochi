import pygame,sys
from pygame import *
pygame.init
ventana= pygame.display.set_mode((1366,768)) #resolucion
pygame.display.set_caption("FORGANGOCHI") #titulo

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() # todo esto es para cerrar la pestaña