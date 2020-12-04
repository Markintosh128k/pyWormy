import pygame
import random
import os
from general import *

#Classe del serpente
class Verme:
    #Costruttore
    def __init__(self, screen, pixel):
        self.screen = screen

        # posizioni x ed y attuali del verme
        self.x = 240
        self.y = 240

        # variabile che ci dice la direzione del verme
        self.direzione = 1

        # Caricamento immagini testa
        # 0 sopra, 1 destra, 2 giu, 3 sinistra
        self.testaList = ["Img/Sprites/Sprites3/TestaSopra.png","Img/Sprites/Sprites3/TestaDestra.png", "Img/Sprites/Sprites3/TestaGiu.png", "Img/Sprites/Sprites3/TestaSinistra.png"]
        assetTesta_url = resource_path(self.testaList[self.direzione])
        self.imgTesta = pygame.image.load(assetTesta_url)

        assetCorpo_url = resource_path("Img/Sprites/Sprites3/CorpoSerpente.png")
        self.imgCorpo = pygame.image.load(assetCorpo_url)

        # lista posizioni verme
        self.vermeImg = [self.imgCorpo,self.imgCorpo, self.imgTesta]
        self.vermeCord = [(self.x - 40, self.y), (self.x - 20, self.y), (self.x, self.y)]
        self.vermeDir = [self.direzione, self.direzione, self.direzione]


        # effetto sonoro, si attiva quando una mela viene mangiata
        assetSuono_url = resource_path("Sounds/slurp.wav")
        self.sound = pygame.mixer.Sound(assetSuono_url)

        # direzioni x e y del vermi
        self.change_x = 20
        self.change_y = 0

        # grandezza della cella del seprente
        self.size = pixel

        # mangiato = True se ha mangiato la mela, mangiato = False se non ha ancora mangiato la mela
        self.mangiato = False


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

    # Funzione per cambaire direzione
    def muoviDown(self):
        if self.direzione != 0:
            self.change_x = 0
            self.change_y = self.size
            self.direzione = 2

    # Funzione per cambaire direzione
    def muoviUp(self):
        if self.direzione != 2:
            self.change_x = 0
            self.change_y = - self.size
            self.direzione = 0

    # Funzione per cambaire direzione
    def muoviRight(self):
        if self.direzione != 3:
            self.change_x = self.size
            self.change_y = 0
            self.direzione = 1

    # Funzione per cambaire direzione
    def muoviLeft(self):
        if self.direzione != 1:
            self.change_y = 0
            self.change_x = - self.size
            self.direzione = 3

    def muovi(self):
        self.x += self.change_x
        self.y += self.change_y

    def popAppend(self):
        # aggiungo le nuove coordinate
        self.vermeCord.append((self.x, self.y))
        self.vermeCord.pop(0)

        # aggiungo la nuova diezione
        self.vermeDir.append(self.direzione)
        self.vermeDir.pop(0)

        # assegno le immagini
        assetTesta_url = resource_path(self.testaList[self.vermeDir[-1]])
        self.imgTesta = pygame.image.load(assetTesta_url)

        # cambiamo le immgaini nella lista
        self.vermeImg[-1] = self.imgTesta

    # Funzione che controlla se il serpente ha mangiato se stesso
    def checkEatItSelf(self):
        finto = False
        for i in range(len(self.vermeCord) - 1):
            if self.vermeCord[-1] == self.vermeCord[i]:
                finto = True

        return finto

    # Funzione che controlla se il serpente ha mangiato la mela
    def mangiaMele(self, mx, my):
        if self.x == mx and self.y == my:
            self.vermeCord.append((self.x, self.y))
            self.vermeImg.append(self.imgTesta)
            self.vermeImg[-2] = self.imgCorpo
            self.mangiato = True
            self.sound.play()
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

        #grandezza
        self.size = pixel

        # prende l'immagine della mela dalla cartella
        self.melaList = ["Img/Sprites/Sprites3/Mela/brackets.png", "Img/Sprites/Sprites3/Mela/cmd.png", "Img/Sprites/Sprites3/Mela/ciclofor.png", "Img/Sprites/Sprites3/Mela/puntoevirgola.png",]
       
        # Caricamento dello sprite
        n = random.randint(0, len(self.melaList)-1)
        assetMela_url = resource_path(self.melaList[n])
        self.imgLoad = pygame.image.load(assetMela_url)
        
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

        # Caricamento dello sprite
        n = random.randint(0, len(self.melaList)-1)
        assetMela_url = resource_path(self.melaList[n])
        self.imgLoad = pygame.image.load(assetMela_url)

    # Disegna la mela
    def disegna(self):
        self.screen.blit(self.imgLoad, (self.x, self.y))

