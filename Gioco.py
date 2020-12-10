from Entities import *
from PyGimager import *

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

# PATH PULSANTI
path_btnPlay = ['Img/Buttons/Play/PlayButton0.png', 'Img/Buttons/Play/PlayButton1.png']
path_btnOptions = ['Img/Buttons/Options/OptionsButton0.png', 'Img/Buttons/Options/OptionsButton1.png']
path_btnEasy = ['Img/Buttons/Easy/EasyButton0.png', 'Img/Buttons/Easy/EasyButton1.png']
path_btnHard = ['Img/Buttons/Hard/HardButton0.png', 'Img/Buttons/Hard/HardButton1.png']
path_btnExit = ['Img/Buttons/Exit/ExitButton0.png', 'Img/Buttons/Exit/ExitButton1.png']
path_btnBackMenu = ['Img/Buttons/BackToMenu/BacktoMenuButton0.png', 'Img/Buttons/BackToMenu/BacktoMenuButton0.png']

for btn in path_btnPlay:
    resource_path(btn)

for btn in path_btnOptions:
    resource_path(btn)

for btn in path_btnEasy:
    resource_path(btn)

for btn in path_btnHard:
    resource_path(btn)

for btn in path_btnExit:
    resource_path(btn)

for btn in path_btnBackMenu:
    resource_path(btn)


# SFONDI
sfondo_menu = pygame.image.load(resource_path('Img/startMenu.png'))
sfondo_gameOver = pygame.image.load(resource_path("Img/GameOver.png"))
sfondo_game = pygame.image.load(resource_path('Img/background.png'))

# MUSICA
musica_menu = pygame.mixer.Sound(resource_path('Sounds/musica.wav'))
musica_hardMode = pygame.mixer.Sound(resource_path('Sounds/difficileSottofondo.wav'))
musica_easyMode = pygame.mixer.Sound(resource_path('Sounds/facileSottofondo.wav'))
musica_gameOver =  pygame.mixer.Sound(resource_path("Sounds/lose.wav"))

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

# Creazione del menu main
def mainMenu(screen):
    action = ''     # azione del pulsante premuto

    # CREAZIONE OGGETTI PULSATNI
    btnPlay = Button(path_btnPlay, 'play', (WIN_WIDTH/2), (WIN_HEIGHT/2) - 150)
    btnOptions = Button(path_btnOptions, 'options', (WIN_WIDTH / 2), (WIN_HEIGHT / 2) - 50)
    btnExit = Button(path_btnExit, 'exit', (WIN_WIDTH / 2), (WIN_HEIGHT / 2) + 50)

    buttonsList = [btnPlay, btnOptions, btnExit]

    # CREAZIONE OGGETTO MAIN MENU
    mainM = Menu(screen, buttonsList, 375, 120)

    # Variabili di default
    done = False
    velocitaMAX = 15
    musica = musica_easyMode

    while not done:
        action = mainM.start(sfondo_menu, 100)
        if action == 'play':
            game_action = game(velocitaMAX, musica)
            if game_action == 'exit':
                done = True

        elif action == 'options':
            velocitaMAX, musica = options()
        elif action == 'exit':
            done = True

# Creazione menu options
def options():
    action = ''  # azione del pulsante premuto
    # CREAZIONE OGGETTI PULSATNI
    btnEasy= Button(path_btnEasy, 'easy', (WIN_WIDTH / 2), (WIN_HEIGHT / 2) - 150)
    btnHard = Button(path_btnHard, 'hard', (WIN_WIDTH / 2), (WIN_HEIGHT / 2))

    buttonsList = [btnEasy, btnHard]

    # CREAZIONE OGGETTO MAIN MENU
    optionMenu = Menu(screen, buttonsList, 375, 120)

    action = optionMenu.start(sfondo_menu, 100)

    if action == 'easy':
        velocitaMAX = 15
        musica = musica_easyMode
    elif action == 'hard':
        velocitaMAX = 40
        musica = musica_hardMode


    return velocitaMAX, musica

# Creazione menu gameover
def messaggioGameOver(screen, punteggio):
    # CREAZIONE OGGETTI PULSATNI
    btnBack = Button(path_btnBackMenu, 'back', (WIN_WIDTH / 2), (WIN_HEIGHT / 2) + 100)
    btnExit = Button(path_btnExit, 'exit', (WIN_WIDTH / 2), (WIN_HEIGHT / 2) + 200)
    buttonsList = [btnBack, btnExit]

    # CREAZIONE OGGETTO MAIN MENU
    gameoverMenu = Menu(screen, buttonsList, 375, 120)

    return gameoverMenu.start(sfondo_gameOver, 100, str(punteggio), FONT_END, (540, 414), YELLOW)

# gioco
def game(velocitaMAX, musica):
    # Velocita' del serpente (in frame per secondo)
    velocita = 10
    fps = pygame.time.Clock()

    # CREAZIONE OGGETTI VERME E MELA
    verme = Verme(screen, CELL_SIZE, START_WIDHT, START_HEIGHT, END_WIDTH, END_HEIGHT)
    mela = Mela(screen, CELL_SIZE, START_WIDHT, START_HEIGHT, END_WIDTH, END_HEIGHT)

    # Inizializzazione varibili utili
    gameover = False
    punteggio = 0

    mela.spawn()
    musica.play(-1)
    while not gameover:
        # Disegna il verme e la mela
        #disegnaGriglia(screen)
        screen.blit(sfondo_game, (0, 0))
        mela.disegna()
        verme.disegna()
        # Mostra il punteggio attuale
        score(screen, FONT_SCORE, punteggio, 290, 831, PINK)

        # Muove il serpente, se va fuori campo o si mangia da solo si perde
        gameover = verme.comandi()

        # Controllo se il verme mangia la mela
        if not gameover:
            if verme.mangiaMele(mela.getX(), mela.getY()):
                mela.spawn()
                punteggio += 1
                if velocita <= velocitaMAX:
                    velocita += 1

        pygame.display.update()
        fps.tick(velocita)

    musica.stop()
    return messaggioGameOver(screen, punteggio)




if __name__ == "__main__":

    # CREAZIONE DELLA FINESTRA DI GIOCO
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("pyWormy")

    mainMenu(screen)




