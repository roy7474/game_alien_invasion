import sys
import pygame

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def _init(self):
        '''initialize the game, and create game resources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        ''' Start the main loop for the game'''