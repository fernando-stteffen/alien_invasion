import pygame
from pygame.sprite import Sprite
from sprite_sheet import SpriteSheet

class Alien(Sprite):
    
    
    def __init__(self, configs, screen):
        super().__init__()
        
        self.screen = screen
        self.alien_configs = configs
        
        
        # Load Sprite Sheet
        self.sprite_sheet = SpriteSheet('images/enemy-small.bmp')
        sheet_width = 32
        sheet_height = 16
        sheet_columns = 2
        sheet_lines = 1
        
        
        # Options of initial sprite
        self.sprites = self.sprite_sheet.positions_sheet(sheet_width, 
                                                         sheet_height,
                                                         sheet_columns,
                                                         sheet_lines)
       
        sprite_scale = 4
        sprite_size_x = int((sheet_width / sheet_columns) * sprite_scale)
        sprite_size_y = int((sheet_height / sheet_lines) * sprite_scale)
      
        
        # Load Sprite
        sprite = self.sprite_sheet.image_at((self.sprites[1]), (255,0,255))
        
        # Instance Sprite and set its rect attributes.
        
        self.image = pygame.transform.scale(sprite, (sprite_size_x, sprite_size_y))
        self.rect = self.image.get_rect()
                
                
        # top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        
        # Store alien's exact position.
        self.x = float(self.rect.x)

    
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
        
        
    
    
    

