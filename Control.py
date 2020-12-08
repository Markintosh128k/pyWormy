from Bottoni import *

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


def score(screen, score):
    text = FONT_OBJ1.render(str(score), True, PINK)
    screen.blit(text, [290, 831])


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
