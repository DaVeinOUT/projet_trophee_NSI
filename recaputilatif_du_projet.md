# Récapitulatif + Informations sur notre projet.
## But du projet
Créer un **RPG (en 2D) avec Pygame**.  
Nous utiliserons des ressources **libres, prévues pour,** trouvées sur internet.

## Vocabulaire
- **DyNacrest:** Nom du RPG (Généré aléatoirement sur le site:https://fr.fantasynamegenerators.com/noms-de-jeux-vid%C3%A9os.php)
- **Repo:** Un dossier sur Github contenant 1 projet
- **Tick:** 1 tick correspond à 1 execution de la boucle de jeu
- **TPS:** (Tick Par Seconde), correspond au nombre de fois que la boucle de jeu s'execute
- **Event/Évenement:** Qqch déclenché par une action de la personne sur son ordinateur ou directement en jeu.
- **Tuile:** Image de décor destinée à faire parti d'une map
- **Sprite:** Image d'une entitée, d'un personnage à un état fixe
- **Animation:** Regroupement de plusieurs sprites destinés à créer une animation
- **Frame:** Image d'une animation. Les frames sont stockées dans un certain ordre.
- **Map:** Regroupement de plusieurs tuiles destinées à créer un décor de jeu
- **Mapping:** Toutes choses relatives aux maps
- **CSV:** Format de stockage d'une map
- **Charger qqch:** Le stocker sous forme d'image/Le faire apparaître sur l'écran
- **Tileset:** Regroupement de plusieurs sprites/tuiles destinées à être séparés.
- **Collisions:** Le fait que certain éléments stoppent la progression du joueur
- **Hitbox:** Zone sensible d'un élément de jeu aux attaques et collisions
- **Masque:** Objet que l'on met par dessus un rectangle pygame afin de créer des collisions basées sur la transparence
- **Timing(s):** Tout ce qui est en rapport avec le temps.
- **Markdown:** Langage de balisage utilisé pour faire nos rapports.
## Structure du projet
- **[DyNacrest](https://github.com/DaVeinOUT/projet_trophee_nsi)**
    - **classes/** (Contient les objets utilisés pour le projet)
        - **joueur.py** (Contient les fonctions relatives au joueur)
        - **mapping.py** (Contient les fonctions relatives a la création de map)
    - **constantes/** (Contient les constantes utilisées pour le projet)
        - **constantes_joueur.py** (Constantes relatives aux joueurs)
        - **constantes_partie.py** (Constantes relatives au jeu en lui même)
        - **constantes_tuiles.py** (Constantes relatives aux tuiles et aux maps)
    - **fonctions/** (Contient les fonctions utilisées pour le projet)
        - **charger.py** (Fonctions pour charger des images)
        - **jeu.py** (Contient les fonctions d'évents et de boucle de jeu)
    - **images/** (Contient les images utilisées pour le projet)
        - **ecrans/** (Contient les écrans d'aide, chargement etc)
        - **sprites/** (Contient les sprites)
        - **tuiles/** (Contient les tuiles)
        - **icone.png** (Contient l'icone du jeu)
    - **maps/** (Contient les maps utilisées pour le projet)
        - **x_0.csv** (Couche 0 de la map "x")
        - **x_1.csv** (Couche 1 de la map "x")
        - **x_2.csv** (Couche 2 de la map "x")
        - **x_3.csv** (Couche 3 de la map "x")
    - **main.py** (Fichier principal, celui que l'on doit executer)
    
## Tâches a faire!
- Hitboxs (DAVIDSON)
- Modification de la carte (Anthoni) + Dimensions de la carte a bonne échelle (en tuiles), des petites maps etc.
- Ajouter des bruitages/Musiques + implémentation en algo/python (Anthoni)
- Masques (Davidson)
- Collisions (Davidson)
- Créer une map simple (1 seul tile) (Felipe)
- Ajouter des tiles a la map (Felipe)
- Permettre aux maps de sortir de l'écran (Anthoni)
- Ajouter un personnage sans animation (Anthoni)
- Faire une map de test en 4 couches (Anthoni)
- Coder les deplacement du personnage (Davidson)
- Trouver un générateur de map (Felipe)
- S'adapter au générateur de map (Felipe)
- Musiques (kedmael)
- Classe ennemi (Davidson)
- Menu (Davidson)
- Histoire (Davidson)
- Choisir les sons et bruitages à ajouter au projet (kedmael)
- Créer des tuiles animés (Davidson)
- S'occuper de l'attaque et des animations (Anthoni)
- Téléportations d'une map à l'autre (Anthoni)
- Création des maps des téléportions (Davidson)
## ps:les taches que j'ai atribuer sont temporaires vous pouvez changer de tache si vous le voulez
