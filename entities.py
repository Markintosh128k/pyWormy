import pygame
import random
import os

#Classe del serpente
class Verme:
    #Costruttore
    def __init__(self, screen):
        self.screen = screen

        # Caricamento immagini testa
        #0 sopra, 1 destra, 2 giu, 3 sinistra
        self.testaList = ["Sprites/Sprites2/TestaSopra.png","Sprites/Sprites2/TestaDestra.png", "Sprites/Sprites2/TestaGiu.png", "Sprites/Sprites2/TestaSinistra.png"]
        self.imgTesta = pygame.image.load(self.testaList[0])

        # posizioni x ed y attuali del verme
        self.x = 240
        self.y = 240

        # direzioni x e y del vermi
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

    # Funzione per cambaire direzione
    def muovi(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.change_y = 20
            self.change_x = 0
            #tests giu
            self.imgTesta = pygame.image.load(self.testaList[2])

        elif key[pygame.K_UP]:
            self.change_y = -20
            self.change_x = 0
            #testa su
            self.imgTesta = pygame.image.load(self.testaList[0])


        if key[pygame.K_RIGHT]:
            self.change_x = 20
            self.change_y = 0
            #testa dx
            self.imgTesta = pygame.image.load(self.testaList[1])

        elif key[pygame.K_LEFT]:
            self.change_x = -20
            self.change_y = 0
            #testa sx
            self.imgTesta = pygame.image.load(self.testaList[3])

        self.x += self.change_x
        self.y += self.change_y

    # Procedura che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.x == mx and self.y == my:
            self.mangiato = True
        else:
            self.mangiato = False

        return self.mangiato

    # Disegna il serpente
    def disegna(self):
        self.screen.blit(self.imgTesta, (self.x, self.y))

#Classe mela
class Mela:

    # Costruttore
    def __init__(self, screen, pixel):
        self.screen = screen
        self.size = pixel

        # prende l'immagine della mela dalla cartella
        dir = os.path.dirname(__file__)
        dirMela = "Sprites/Sprites1/meloide.png"
        mela = os.path.join(dir, dirMela)

        #Caricamento dello sprite
        self.imgLoad = pygame.image.load(mela)

        # grandezza della cella della mela
        self.height = 20
        self.width = 20

        #posizioni x e y attuali della mela
        self.x = 0
        self.y = 0


    # Restituisce il valore della x
    def getX(self):
        return self.x

    # Restituisce il valore della y
    def getY(self):
        return self.y

    # Funzione che restituisce la x in una posizione random
    def spawn(self):
        n = 0
        finito = False
        while not finito:
            n = random.randint(40, 460)
            if n % self.size == 0:
                finito = True

        self.x = n
        self.y = n

    # Disegna la mela
    def disegna(self):
        self.screen.blit(self.imgLoad, (self.x, self.y))
        #pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])
