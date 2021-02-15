import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Application():
    def __init__(self):
        self.win = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Hi")
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


win = Application()
win.run()