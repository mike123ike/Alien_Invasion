import pygame # type: ignore

from pygame.sprite import Sprite # type: ignore

class Bullet(Sprite):
    """manages bullets"""

    def __init__(self, ai_game):
        """create a bullet at the ship's location"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet at (0,0) and move to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #store position as a decimal
        self.y = float(self.rect.y)
    
    def update(self):
        """move the bullet up the screen"""
        #update decimal position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)