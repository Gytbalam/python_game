import sys

import pygame

class AlienInvasion:
    """class to manage game and behaviour"""

    def __init__(self):
        """Initialize game and resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            """Start the main loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
