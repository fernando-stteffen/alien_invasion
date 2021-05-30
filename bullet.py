import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, configs, screen, ship): 
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, configs.bullet_width,
          configs.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = configs.bullet_color
        self.speed = configs.bullet_speed
        
    def update(self):
        
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
