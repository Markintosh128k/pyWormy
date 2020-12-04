import pygame
import os
import sys

pygame.init()

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Larghezza e altezza finestera
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Grandezza celle
CELL_SIZE = 20

# Dichiarazione Font
FONT_OBJ = pygame.font.Font('SF_Pixelate.ttf', 25)

# Musica
sound = pygame.mixer.Sound("Sounds/musica.wav")

#Procedurea per stampre a schermo una scritta
def messaggio(screen, listaDiMessaggi):
    screen.fill(BLACK)
    text = []
    text_rect = []
    i = 0
    j = -100
    for testo in listaDiMessaggi:
        text.append(FONT_OBJ.render(listaDiMessaggi[i], True, WHITE))
        text_rect.append(text[i].get_rect())
        text_rect[i].center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 2) + j)
        i += 1
        j += 40

    i = 0
    for testo in listaDiMessaggi:
        screen.blit(text[i], text_rect[i])
        i += 1

def start():
    sound.play(-1)
    tastimenu()
    pygame.mixer.Sound.stop(sound)


#Funzione per gestire i tasti premuti nel menu
def tastimenu():

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
    return fineGame

#Procedura per diegnare la griglia
def disegnaGriglia(screen):
    for x in range(0, WIN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WIN_HEIGHT), 1)

    for y in range(0, WIN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIN_WIDTH, y), 1)


# Funzione per stampare il messaggio di gameover con relativo punteggio
def messaggioGameOver(screen, score=0):
    mystr = str(score)
    messaggio(screen, ["GAME OVER", "PUNTEGGIO: ", mystr, "PREMI SPAZIO PER RIGIOCARE", "PREMI ESC PER USCIRE"])
    fine = tastimenu()

    return fine #fine = True il gico finisce, fine = Fale il gioco continua ancora

