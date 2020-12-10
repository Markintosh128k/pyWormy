import sys
import os
import pygame

pygame.init()

# Default parameters for GifPlater
def_position = (0, 0)
def_scaling = (100, 100)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def gifPlayer(screen, frameList, position=def_position, wait=500):
    for frame in frameList:
        img = pygame.image.load(frame)
        screen.blit(img, position)
        pygame.time.wait(wait)
        pygame.display.update()
