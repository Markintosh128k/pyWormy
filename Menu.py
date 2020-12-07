import pygame


class Menu:

    # Costruttore
    def __init__(self, screen, sfondo, imgList, musica=None):
        self.screen = screen
        self.sfondo = sfondo
        self.imgList = []
        self.musica = musica
        for img in imgList:
            self.imgList.append(img)

    def start(self):
        mouseX, mouseY = pygame.
