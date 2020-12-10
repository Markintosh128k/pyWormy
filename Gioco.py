from Entities import *
from PyGimager import *
import pygame
import sys

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (222, 50, 235)
YELLOW = (217, 210, 57)

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

#BOTTONI
btnPlay = ['Img/Buttons/Play/PlayButton0.png', 'Img/Buttons/Play/PlayButton1.png']
btnOptions = ['Img/Buttons/Options/OptionsButton0.png', 'Img/Buttons/Options/OptionsButton1.png']
btnEasy = ['Img/Buttons/Easy/EasyButton0.png', 'Img/Buttons/Easy/EasyButton1.png']
btnHard = ['Img/Buttons/Hard/HardButton0.png', 'Img/Buttons/Hard/HardButton1.png']
btnExit = ['Img/Buttons/Exit/ExitButton0.png', 'Img/Buttons/Exit/ExitButton1.png']
btnBackMenu = ['Img/Buttons/BackToMenu/BacktoMenuButton0.png', 'Img/Buttons/BackToMenu/BacktoMenuButton0.png']

for btn in btnPlay:
    resource_path(btn)

for btn in btnOptions:
    resource_path(btn)

for btn in btnEasy:
    resource_path(btn)

for btn in btnHard:
    resource_path(btn)

for btn in btnExit:
    resource_path(btn)

for btn in btnBackMenu:
    resource_path(btn)


# SFONDI
assetMenu_url = resource_path("Img/startMenu.png")
sfondoMenu = pygame.image.load(assetMenu_url)

# MUSICA
assetMenuSound_url = resource_path("Sounds/musica.wav")
musicaMenu = pygame.mixer.Sound(assetMenuSound_url)

assetHardSound_url = resource_path("Sounds/difficileSottofondo.wav")
musicaHard = pygame.mixer.Sound(assetHardSound_url)

assetEasySound_url = resource_path("Sounds/facileSottofondo.wav")
musicaEasy = pygame.mixer.Sound(assetEasySound_url)

# FONT
assetFONT_OBJ_url = resource_path('SF_Pixelate.ttf')
FONT_END = pygame.font.Font(assetFONT_OBJ_url, 70)
FONT_SCORE = pygame.font.Font(assetFONT_OBJ_url, 25)

def score(screen, font, score, x ,y, color):
    text = font.render(str(score), True, color)
    screen.blit(text, [x, y])

# Procedura per diegnare la griglia
def disegnaGriglia(screen):
    for x in range(START_WIDHT, END_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, START_HEIGHT), (x, END_HEIGHT), 1)

    for y in range(START_HEIGHT, END_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (START_WIDHT, y), (END_WIDTH, y), 1)

# Creazione menu options
def options():

    imgEasy = pygame.image.load(btnEasy[1])
    rectEasy = imgEasy.get_rect(center=(480, 400))

    imgHard = pygame.image.load(btnHard[1])
    rectHard = imgHard.get_rect(center=(480, 500))

    finito = False
    click = False
    while not finito:
        # cattura posizione mouse
        mouse = pygame.mouse.get_pos()

        # Disegno sullo schermo
        screen.blit(sfondoMenu, (0, 0))
        screen.blit(imgEasy, rectEasy)
        screen.blit(imgHard, rectHard)

        if rectEasy.collidepoint(mouse):
            gifPlayer(screen, btnEasy, rectEasy, 100)
            if click:
                velocitaMAX = 15
                musica = musicaEasy
                finito = True

        elif rectHard.collidepoint(mouse):
                gifPlayer(screen, btnHard, rectHard, 100)
                if click:
                    velocitaMAX = 40
                    musica = musicaHard
                    finito = True


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    return velocitaMAX, musica

# Creazione menu gameover
def messaggioGameOver(screen, punteggio):

    # MUSICA
    assetgameOverSound_url = resource_path("Sounds/lose.wav")
    gameOverSound = pygame.mixer.Sound(assetgameOverSound_url)

    # SFONDO
    assetGameOverImg_url = resource_path("Img/GameOver.png")
    gameOverImg = pygame.image.load(assetGameOverImg_url)


    # Caricamento img
    imgBack = pygame.image.load(btnBackMenu[1])
    rectBack = imgBack.get_rect(center=(480, 600))

    imgExit = pygame.image.load(btnExit[1])
    rectExit = imgExit.get_rect(center=(480, 700))

    finito = False
    click = False

    gameOverSound.play()
    azione = ''
    while not finito:
        # cattura posizione mouse
        mouse = pygame.mouse.get_pos()

        # Disegno sullo schermo
        screen.blit(gameOverImg, (0, 0))
        score(screen, FONT_END, punteggio, 540, 414, YELLOW)
        screen.blit(imgBack, rectBack)
        screen.blit(imgExit, rectExit)

        if rectBack.collidepoint(mouse):
            gifPlayer(screen, btnBackMenu, rectBack, 100)
            if click:
                azione = 'mainMenu'
                finito = True

        elif rectExit.collidepoint(mouse):
            gifPlayer(screen, btnExit, rectExit, 100)
            if click:
                azione = 'exit'
                finito = True

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    return azione


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
        score(screen, FONT_SCORE, punteggio, 290, 831, PINK)
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
    finito = False
    click = False

    musicaMenu.play(-1)

    # Caricamento img
    imgPlay = pygame.image.load(btnPlay[1])
    rectPlay = imgPlay.get_rect(center=(480, 300))

    imgOpt = pygame.image.load(btnOptions[1])
    rectOpt = imgPlay.get_rect(center=(480, 400))

    imgExit= pygame.image.load(btnExit[1])
    rectExit = imgPlay.get_rect(center=(480, 500))

    while not finito:
        # cattura posizione mouse
        mouse = pygame.mouse.get_pos()

        # Disegno sullo schermo
        screen.blit(sfondoMenu, (0, 0))
        screen.blit(imgPlay, rectPlay)
        screen.blit(imgOpt, rectOpt)
        screen.blit(imgExit, rectExit)

        if rectPlay.collidepoint(mouse):
            gifPlayer(screen, btnPlay, rectPlay, 100)
            if click:
                musicaMenu.stop()
                gameover = False
                while not gameover:
                    if game(velocitaMAX, musica) == 'exit':
                        finito = True
                    gameover = True

        elif rectOpt.collidepoint(mouse):
            gifPlayer(screen, btnOptions, rectOpt, 100)
            if click:
                velocitaMAX, musica = options()

        elif rectExit.collidepoint(mouse):
            gifPlayer(screen,btnExit, rectExit, 100)
            if click:
                finito = True

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    musicaMenu.stop()
    pygame.quit()
    sys.exit()
