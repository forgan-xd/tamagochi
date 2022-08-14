import pygame
pygame.init

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

ventana= pygame.display.set_mode((1366,768)) #resolucion
pygame.display.set_caption("FORGANGOCHI") #titulo


    
