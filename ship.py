import pygame
from sprite_sheet import SpriteSheet
from pygame.sprite import Sprite

class Ship(Sprite):
    
    
    def __init__(self, ship_configs, screen):
        super().__init__()
        
        self.screen = screen
        self.ship_configs = ship_configs
        
        
        # Load Sprite Sheet
        self.sprite_sheet = SpriteSheet('images/ship.bmp')
        sheet_width = 80
        sheet_height = 48
        sheet_columns = 5
        sheet_lines = 2
        
        
        # Options of initial sprite
        self.sprites = self.sprite_sheet.positions_sheet(sheet_width, 
                                                         sheet_height,
                                                         sheet_columns,
                                                         sheet_lines)
       
        sprite_scale = 4
        sprite_size_x = int((sheet_width / sheet_columns) * sprite_scale)
        sprite_size_y = int((sheet_height / sheet_lines) * sprite_scale)
      
        
        # Load Sprite
        sprite = self.sprite_sheet.image_at((self.sprites[7]), (255,0,255))
        self.image = pygame.transform.scale(sprite, (sprite_size_x, sprite_size_y))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
                
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 5
        
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Ship flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ Update Ship """
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_configs.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_configs.ship_speed
            
        self.rect.centerx = self.center
    
    def center_ship(self):
        """Center ship on the screen """
        
        self.center = self.screen_rect.centerx
        
        
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
        
        
    
    
    
