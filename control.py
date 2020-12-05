import pygame
import os
import sys
from pyGimager import *

pygame.init()

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (217, 210, 57)
PINK = (222, 50, 235)

# Larghezza e altezza finestera
START_WIDHT = 120
START_HEIGHT = 60
END_WIDTH = 940
END_HEIGHT = 800

# Grandezza celle
CELL_SIZE = 20

# Dichiarazione Font
assetFONT_OBJ_url = resource_path('SF_Pixelate.ttf')
FONT_OBJ = pygame.font.Font(assetFONT_OBJ_url, 25)
FONT_OBJ1 = pygame.font.Font(assetFONT_OBJ_url, 25)

# Musica
assetSound_url = resource_path("Sounds/musica.wav")
sound = pygame.mixer.Sound(assetSound_url)


# play button
btnPlay = pyGimager('Img\Buttons\Play.gif')
btnPlay.deconstructGif('PlayButton', 'Img/Buttons/Play/')
btnPlay.gifLoader('Img/Buttons/Play/')

# options button
btnOptions = pyGimager('Img\Buttons\Options.gif')
btnOptions.deconstructGif('OptionsButton', 'Img/Buttons/Options/')
btnOptions.gifLoader('Img/Buttons/Options/')

# exit button
btnExit = pyGimager('Img\Buttons\Exit.gif')
btnExit.deconstructGif('ExitButton', 'Img/Buttons/Exit/')
btnExit.gifLoader('Img/Buttons/Exit/')

# easy button
btnEasy = pyGimager('Img\Buttons\Easy.gif')
btnEasy.deconstructGif('EasyButton', 'Img/Buttons/Easy/')
btnEasy.gifLoader('Img/Buttons/Easy/')

# hard button
btnHard = pyGimager('Img\Buttons\Hard.gif')
btnHard.deconstructGif('HardButton', 'Img/Buttons/Hard/')
btnHard.gifLoader('Img/Buttons/Hard/')

#Procedurea per stampre a schermo una scritta
def disegnaTesto(text, font, color, screen, x, y):
    text_obj = font.reder(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)

def score(screen, score):
    text = FONT_OBJ1.render(str(score), True, PINK)
    screen.blit(text, [290, 831])

def startMenu(screen):
    # caricamento immagine sfondo menu
    assetMenu_url = resource_path("Img/menu.png")
    bgMenu = pygame.image.load(assetMenu_url)
    bgMenu = pygame.transform.scale(bgMenu, (1000, 900))


    # avvio musica
    sound.play(-1)

    # azione fatta
    azione = 'nessuna'

    # controllo azioni del menu
    finito = False
    click = False
    while not finito:
        screen.blit(bgMenu, (0, 0))

        # prendi posizioni mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # disegna pulsanti

        
        #btnPlay.gifPlayer(screen, (350,350), 500, (300,50))

        

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                azione = 'esci'
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    azione = 'esci'
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

    pygame.mixer.Sound.stop(sound)
    return azione


# Procedura per diegnare la griglia
def disegnaGriglia(screen):
    for x in range(START_WIDHT, END_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, START_HEIGHT), (x, END_HEIGHT), 1)

    for y in range(START_HEIGHT, END_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (START_WIDHT, y), (END_WIDTH, y), 1)


# Funzione per stampare il messaggio di gameover con relativo punteggio
'''def messaggioGameOver(screen, score=0):
    mystr = str(score)
    assetGameOver_url = resource_path("Img/GameOver.png")
    gameOver = pygame.image.load(assetGameOver_url)

    screen.blit(gameOver, (0, 0))
    text = FONT_OBJ.render(str(score), True, YELLOW)
    screen.blit(text, [240, 373])

    return tastiEscSpace()'''

