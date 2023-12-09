import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("pygame platrofmer")

#update screen
pygame.display.flip()

#boolean window is running
running = True

while running:
    for event in pygame.event.get():

        #check if window was closed 
        if event.type == pygame.QUIT:
            running = False



