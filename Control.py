from Menu import *

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


btnMainPathList = ['Img/Buttons/Play.gif', 'Img/Buttons/Options.gif', 'Img/Buttons/Credits.gif', 'Img/Buttons/Exit.gif']
saveMainPathList = [('PlayButton', 'Img/Buttons/Play/'), ('OptionsButton', 'Img/Buttons/Options/'), ('CreditsButton', 'Img/Buttons/Credits/'), ('ExitButton', 'Img/Buttons/Exit/')]

btnOptionsPathList = ['Img/Buttons/Easy.gif', 'Img/Buttons/Hard.gif']
saveOptionsPathList = [('EasyButton', 'Img/Buttons/Easy/'), ('HardButton', 'Img/Buttons/Hard/')]


def score(screen, score):
    text = FONT_OBJ1.render(str(score), True, PINK)
    screen.blit(text, [290, 831])

def startMenu(screen):
    # Setta di default la modalità facile
    FPS_LOCK, musica = facile_init()

    # caricamento immagine sfondo menù
    assetMenu_url = resource_path("Img/startMenu.png")
    bgMenu = pygame.image.load(assetMenu_url)

    # Avvio musica
    sound.play(-1)

    # Caricamento immagini bottoni
    mainMenu = Bottoni(screen, 475, 300, btnMainPathList, saveMainPathList, bgMenu)
    bottonePremuto = mainMenu.start()

    finito = False
    # MAIN MENU
    while not finito:
        if bottonePremuto == 0:     # PLAY
            finito = True

        elif bottonePremuto == 1:   # OPTIONS
            optionMenu = Bottoni(screen, 475, 300, btnOptionsPathList, saveOptionsPathList, bgMenu)
            bottonePremuto = optionMenu.start()

            # scelta modalita: easy/hard
            if bottonePremuto == 0:
                FPS_LOCK, musica = facile_init()

            elif bottonePremuto == 1:
                FPS_LOCK, musica = difficile_init()

            bottonePremuto = mainMenu = Bottoni(screen, 475, 300, btnMainPathList, saveMainPathList, bgMenu)


        elif bottonePremuto == 2:   # CREDITS
            
            bottonePremuto = mainMenu = Bottoni(screen, 475, 300, btnMainPathList, saveMainPathList, bgMenu)

        else:                       # EXIT
            finito = False
            pygame.quit()
            sys.exit()

    sound.stop()

    return FPS_LOCK, musica

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

def difficile_init():
    assetSound_url = resource_path("Sounds/difficileSottofondo.wav")
    musica = pygame.mixer.Sound(assetSound_url)
    FPS_LOCK = 30

    return FPS_LOCK, musica

def facile_init():
    assetSound_url = resource_path("Sounds/facileSottofondo.wav")
    musica = pygame.mixer.Sound(assetSound_url)
    FPS_LOCK = 10

    return FPS_LOCK, musica