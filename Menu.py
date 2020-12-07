from PyGimager import *

class Bottoni:
    # Costruttore
    def __init__(self, screen, x, y, btnPathList, savePathList, sfondo):
        self.screen = screen    # schermo dove disegnare
        self.sfondo = sfondo    # immagine di sfondo

        self.gifList = []       # lista di tutte le gif
        self.firstFrame = []    # lista di tutti i primi frame della lista
        self.rectList = []      # lista di tutte le aree dei bottoni
        self.x = x  # x dove partire a disegnare
        self.y = y  # y dove partire a disegnare

        for i in range(len(btnPathList)):
            self.gifList.append(PyGimager(btnPathList[i]))
            self.gifList[i].deconstructGif(savePathList[i][0], savePathList[i][1])
            self.gifList[i].gifLoader(savePathList[i][1])
            self.firstFrame.append(self.gifList[i].getFirstFrame())

            rect = self.firstFrame[i].get_rect(center=(x, y))
            y += 100
            self.rectList.append(rect)


    def start(self):
        bottonePremuto = None
        finito = False
        click = True

        while not finito:
            self.screen.blit(self.sfondo, (0, 0))
            mouseX, mouseY = pygame.mouse.get_pos()

            # disegno i bottoni
            for i in range(len(self.firstFrame)):
                self.screen.blit(self.firstFrame[i], self.rectList[i])

            # controllo se il mouse passa sorpa l'area del bottone
            for i in range(len(self.gifList)):
                if self.rectList[i].collidepoint((mouseX, mouseY)):
                    self.gifList[i].gifPlayer(self.screen, self.rectList[i], 100)
                    if click:
                        bottonePremuto = i
                        finito = True

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

        return bottonePremuto
