import pygame
pygame.init

runnin = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

ventana= pygame.display.set_mode((1366,768)) #resolucion
pygame.display.set_caption("FORGANGOCHI") #titulo


    for evento in pygame.event.get():
        if evento.type == quit:
            pygame.quit()
            sys.exit()

    pygame.display.update() # todo esto es para cerrar la pestaña
