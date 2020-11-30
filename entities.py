import pygame
import random
import os

#Classe del serpente
class Verme:
    #Costruttore
    def __init__(self, screen, x, y, selzioneImg=0):
        self.screen = screen

        # Caricamento immagini
        if selzioneImg == 0:
            #0 sopra, 1 destra, 2 giu, 3 sinistra
            self.img = ["Sprites/Sprites2/TestaSopra.png", "Sprites/Sprites2/TestaDestra.png", "Sprites/Sprites2/TestaGiu.png", "Sprites/Sprites2/TestaSinistra.png"]
        elif selzioneImg == 1:
            self.img = ["Sprites/Sprites2/CorpoVerticale.png", "Sprites/Sprites2/CorpoOrizzontale.png", "Sprites/Sprites2/CorpoVerticale.png", "Sprites/Sprites2/CorpoOrizzontale.png"]
        elif selzioneImg == 2:
            self.img = ["Sprites/Sprites2/CodaSopra.png", "Sprites/Sprites2/CodaDestra.png", "Sprites/Sprites2/CodaGiu.png", "Sprites/Sprites2/CodaSinistra.png"]

        # Caricamento dello sprite
        self.imgLoad = pygame.image.load(self.img[1])
        self.rectImg = self.imgLoad.get_rect()

        # posizioni x ed y del serpente
        self.rectImg.x = x
        self.rectImg.y = y

        # grandezza della cella del seprente
        self.height = 20
        self.width = 20

        # mangiato = True se ha mangiato la mela, mangiato = False se non ha ancora mangiato la mela
        self.mangiato = False



    # Restituisce il valore della x del serpente
    def getX(self):
        return self.rectImg.x

    # Restituisce il valore della y del serpente
    def getY(self):
        return self.rectImg.y
    # Restituisce la posizione
    def getPosizione(self):
        return self.rectImg

    # Restituise il booleno, True se il serpente ha mangiato la mela, False se il serpente non ha mangiato la mela
    def isMangiato(self):
        return self.mangiato

    # Funzione per cambaire direzione
    def spostamenti(self):
        change_x = 0
        change_y = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            change_y = 20
            change_x = 0
            #tests giu
            self.imgLoad = pygame.image.load(self.img[2])

        elif key[pygame.K_UP]:
            change_y = -20
            change_x = 0
            #testa su
            self.imgLoad = pygame.image.load(self.img[0])


        if key[pygame.K_RIGHT]:
            change_x = 20
            change_y = 0
            #testa dx
            self.imgLoad = pygame.image.load(self.img[1])

        elif key[pygame.K_LEFT]:
            change_x = -20
            change_y = 0
            #testa sx
            self.imgLoad = pygame.image.load(self.img[3])

        self.rectImg.x += change_x
        self.rectImg.y += change_y



    # Procedura che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.rectImg.x == mx and self.rectImg.y == my:
            self.mangiato = True
        else:
            self.mangiato = False

    # Disegna il serpente
    def disegnaTesta(self):
        self.screen.blit(self.imgLoad, self.rectImg)

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
        self.rectImg = self.imgLoad.get_rect()

        # grandezza della cella della mela
        self.height = 20
        self.width = 20

        self.spawn()

    # Restituisce il valore della x
    def getX(self):
        return self.rectImg.x

    # Restituisce il valore della y
    def getY(self):
        return self.rectImg.y

    # Funzione che restituisce la x in una posizione random
    def spawn(self):
        n = 0
        finito = False
        while not finito:
            n = random.randint(40, 460)
            if n % self.size == 0:
                finito = True

        self.rectImg.x = n
        self.rectImg.y = n

    # Disegna la mela
    def disegna(self):
        self.screen.blit(self.imgLoad, self.rectImg)
        #pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])
