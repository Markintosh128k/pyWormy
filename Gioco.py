from Entities import *
from Control import *
from PyGimager import *
import pygame
import sys

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Larghezza e altezza finestera
WIN_WIDTH = 1000
WIN_HEIGHT = 900

# Posizioni da dove parte la griglia
START_WIDHT = 100
START_HEIGHT = 40
END_WIDTH = 940
END_HEIGHT = 800

# Grandezza celle
CELL_SIZE = 20

#COLORI
PINK = (222, 50, 235)

# Percorsi gif
btnMainPathList = ['Img/Buttons/Play.gif', 'Img/Buttons/Options.gif', 'Img/Buttons/Exit.gif']
saveMainPathList = [('PlayButton', 'Img/Buttons/Play/'), ('OptionsButton', 'Img/Buttons/Options/'), ('ExitButton', 'Img/Buttons/Exit/')]
# Carico file per l'eseguie
for gif in btnMainPathList:
    resource_path(gif)


btnOptionsPathList = ['Img/Buttons/Easy.gif', 'Img/Buttons/Hard.gif']
saveOptionsPathList = [('EasyButton', 'Img/Buttons/Easy/'), ('HardButton', 'Img/Buttons/Hard/')]
# Carico file per l'eseguie
for gif in btnOptionsPathList:
    resource_path(gif)


btnGameOverPathlist = ['Img/Buttons/BackToMenu.gif', 'Img/Buttons/Exit.gif']
saveGameOverPathList = [('BacktoMenuButton', 'Img/Buttons/BackToMenu/'), ('ExitButton', 'Img/Buttons/Exit/')]
resource_path('Img/Buttons/BackToMenu.gif')


# caricamento immagine sfondo menù
assetMenu_url = resource_path("Img/startMenu.png")
sfondoMenu = pygame.image.load(assetMenu_url)
assetMenuSound_url = resource_path("Sounds/musica.wav")
musicaMenu = pygame.mixer.Sound(assetMenuSound_url)

# caricamento delle musiche
assetHardSound_url = resource_path("Sounds/difficileSottofondo.wav")
musicaHard = pygame.mixer.Sound(assetHardSound_url)

assetEasySound_url = resource_path("Sounds/facileSottofondo.wav")
musicaEasy = pygame.mixer.Sound(assetEasySound_url)

# Font
assetFONT_OBJ_url = resource_path('SF_Pixelate.ttf')
FONT_OBJ = pygame.font.Font(assetFONT_OBJ_url, 70)

# Creazione menu options
def options():
    optionsMenu = Bottoni(screen, 480, 300, btnOptionsPathList, saveOptionsPathList, sfondoMenu)

    finito = False
    while not finito:
        optionsMenu.start()
        if optionsMenu.getBottonePremuto() == 0:
            velocitaMAX = 15
            musica = musicaEasy
            finito = True

        elif optionsMenu.getBottonePremuto() == 1:
            velocitaMAX = 40
            musica = musicaHard
            finito = True

    return velocitaMAX, musica


# Creazione menu gameover
def messaggioGameOver(screen, punteggio):
    assetgameOverSound_url = resource_path("Sounds/lose.wav")
    gameOverSound = pygame.mixer.Sound(assetgameOverSound_url)

    assetGameOverImg_url = resource_path("Img/GameOver.png")
    gameOverImg = pygame.image.load(assetGameOverImg_url)

    gameOverSound.play()
    gameoverMenu = Bottoni(screen, 480, 600,btnGameOverPathlist, saveGameOverPathList, gameOverImg)
    scelta = ''
    finito = False
    while not finito:
        gameoverMenu.start(1, punteggio, FONT_OBJ, 540, 414, YELLOW)
        if gameoverMenu.getBottonePremuto() == 0: # andare al menu principlale
            scelta = 'mainMenu'
            finito = True
        elif gameoverMenu.getBottonePremuto() == 1: # exit
            scelta = 'exit'
            finito = True
        pygame.display.update()

    return scelta


# gioco
def game(velocitaMAX, musica):
    # Velocita' del serpente (in frame per secondo)
    velocita = 10
    fps = pygame.time.Clock()

    # Oggetti
    verme = Verme(screen, CELL_SIZE, START_WIDHT, START_HEIGHT, END_WIDTH, END_HEIGHT)
    mele = Mela(screen, CELL_SIZE, START_WIDHT, START_HEIGHT, END_WIDTH, END_HEIGHT)

    # Inizializzazione varibili utili
    gameover = False
    assetSfondo = resource_path("Img/background.png")
    bg = pygame.image.load(assetSfondo)
    bg = pygame.transform.scale(bg, (1000, 900))
    punteggio = 0

    mele.spawn()
    musica.play(-1)
    while not gameover:
        melaX = mele.getX()
        melaY = mele.getY()
        screen.blit(bg, (0, 0))
        # disegnaGriglia(screen)
        score(screen, punteggio, 290, 831)
        mele.disegna()
        verme.disegna()

        # seleziona i comandi
        gameover = verme.comandi()
        
        if verme.mangiaMele(melaX, melaY):
            mele.spawn()
            punteggio += 1
            if velocita <= velocitaMAX:
                velocita += 1

        pygame.display.update()
        fps.tick(velocita)

    musica.stop()
    return messaggioGameOver(screen, punteggio)


if __name__ == "__main__":

    # Creazione della finestra (screen)
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("pyWormy")

    # Set del modalità default
    velocitaMAX = 15
    musica = musicaEasy

    # Creazione menu principlae
    mainMenu = Bottoni(screen, 480, 300, btnMainPathList, saveMainPathList, sfondoMenu)

    finito = False
    scelta = ''

    musicaMenu.play(-1)

    while not finito:
        mainMenu.start()
        if mainMenu.getBottonePremuto() == 0:
            musicaMenu.stop()
            gameover = False
            while not gameover:
                if game(velocitaMAX, musica) == 'exit':
                    finito = True
                gameover = True

        elif mainMenu.getBottonePremuto() == 1:
            velocitaMAX, musica = options()

        elif mainMenu.getBottonePremuto() == 2:
            finito = True
        pygame.display.update()


    musicaMenu.stop()
    pygame.quit()
    sys.exit()
