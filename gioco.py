import pygame
import sys
from entities import *
from general import *

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Larghezza e altezza finestera
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Grandezza celle
CELL_SIZE = 20


#Procedura main
def main():
    pygame.init()

    #Velocita' del serpente (in frame per secondo)
    FPS = 10
    frames_per_secondo = pygame.time.Clock()
    
    #Creazione della finestra (screen)
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Wormy")
    startGame(screen)

    #Creazione dell'oggetto verme
    verme = [Verme(screen, 240, 240, 0), Verme(screen, 220, 240, 1), Verme(screen, 200, 240, 2)]
    
    #Inizializzazione della variabile di GameOver
    gameover = False
    
    #Creazione dell'oggetto mele
    mele = Mela(screen, CELL_SIZE)
    
    #Inizializzazione del punteggio
    punteggio = 0


    # Sfondo
    sfondo = pygame.image.load("background.png")

    x = verme[0].getX()
    y = verme[0].getY()
    while not gameover:
        screen.fill(WHITE)
        screen.blit(sfondo, (0, 0))
        mele.disegna()
        #disegnaGriglia(screen)
        verme[0].disegnaTesta()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        verme[0].spostamenti()
        gameover = controlloBordi(verme[0].getX(), verme[0].getY())
        verme[0].mangiaMele(mele.getX(), mele.getY())
       
        mangiato = verme[0].isMangiato()
        if mangiato == True:
            print("UA MEGLIO DI MAGMA")
            mele.spawn()
            punteggio += 1
            FPS += 1

        pygame.display.update()
        frames_per_secondo.tick(FPS)

    fineGioco = messaggioGameOver(screen, punteggio)    
    return fineGioco

if __name__ == "__main__":
    finito = False
    while not finito:
        finito = main()
    sys.exit()
