from Entities import *
from Control import *
from PyGimager import *

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


# Procedura main
def main(FPS_LOCK, musica):
    # Velocita' del serpente (in frame per secondo)
    FPS = 10
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
        screen.blit(bg, (0, 0))
        #disegnaGriglia(screen)
        score(screen, punteggio)
        mele.disegna()
        verme.disegna()

        # seleziona i comandi
        gameover = verme.comandi()

        if verme.mangiaMele(mele.getX(), mele.getY()):
            mele.spawn()
            punteggio += 1
            if FPS <= FPS_LOCK:
                FPS += 1

        pygame.display.update()
        fps.tick(FPS)

    musica.stop()
    #return messaggioGameOver(screen, punteggio)

if __name__ == "__main__":

    # Creazione della finestra (screen)
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("pyWormy")


    # FPS, musica default
    FPS_LOCK, musica = difficile_init()

    startMenu(screen)
    finito = False
    while not finito:
        finito = main(FPS_LOCK, musica)
    sys.exit()
