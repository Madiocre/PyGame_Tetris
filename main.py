#!/usr/bin/env python3
""" Self Playing Teteris using Pygame """

from settings import *


class Game:
    def __init__(self):
        """ """
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            
if __name__ == '__main__':
    main = Game()
