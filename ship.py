import pygame
from sprite_sheet import SpriteSheet

class Ship():
    
    
    def __init__(self, screen):
        
        self.screen = screen
        
        
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
        sprite = self.sprite_sheet.image_at((self.sprites[2]), (255,0,255))
        self.image = pygame.transform.scale(sprite, (sprite_size_x, sprite_size_y))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
                
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 5
        
        # Ship flags
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        """ Update Ship """
        
        if self.moving_right:
            self.rect.centerx += 1
        
        if self.moving_left:
            self.rect.centerx -= 1
    
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
        
        
    
    
    
