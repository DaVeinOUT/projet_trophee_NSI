import pygame

pygame.init()

pygame.display.set_caption("jeux de voiture")
screen = pygame.display.set_mode((900, 700))

run = True
while run:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
