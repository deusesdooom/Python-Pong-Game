import pygame
from pygame import *
from math import *


init() ## initialise différentes choses de pygame. Faut le mettre car ca marche mieux avec que sans
fenetre = display.set_mode((1297, 720), RESIZABLE)

pygame.mixer.init() #gestion du son
start_sound = pygame.mixer.Sound("start_sound.wav")
goal_sound = pygame.mixer.Sound("goal_sound.wav")
win_sound = pygame.mixer.Sound("win_sound.wav")

## Ouvre notre fenêtre pygame. il faudra peut être ouvrir une fenêtre avec des
## dimensions plus grande si votre image dépasse la taille 640*480

fond = image.load("fond.jpg").convert()## python charge votre image en mémoire, elle n’est pas
                                        ## encore à l’écran.


balle = image.load("ball.png").convert_alpha()
font = font.SysFont("broadway", 80, bold=True, italic=False)
rack = image.load("raquette.png").convert_alpha()

##for x in range (balle.get_size()[0]):
    ##for y in range (balle.get_size()[1]):
        ##(r,v,b,t)=balle.get_at((x,y))
        ##if r+b+v>700:
            ##balle.set_at((x,y),(r,v,b,0))
            ##fenetre.blit(balle, (x,y))

            
##for x in range (raquette.get_size()[0]):
    ##for y in range (raquette.get_size()[1]):
        ##(r,v,b,t)=raquette.get_at((x,y))
        ##if r+b+v>700:
            ##raquette.set_at((x,y),(r,v,b,0))

bu = "but"
but = font.render("but", 1, (255, 255, 0))
j1 = 0
j2 = 0
xb = 400
yb = 0
xr = 0
yr = 0
xr1 = 0
xr2 = 1200
yr1 = 0
yr2 = 0
chaine = 2
continuer = 1
deplacement_x = 3
deplacement_y = 6

start_sound.play()

while continuer == 1: #on continue tant que continuer=1.
    time.Clock().tick(200)# bridage de la vitesse à 200 tour de boucle/seconde

    for evenements in event.get():# on regarde tous les évènement possible depuis le dernier
        
#check sous forme de liste d’event.
        if evenements.type == QUIT:#si on a cliqué sur la croix fermant la fenêtre
            continuer = 0# continuer vaut 0 ce qui nous sortira de la boucle.

    keyb = key.get_pressed() # prend la cartographie du clavier, la variable contient
#maintenant une liste pour chaque touche sachant si elle est
#enfoncée (valeur 1) ou pas (valeur 0)
    # gestion du clavier
    
     #gestion de smash 
    if keyb[K_SPACE]:
        deplacement_x *= smash_multiplier
        deplacement_y *= smash_multiplier
    if keyb[K_UP]:
        if yr >= 0:
            yr = yr - 1 # gestion des déplacements de mon personnage.

    if keyb[K_DOWN]:
        if yr < 600:
            yr = yr + 1

    if keyb[K_LEFT]:
        if xr >= 170:
            xr = xr - 1

    if keyb[K_RIGHT]:
        if xr <= 1200:
            xr = xr + 1

    if keyb[K_w]:
        if yr2 >= 0:
            yr2 = yr2 - 1 # gestion des déplacements de mon personnage.

    if keyb[K_s]:
        if yr2 < 600:
            yr2 = yr2 + 1

    if keyb[K_a]:
        if xr2 >= 970:
            xr2 = xr2 - 1

    if keyb[K_d]:
        if xr2 <= 1200:
            xr2 = xr2 + 1
            
    #gestion de la balle
    xb += deplacement_x
    yb += deplacement_y

    if yb > fond.get_size()[1] - balle.get_size()[1] or yb < 0:
        deplacement_y = -deplacement_y

    if Rect((xb, yb), balle.get_size()).colliderect(Rect((xr2, yr2), rack.get_size())):
        deplacement_x = min(-1, -deplacement_x - 1)

    if Rect((xb, yb), balle.get_size()).colliderect(Rect((xr1, yr1), rack.get_size())):
        deplacement_x = max(1, deplacement_x + 1)
        
#gestion du mouvement des raquettes et de la balle
    if xb > 1496:
        j1 += 1
        goal_sound.play()
        yr2 = 450
        deplacement_x = 0
        time.wait(100)
        xb = 800
        yb = 450
        deplacement_x = 3

    if xb < -10:
        j2 += 1
        goal_sound.play()
        yr1 = 450
        deplacement_x = 0
        time.wait(100)
        xb = 800
        yb = 450
        deplacement_x = -3
        
    if j1 >= 10 or j2 >= 10:
        continuer = 0
        time.wait(3000)
        win_sound.play()
        
    # gestion de l'affichage
    scorej1 = font.render(str(j1), 1, (255, 0, 0))
    scorej2 = font.render(str(j2), 1, (0, 0, 255)) # réaffichage du fond (pour effacer l’ancienne position du personnage)
    
    # affiche le personnage à ses coordonnées
    fenetre.blit(fond, (0, 0))
    fenetre.blit(balle, (xb, yb))
    fenetre.blit(rack, (xr1, yr1))
    fenetre.blit(rack, (xr2, yr2))
    fenetre.blit(scorej1, (300, 200))
    fenetre.blit(scorej2, (950, 200))
    
    # voir si le joueur a gagner des qu'il a atteint 10 et afficher qu'il a ganger
    if j1 >= 10 or j2 >= 10:
        if j1 > j2:
            winner_text = font.render("Player 1 Wins!", 1, (255, 255, 0))
        else:
            winner_text = font.render("Player 2 Wins!", 1, (255, 255, 0))

        fenetre.blit(winner_text, (500, 400))

    display.flip() #rafraichi le tout

win_sound.play()

time.wait(4000)

quit()# fermeture propre du programme quand on sort de la boucle (bien respecter l’indentation)
