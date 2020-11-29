import pygame
import random
import os

#Classe del serpente
class Verme:
    #Costruttore
    def __init__(self, screen):
        self.screen = screen

        # Caricamento immagini testa
        self.testaGiu = "sprites/sprite_serpente/testa/testa1.png"
        self.testaSu = "sprites/sprite_serpente/testa/testa3.png"
        self.testaDx = "sprites/sprite_serpente/testa/testa2.png"
        self.testaSx = "sprites/sprite_serpente/testa/testa4.png"

        # Caricamento dello sprite della testa
        self.imgTesta = pygame.image.load(self.testaSu)

        #Lunghezza
        #self.vermeLenght = 1
        '''self.vermeList = []
        self.vermeList.append(self.imgTesta)'''

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
            self.imgTesta = pygame.image.load(self.testaGiu)

        elif key[pygame.K_UP]:
            self.change_y = -20
            self.change_x = 0
            #testa su
            self.imgTesta = pygame.image.load(self.testaSu)


        if key[pygame.K_RIGHT]:
            self.change_x = 20
            self.change_y = 0
            #testa dx
            self.imgTesta = pygame.image.load(self.testaDx)

        elif key[pygame.K_LEFT]:
            self.change_x = -20
            self.change_y = 0
            #testa sx
            self.imgTesta = pygame.image.load(self.testaSx)

        return self.change_x, self.change_y

    # Procedura per muovere in avanti il serprente
    def muovi(self, x, y):
        self.x += x
        self.y += y

    # Procedura che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.x == mx and self.y == my:
            #self.vermeLenght += 1
            '''self.vermeList.append(self.imgTesta)
            print(self.vermeList)'''
            self.mangiato = True
        else:
            self.mangiato = False

    # Disegna il serpente
    def disegnaTesta(self):
        for img in self.vermeList:
            self.screen.blit(self.imgTesta, (self.x, self.y))


#Classe mela
class Mela:

    # Costruttore
    def __init__(self, screen):
        self.screen = screen

        # prende l'immagine della mela dalla cartella
        dir = os.path.dirname(__file__)
        dirMela = "sprites/meloide.png"
        mela = os.path.join(dir, dirMela)
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

class Sfondo:
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
