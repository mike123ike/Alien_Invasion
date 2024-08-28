import pygame # type: ignore

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get rect
        self.image = pygame.image.load('Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for ship's x position
        self.x = float(self.rect.x)

        #movement flags
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        """update position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)