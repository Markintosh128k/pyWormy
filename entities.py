import pygame
import random
import os

#Classe del serpente
class Verme:
    #Costruttore
    def __init__(self, screen, pixel):
        self.screen = screen
        # Caricamento immagini testa

        #0 sopra, 1 destra, 2 giu, 3 sinistra
        self.testaList = ["Sprites/Sprites2/TestaSopra.png","Sprites/Sprites2/TestaDestra.png", "Sprites/Sprites2/TestaGiu.png", "Sprites/Sprites2/TestaSinistra.png"]
        self.corpoList = ["Sprites/Sprites2/CorpoVerticale.png","Sprites/Sprites2/CorpoOrizzontale.png", "Sprites/Sprites2/CorpoVerticale.png", "Sprites/Sprites2/CorpoOrizzontale.png"]
        self.codaList = ["Sprites/Sprites2/CodaSopra.png","Sprites/Sprites2/CodaDestra.png", "Sprites/Sprites2/CodaGiu.png", "Sprites/Sprites2/CodaSinistra.png"]

        self.imgTesta = pygame.image.load(self.testaList[1])
        self.imgCorpo = pygame.image.load(self.corpoList[1])
        self.imgCoda = pygame.image.load(self.codaList[1])

        # posizioni x ed y attuali del verme
        self.x = 240
        self.y = 240

        # direzioni x e y del vermi
        self.change_x = 20
        self.change_y = 0

        # grandezza della cella del seprente
        self.size = pixel

        # mangiato = True se ha mangiato la mela, mangiato = False se non ha ancora mangiato la mela
        self.mangiato = False

        self.vermeImg = [self.imgCoda, self.imgCorpo, self.imgTesta]
        self.vermeCord = [(self.x - 40, self.y), (self.x - 20, self.y), (self.x, self.y),]

    # Restituisce il valore posizione del serpente
    def getPosizione(self):
        return self.vermeCord[0]

    # Funzione che restituisce se il verme va fuori dai bordi
    def controlloBordi(self):
        finito = False
        x = self.vermeCord[-1][0]
        y = self.vermeCord[-1][1]
        if x >= 500:
            finito = True
        if x <= 0:
            finito = True
        if y >= 500:
            finito = True
        if y <= 0:
            finito = True

        return finito

    '''
    def caricaImg(self, old_x, old_y):
        for block in range(len(self.vermeImg)):
            img = self.vermeImg[block]
            x = self.vermeCord[block][0]
            y = self.vermeCord[block][1]

            # verso destra
            if self.x + self.change_x > self.x:
                if block == 0:
                    #coda
                    img = self.codaList[1]
                elif block == len(self.vermeImg) - 1:
                    #testa
                    img = self.testaList[1]
                else:
                    #corpo
                    img = self.codaList[1]

            # verso sinistra
            elif self.x + self.change_x < self.x:
                if block == 0:
                    #coda
                    img = self.codaList[3]
                elif block == len(self.vermeImg) - 1:
                    #testa
                    img = self.testaList[3]
                else:
                    #corpo
                    img = self.codaList[3]

            # verso sotto
            elif self.y + self.change_y > self.y:
                if block == 0:
                    #coda
                    img = self.codaList[2]
                elif block == len(self.vermeImg) - 1:
                    #testa
                    img = self.testaList[2]
                else:
                    #corpo
                    img = self.codaList[2]

            # verso sopra
            elif self.y + self.change_y < self.y:
                if block == 0:
                    #coda
                    img = self.codaList[0]
                elif block == len(self.vermeImg) - 1:
                    #testa
                    img = self.testaList[0]
                else:
                    #corpo
                    img = self.codaList[0]

            self.vermeImg[block] = img
        '''


    # Funzione per cambaire direzione
    def muovi(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.change_y = self.size
            self.change_x = 0
            #tests giu

        elif key[pygame.K_UP]:
            self.change_y = -self.size
            self.change_x = 0
            #testa su

        if key[pygame.K_RIGHT]:
            self.change_x = self.size
            self.change_y = 0
            #testa dx

        elif key[pygame.K_LEFT]:
            self.change_x = -self.size
            self.change_y = 0
            #testa sx

        '''
        self.imgTesta = self.vermeImg[-1]
        x = self.vermeCord[-1][0]
        y = self.vermeCord[-1][1]

        # verso destra
        if self.x + self.change_x > self.x:
            #testa
            self.imgTesta = self.testaList[1]

        # verso sinistra
        elif self.x + self.change_x < self.x:
            self.imgTesta = self.testaList[3]

        # verso sotto
        elif self.y + self.change_y > self.y:
            self.imgTesta = self.testaList[2]

        # verso sopra
        elif self.y + self.change_y < self.y:
            self.imgTesta = self.testaList[0]

        self.vermeImg.append(self.imgTesta)
        self.vermeImg.pop(0)
        self.vermeImg[0] = self.imgCoda
        self.vermeImg[1] = self.imgCorpo
        '''
        self.x += self.change_x
        self.y += self.change_y

        self.vermeCord.append((self.x, self.y))
        self.vermeCord.pop(0)
        print(self.vermeCord)




    # Funzione che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.x == mx and self.y == my:
            self.vermeCord.append((self.x, self.y))
            self.vermeImg.append(self.imgTesta)
            self.vermeImg[-2] = self.imgCorpo
            self.mangiato = True
        else:
            self.mangiato = False

        return self.mangiato

    # Disegna il serpente
    def disegna(self):
        for block in range(len(self.vermeCord)):
            self.screen.blit(self.vermeImg[block], self.vermeCord[block])

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
        n = random.randint(4, 46) * 10
        if n % self.size != 0:
                n += 10
        self.x = n

        n = random.randint(4, 46) * 10
        if n % self.size != 0:
            n += 10
        self.y = n

    # Disegna la mela
    def disegna(self):
        self.screen.blit(self.imgLoad, (self.x, self.y))

