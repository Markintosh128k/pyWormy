from entities import *
from control import *

pygame.init()

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Larghezza e altezza finestera
WIN_WIDTH = 1000
WIN_HEIGHT = 1000

# Grandezza celle
CELL_SIZE = 20


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

# Procedura main
def main(FPS_LOCK, musica):
    # Velocita' del serpente (in frame per secondo)
    FPS = 10
    fps = pygame.time.Clock()

    # Oggetti
    verme = Verme(screen, CELL_SIZE)
    mele = Mela(screen, CELL_SIZE)

    # Inizializzazione varibili utili
    gameover = False
    assetSfondo = resource_path("Img/background1.png")
    sfondo = pygame.image.load(assetSfondo)
    punteggio = 0

    mele.spawn()
    musica.play(-1)
    while not gameover:
        screen.blit(sfondo, (0, 0))
        # disegnaGriglia(screen)
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

    azione = startMenu(screen)
    print(azione)
    if azione == 'play':
        finito = False
        while not finito:
            finito = main(FPS_LOCK, musica)
    elif azione == 'opzioni':
        pass
    elif azione == 'creatori':
        pass
    elif azione == 'esci':
        pass

    sys.exit()
