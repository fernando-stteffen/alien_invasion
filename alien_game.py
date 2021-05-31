import pygame
import game_functions 

from pygame.sprite import Group
from config import Configs
from ship import Ship



def run_game():
    
    #Load Configs    
    configs = Configs()
    
    #Create Window
    pygame.init()
    pygame.display.set_caption(configs.get_game_name())
    screen = pygame.display.set_mode(configs.get_display_size())
        
    
    #Elements    
    ship = Ship(configs, screen)
    bullets = Group()
    aliens = Group()
    
    
    # Set Configs
    game_functions.set_globals(configs, screen)
    game_functions.create_fleet(aliens, ship.rect.height)
    
    while True:
        
        #Listen
        game_functions.check_events(ship, bullets)
        
        # Upadating Elements
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_aliens(aliens)
        game_functions.update_screen(ship, bullets, aliens)




run_game()
