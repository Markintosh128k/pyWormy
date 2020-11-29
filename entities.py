import pygame
import random
import os

#Classe del serpente
class Verme:

    #Costruttore
    def __init__(self, screen):
        self.screen = screen
        img_verme = pygame.image.load("Wormy/sprite_serpente/testa_su_dx.png")
        self.img = pygame.image.load(img_verme)

        # posizioni x ed y del serpente
        self.x = 240
        self.y = 240

        # direzioni x e y del serpente
        self.change_x = 0
        self.change_y = 0

        # grandezza della cella del seprente
        self.height = 20
        self.width = 20

        # mangiato = True se ha mangiato la mela, mangiato = False se non ha ancora mangiato la mela
        self.mangiato = False

    # Restituisce il valore della x del serpente
    def getX(self):
        return self.x

    # Restituisce il valore della y del serpente
    def getY(self):
        return self.y

    # Restituise il booleno, True se il serpente ha mangiato la mela, False se il serpente non ha mangiato la mela
    def isMangiato(self):
        return self.mangiato

    # Funzione per cambaire direzione
    def spostamenti(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.change_y = 20
            self.change_x = 0
            #tests giu

        elif key[pygame.K_UP]:
            self.change_y = -20
            self.change_x = 0
            #testa su


        if key[pygame.K_RIGHT]:
            self.change_x = 20
            self.change_y = 0
            #testa dx

        elif key[pygame.K_LEFT]:
            self.change_x = -20
            self.change_y = 0
            #testa sx

        return self.change_x, self.change_y

    # Procedura per muovere in avanti il serprente
    def muovi(self, x, y):
        self.x += x
        self.y += y

    # Procedura che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.x == mx and self.y == my:
            self.mangiato = True
        else:
            self.mangiato = False

    # Disegna il serpente
    def disegna(self):
        self.screen.blit(self.img, (self.x, self.y))

#Classe mela
class Mela:

    # Costruttore
    def __init__(self, screen):
        self.screen = screen

        # prende l'immagine della mela dalla cartella
        base_path = os.path.dirname(__file__)
        mela = os.path.join(base_path, "meloide.png")
        self.img = pygame.image.load(mela)

        # grandezza della cella della mela
        self.height = 20
        self.width = 20

        # posizioni x ed y della mela
        self.x = self.spawnX()
        self.y = self.spawnY()

    # Setta il valore della x
    def setX(self, x):
        self.x = x

    # Setta il valore della y
    def setY(self, y):
        self.y = y

    # Restituisce il valore della x
    def getX(self):
        return self.x

    # Restituisce il valore della y
    def getY(self):
        return self.y

    # Funzione che restituisce la x in una posizione random
    def spawnX(self):   
        finito = False
        while not finito:
            self.x = random.randint(40, 460)
            if self.x % 20 == 0:
                finito = True
        return self.x

    # Funzione che restituisce la y in una posizione random
    def spawnY(self):
        finito = False
        while not finito:
            self.y = random.randint(40, 460)
            if self.y % 20 == 0:
                finito = True

        return self.y

    # Disegna la mela
    def disegna(self):
        self.screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])



#BUONE IDEE PROGETTUALI PER DOPO
"""    class MelaSpeciale(Mele):
        
        def __init__(self):

            Mele.__init__()"""