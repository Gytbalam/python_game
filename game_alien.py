import sys
 
import pygame

from settings import Settings  #import settings from settings class

from ship import Ship

class AlienInvasion:
    """class to manage game and behaviour"""

    def __init__(self):
        """Initialize game and resources"""
        pygame.init()
        self.settings = Settings()

        #full screen code 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        self.screen = pygame.display.set_mode(
              (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)  #import ship and and make and instance after the creation of the screen

        
        

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
        

    def _check_events(self):
            """Start the main loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)  
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                                                  
                          
                      #    self.ship.rect.x += 1      #move the ship to the right


    def  _check_keydown_events(self, event):
         """Key press down"""
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
         elif event.key == pygame.K_q:      #press k key to quit the game
            sys.exit()


    def  _check_keyup_events(self, event):
         """Key press down"""
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
            #color of the screen for each loop   
        self.screen.fill(self.settings.bg_color)   #fill the screen with colors
        self.ship.blitme()    #draw the ship on the screen

        pygame.display.flip()



if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
