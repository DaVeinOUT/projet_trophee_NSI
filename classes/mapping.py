import pygame 
def mapping(carte, tuiles, ecran):
    # Récupérer la taille de la carte en nombre de tuiles
    nb_lignes = len(carte)
    nb_colonnes = len(carte[0])
    
    # Parcourir toutes les tuiles de la carte et les afficher sur l'écran
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            # Récupérer le numéro de tuile correspondant à cette case
            num_tuile = carte[ligne][colonne]
            
            # Récupérer l'image correspondant à cette tuile
            image_tuile = tuiles[num_tuile]
            
            # Calculer les coordonnées de l'image sur l'écran
            x = colonne * TAILLE_TUILE
            y = ligne * TAILLE_TUILE
            
            # Afficher l'image sur l'écran aux coordonnées calculées
            ecran.blit(image_tuile, (x, y))
