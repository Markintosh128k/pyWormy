from PIL import Image
import sys
import os
import pygame

pygame.init()


 # Default parameters for GifPlater
def_filling = (255, 255, 255)
def_position = (0, 0)
def_scaling = (100, 100)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class PyGimager:
    def __init__(self, gif):
        # Loading the desired gif image
        self.gif = Image.open(gif)

        # Variable where all the frames will be stored
        self.frames = []

        self.assetFrames_url = []

    # This method divides all the frames of the gif in a .png file (in a desired folder)
    def deconstructGif(self, mainName='decImage', savePath='LOCAL'):
        path = savePath + "/" + mainName
        self.assetFrames_url.append(resource_path(path))
        f = open("paths.txt", 'w')
        f.write("[")
        local = True

        if savePath != 'LOCAL':
            try:
                os.makedirs(savePath)
            except OSError as error:
                print("Path creation failed: {}".format(error))
            local = False

        for i in range(self.gif.n_frames):
            self.gif.seek(i)
            if not local:
                self.gif.save(savePath+mainName+'{}.png'.format(i), 'PNG')
                f.write("('{}{}','{}'),".format(savePath+mainName, i, savePath))
                
            else:
                self.gif.save(mainName+'{}.png'.format(i))
                f.write("('{}{}','{}'),".format(mainName, i, "'.'"))
        f.write("]")
        
            
    # loads all the frames in a bidimensional array
    def gifLoader(self, loadPath="/"):
        frame = ''
        if loadPath == "/":
            for image in os.listdir():
                if image.endswith(".png"):
                    frame = pygame.image.load(image)
                    self.frames.append(frame) 
        else:
            for image in os.listdir(loadPath):
                if image.endswith(".png"):
                    frame = pygame.image.load(loadPath+image)
                    self.frames.append(frame) 
       

    def gifPlayer(self, screen, position=def_position, wait=500):
        for frame in self.frames:
            AnimatedSprite = frame
            screen.blit(AnimatedSprite, position)
            pygame.time.wait(wait)
            pygame.display.update()

    def getFirstFrame(self):
        return self.frames[-1]