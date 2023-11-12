import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):
        """initialize ship and its position"""
        self.screen = ai_game.screen   #assign the screen to attribute of ship
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()   #acess screen rect attribute using get_rect()

        #load ship img

        self.image = pygame.image.load('D:\Archivos\Odin project\python\py_git\irship.png')    #load the img 
        self.rect = self.image.get_rect()   

        #start new ship at the bottom
        self.rect.midbottom = self.screen_rect.midbottom       #give a location to the img

         # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
       """Update ship position based on the movement flag"""
       if self.moving_right and self.rect.right < self.screen_rect.right:
          self.x += self.settings.ship_speed
       if self.moving_left and self.rect.left > 0:
          self.x -= self.settings.ship_speed 
         # Update rect object from self.x.
       self.rect.x = self.x

    def blitme(self):
     """Draw the ship at its current location."""
     self.screen.blit(self.image, self.rect)
