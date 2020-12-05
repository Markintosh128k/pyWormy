import pygame
import os
import sys

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (217, 210, 57)

# Larghezza e altezza finestera
WIN_WIDTH = 1000
WIN_HEIGHT = 1000

# Grandezza celle
CELL_SIZE = 20

# Dichiarazione Font
assetFONT_OBJ_url = resource_path('SF_Pixelate.ttf')
FONT_OBJ = pygame.font.Font(assetFONT_OBJ_url, 25)
FONT_OBJ1 = pygame.font.Font(assetFONT_OBJ_url, 15)

# Musica
assetSound_url = resource_path("Sounds/musica.wav")
sound = pygame.mixer.Sound(assetSound_url)

#Procedurea per stampre a schermo una scritta
def disegnaTesto(text, font, color, screen, x, y):
    text_obj = font.reder(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)

def score(screen, score):
    text = FONT_OBJ1.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(text, [350, 10])

def startMenu(screen):
    # caricamento immagine sfondo menu
    assetMenu_url = resource_path("Img/menu.png")
    menu = pygame.image.load(assetMenu_url)
    menu = pygame.transform.scale(menu, (1000, 1000))


    # avvio musica
    sound.play(-1)

    # azione fatta
    azione = 'nessuna'

    # bottoni
    btnPlay = pygame.Rect(350, 300, 300, 50)
    btnOpzioni = pygame.Rect(350, 400, 300, 50)
    btnCreatori = pygame.Rect(350, 500, 300, 50)
    btnEsci = pygame.Rect(350, 600, 300, 50)



    # controllo azioni del menu
    finito = False
    click = False
    while not finito:
        screen.blit(menu, (0, 0))

        # prendi posizioni mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # disegna pulsanti
        pygame.draw.rect(screen, YELLOW, btnPlay)
        pygame.draw.rect(screen, YELLOW, btnOpzioni)
        pygame.draw.rect(screen, YELLOW, btnCreatori)
        pygame.draw.rect(screen, YELLOW, btnEsci)

        if btnPlay.collidepoint((mouseX, mouseY)):
            if click:
                azione = 'play'
                finito = True
        if btnOpzioni.collidepoint((mouseX,mouseY)):
            if click:
                azione = 'opzioni'
                finito = True
        if btnCreatori.collidepoint((mouseX,mouseY)):
            if click:
                azione = 'creatori'
                finito = True
        if btnEsci.collidepoint((mouseX, mouseY)):
            if click:
                azione = 'esci'
                finito = True

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





#Funzione per gestire i tasti premuti nel menu
'''
def tastiEscSpace():

    finito = False  #finito gestisce il ciclo while riga 44
    fineGame = False #fineGame = True il gico finisce, fineGame = Fale il gioco continua ancora
    while not finito:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    finito = True
                    fineGame = False
                elif event.key == pygame.K_ESCAPE:
                    fineGame = True
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                fineGame = True
                pygame.quit()
                sys.exit()
        pygame.display.update()

    return fineGame'''


# Procedura per diegnare la griglia
def disegnaGriglia(screen):
    for x in range(0, WIN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WIN_HEIGHT), 1)

    for y in range(0, WIN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIN_WIDTH, y), 1)


# Funzione per stampare il messaggio di gameover con relativo punteggio
'''def messaggioGameOver(screen, score=0):
    mystr = str(score)
    assetGameOver_url = resource_path("Img/GameOver.png")
    gameOver = pygame.image.load(assetGameOver_url)

    screen.blit(gameOver, (0, 0))
    text = FONT_OBJ.render(str(score), True, YELLOW)
    screen.blit(text, [240, 373])

    return tastiEscSpace()'''

