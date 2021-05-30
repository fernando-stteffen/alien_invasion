import pygame
import game_functions 

from pygame.sprite import Group
from config import Configs
from ship import Ship



def run_game():
        
    configs = Configs()
    
    
    pygame.init()
    pygame.display.set_caption(configs.get_game_name())
    screen = pygame.display.set_mode(configs.get_display_size())
        
    ship = Ship(configs, screen)
    bullets = Group()
    
    game_functions.set_globals(configs, screen)
    
    while True:
        
        game_functions.check_events(ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(ship, bullets)




run_game()
