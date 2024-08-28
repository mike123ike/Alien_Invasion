import pygame # type: ignore

from pygame.sprite import Sprite # type: ignore

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_game):
        """initialize alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load image and set rect
        self.image = pygame.image.load('Alien_Invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return -1 if alien is at right edge and 1 if left edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return -1
        elif self.rect.left <= screen_rect.left:
            return 1
        
    def update(self):
        """move alien right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x