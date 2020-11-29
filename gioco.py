import pygame
import sys
from entities import *
from startGame import *

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
    verme = Verme(screen)
    
    #Inizializzazione della variabile di GameOver
    gameover = False
    
    #Creazione dell'oggetto mele
    mele = Mela(screen)
    
    #Inizializzazione del punteggio
    punteggio = 0

    
    #Generazione casuale delle mele sulla mappa
    mele.setX(mele.spawnX())
    mele.setY(mele.spawnY())

    x = verme.getX()
    y = verme.getY()
    while not gameover:
        screen.fill(WHITE)
        mele.disegna()
        #disegnaGriglia(screen) 
        verme.disegna()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x, y = verme.spostamenti()
        verme.muovi(x, y)
        gameover = controlloBordi(verme.getX(), verme.getY()) 
        verme.mangiaMele(mele.getX(), mele.getY())
       
        mangiato = verme.isMangiato()
        if mangiato == True:
            print("UA MEGLIO DI MAGMA")
            mele.setX(mele.spawnX())
            mele.setY(mele.spawnY())
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
