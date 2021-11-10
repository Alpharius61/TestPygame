import pygame


class Game :

    def __init__(self) :
       # créer fenêtre
        pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygame Test")

    def run(self) :
        # boucle du jeu (maintien de la fenêtre plus quitter)
        running = True
        while running == True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    running = False

        pygame.quit()
