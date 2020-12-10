import pygame
import sys
import os

defaultFont = pygame.font.get_default_font()

class Menu:
    def __init__(self, surface, ButtonsList, x, y):
        self.surface = surface      # Superfice dove disegnare
        self.buttonsList = []       # Lista di oggetti Button
        self.x = x                  # Posizione iniziale x del pulsante
        self.y = y                  # Posizione iniziale y del pulsante

        # Carica tutti i pulsanti nella lista
        for button in ButtonsList:
            self.buttonsList.append(button)

    def start(self, background, time=500, text='', font=defaultFont, tposition=(0, 0), color=(0, 0, 0)):
        click = False   # Controlla se è stato pemuto un tasto del mouse
        done = False    # Controlla se il ciclo è finito
        action = None   # Azione del pulsatne
        while not done:
            mouse = pygame.mouse.get_pos()  # mouse assume il valore della x & y del mouse
            # Disegno dei pulsanti
            self.surface.blit(background, (0, 0))
            for button in self.buttonsList:
                self.surface.blit(button.getFirstFrame(), button.getArea())

            # Disegno di un eventuale testo
            if text:
                self.drawText(text, tposition, font, color)

            # Controllo se il mouse passa sopra il pulsante
            for button in self.buttonsList:
                if button.getArea().collidepoint(mouse):
                    button.animatedButton(self.surface, button.getArea(), time)
                    if click:
                        action = button.getAction()
                        done = True

            # Controllo eventi
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

        return action

    # Disegna un testo sullo schermo
    def drawText(self, text, position, font, color):
        text = font.render(str(text), True, color)
        self.surface.blit(text, position)

class Button:
    def __init__(self, pathImags=None, action='', x=0, y=0):
        self.imgButton = []     # Lista di tutte le immagini necessarie per disegnare il pulsante
        self.action = action    # Azione del pulsante
        self.x = x              # Posizione x del pulsante
        self.y = y              # Posizione y del pulsante

        # Carica tutte le immagini
        for path in pathImags:
            img = pygame.image.load(path)
            self.imgButton.append(img)

        # Area della prima immaginie
        self.area = self.imgButton[0].get_rect(center=(self.x, self.y))# Area del pulsante

    # Crea un animazione del bottone
    def animatedButton(self, screen, position, wait=500):
        for img in self.imgButton:
            screen.blit(img, position)
            pygame.time.wait(wait)
            pygame.display.update()

    # Imposta le cordinate d'inizio del pulsante
    def setArea(self, x, y):
        self.area.center = (x, y)

    # Restituisce le cordinate d'inizio del pulsante
    def getArea(self):
        return self.area

    # Restituisce la prima immagine del pulsante
    def getFirstFrame(self):
        return self.imgButton[0]

    # Restituisce l'azione del bottone
    def getAction(self):
        return self.action


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)