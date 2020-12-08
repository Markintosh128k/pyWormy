from PyGimager import *
import pygame

class Bottoni:
    # Costruttore
    def __init__(self, screen, x, y, btnPathList, savePathList, sfondo):
        self.screen = screen    # schermo dove disegnare
        self.sfondo = sfondo    # immagine di sfondo
        self.bottonePremuto = None

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


    def start(self, flag=0, text='', font='', x=0, y=0, color=(255,255,255) ):
        finito = False
        click = False

        while not finito:
            self.screen.blit(self.sfondo, (0, 0))
            mouse = pygame.mouse.get_pos()
            
            if flag != 0:
                self.stampaText(text, font, x, y, color)
            
            # disegno i bottoni
            for i in range(len(self.firstFrame)):
                self.screen.blit(self.firstFrame[i], self.rectList[i])

            # controllo se il mouse passa sorpa l'area del bottone
            for i in range(len(self.gifList)):
                if self.rectList[i].collidepoint(mouse):
                    self.gifList[i].gifPlayer(self.screen, self.rectList[i], 100)
                    if click:
                        self.bottonePremuto = i
                        finito = True

            if not finito:
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
                        click = True


            pygame.display.update()

    def getBottonePremuto(self):
        return self.bottonePremuto

    
    def stampaText(self, text, font, x, y, color=(255,255,255)):
        text = font.render(str(text), True, color)
        self.screen.blit(text, [x, y])