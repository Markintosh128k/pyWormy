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


# Procedura main
def main():
    pygame.init()

    # Velocita' del serpente (in frame per secondo)
    FPS = 10
    fps = pygame.time.Clock()

    # Creazione della finestra (screen)
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Wormy")
    startGame(screen)

    # Oggetti
    verme = Verme(screen, CELL_SIZE)
    mele = Mela(screen, CELL_SIZE)


    # Inizializzazione varibili utili
    gameover = False
    sfondo = pygame.image.load("background.png")
    punteggio = 0
    mele.spawn()



    while not gameover:
        screen.fill(WHITE)
        #screen.blit(sfondo, (0, 0))
        disegnaGriglia(screen)
        mele.disegna()
        verme.disegna()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    verme.muoviUp()

                elif event.key == pygame.K_DOWN:
                    verme.muoviDown()
                elif event.key == pygame.K_RIGHT:
                    verme.muoviRight()
                elif event.key == pygame.K_LEFT:
                    verme.muoviLeft()
        verme.muovi()
        verme.popAppend()


        gameover = verme.controlloBordi()
        if not gameover:
            gameover = verme.checkEatItSelf()

        if verme.mangiaMele(mele.getX(), mele.getY()):
            print("MELA MELINDAAA FANTASTICAAA!")
            mele.spawn()
            punteggio += 1
            if FPS <= 30:
                #FPS += 1
                pass

        pygame.display.update()
        fps.tick(FPS)

    return messaggioGameOver(screen, punteggio)

if __name__ == "__main__":
    finito = False
    while not finito:
        finito = main()

    sys.exit()
