# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame

class SpriteSheet(object):
    
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load spritesheet image:'), filename
            raise SystemExit(message)
            
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
        
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
        
        
    def positions_sheet(self, sheet_width, sheet_height, sheet_columns, 
                        sheet_lines):
        
        """ That return all possible positions of a sprite in a dictionary """
        sheet_offset_x = int(sheet_width / sheet_columns) # 16
        sheet_offset_y = int(sheet_height / sheet_lines)  # 24
        
        
        sprites = {}
        
        current_sheet_line = 0
        current_sheet_column = 0
        current_number_sprite = 0
        
        while current_sheet_line < sheet_lines:
            
            while current_sheet_column < sheet_columns:
                
                offset_x = int(sheet_offset_x * current_sheet_column)
                offset_y = int(sheet_offset_y * current_sheet_line)
                
                current_sprite = (offset_x, 
                                  offset_y, 
                                  sheet_offset_x, 
                                  sheet_offset_y)
                sprites[current_number_sprite] = current_sprite
                
                current_number_sprite += 1
                current_sheet_column += 1
                
            current_sheet_column = 0
            current_sheet_line += 1
        
        
        return sprites
        


