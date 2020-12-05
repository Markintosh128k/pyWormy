from entities import *
from control import *

pygame.init()

# Colori utili
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Larghezza e altezza finestera
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Grandezza celle
CELL_SIZE = 20

# Velocita' del serpente (in frame per secondo)
FPS = 10
fps = pygame.time.Clock()

def menu():
    start(screen)

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

def comandi (verme):
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

    return gameover

# Procedura main
def main(FPS_LOCK, musica):

    global FPS
    global fps

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
        gameover = comandi(verme)

        if verme.mangiaMele(mele.getX(), mele.getY()):
            mele.spawn()
            punteggio += 1
            if FPS <= FPS_LOCK:
                FPS += 1

        pygame.display.update()
        fps.tick(FPS)

    musica.stop()
    return messaggioGameOver(screen, punteggio)

if __name__ == "__main__":

    # Creazione della finestra (screen)
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("pyWormy")

    FPS_LOCK = None
    musica = None
    
    if menu() == 1:
        FPS_LOCK, musica = facile_init()
    elif menu() == 2:
        FPS_LOCK, musica = difficile_init()

    finito = False
    while not finito:
        finito = main(FPS_LOCK, musica)

    sys.exit()
