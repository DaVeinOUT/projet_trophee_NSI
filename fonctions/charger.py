import pygame

def load_game():
    # Initialisation de pygame
    pygame.init()

    # Définition de la taille de la fenêtre
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Titre de la fenêtre
    pygame.display.set_caption("Nom du jeu")

    # Boucle principale du jeu
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualisation de l'écran
        pygame.display.update()

    # Fermeture de la fenêtre pygame
    pygame.quit()
