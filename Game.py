import pygame
import pytmx
import pyscroll


class Game :

    def __init__(self) :
       # créer fenêtre de jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygame Test")
    
        # charger carte (tmx)
        tmxData = pytmx.util_pygame.load_pygame('Map.tmx')
        mapData = pyscroll.data.TiledMapData(tmxData)
        mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
        mapLayer.zoom = 2


        # dessiner le gp de calques
        self.group = pyscroll.PyscrollGroup(map_layer = mapLayer, default_layer = 1)

    def run(self) :
        # boucle du jeu (maintien de la fenêtre plus quitter)
        running = True
        while running == True :
            
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    running = False

        pygame.quit()
