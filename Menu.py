import pygame
from PyGimager import *

class Menu:
    # Costruttore
    def __init__(self, screen, sfondo, buttonList, sound=None):
        self.screen = screen
        self.sfondo = sfondo
        self.buttonList = []
        self.button_rectList = []
        self.sound = sound

    def buttonLoader(self, button):
        self.buttonList.append(button)
        rect = button.get_rect()
        self.button_rectList.append(rect)

    def start(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        for i in  range(len(self.buttonList)):
            if self.button_rectList[i].collidepoint(mouseX, mouseY):


