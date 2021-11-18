import pygame
import pytmx
import pyscroll
from Player import Player


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

        #  generer un joueur
        player_position = tmxData.get_object_by_name("Player")
        self.player = Player(player_position.x,player_position.y)

        # générer les zones interdite (collision)
        self.walls = []

        for object in tmxData.objects :
            if object.type == 'collision' :
                self.walls.append(pygame.Rect(object.x , object.y , object.width, object.height))

        # dessiner le gp de calques
        self.group = pyscroll.PyscrollGroup(map_layer = mapLayer, default_layer = 5)
        self.group.add(self.player)



        # definir le rectangle de collision pour entrer dans la maison
        enterHouse= tmxData.get_object_by_name("enterHouse")
        self.enterHouseRect = pygame.rect(enterHouse.x , enterHouse.y, enterHouse.width, enterHouse.height)

    def handleInput(self):

        """
        Intercepte les commande (fleche du clavier)
        
        """
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.moveUp()
            self.player.changeAnimation("up")

        elif pressed[pygame.K_DOWN]:
            self.player.moveDown()
            self.player.changeAnimation("down")

        elif pressed[pygame.K_LEFT]:
            self.player.moveLeft()
            self.player.changeAnimation("left")

        elif pressed[pygame.K_RIGHT]:
            self.player.moveRight()
            self.player.changeAnimation("right")

    def update(self):
        self.group.update()
        # vérification de l'entré dans la maison
        if self.player.feet.colliderect(self.enterHouseRect):
            self.switchHouse()
        # vérification des collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.moveBack()

    def switchHouse(self):
        # charger carte (tmx)
        tmxData = pytmx.util_pygame.load_pygame('House.tmx')
        mapData = pyscroll.data.TiledMapData(tmxData)
        mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
        mapLayer.zoom = 2

        #  generer un joueur
        player_position = tmxData.get_object_by_name("Player")
        self.player = Player(player_position.x,player_position.y)

        # générer les zones interdite (collision)
        self.walls = []

        for object in tmxData.objects :
            if object.type == 'collision' :
                self.walls.append(pygame.Rect(object.x , object.y , object.width, object.height))

        # dessiner le gp de calques
        self.group = pyscroll.PyscrollGroup(map_layer = mapLayer, default_layer = 5)
        self.group.add(self.player)



        # definir le rectangle de collision pour entrer dans la maison
        enterHouse= tmxData.get_object_by_name("enterHouse")
        self.enterHouseRect = pygame.rect(enterHouse.x , enterHouse.y, enterHouse.width, enterHouse.height)


    def run(self) :
        #  Reglage des FPS
        clock = pygame.time.Clock()

        # boucle du jeu (maintien de la fenêtre plus quitter)
        running = True
        while running == True :
            self.player.saveLocation()
            self.handleInput()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    running = False

            clock.tick(60)     

        pygame.quit()
