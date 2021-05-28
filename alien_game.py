import pygame
import game_functions 

from config import Configs
from ship import Ship

def run_game():
        
    configs = Configs()
    
    pygame.init()
    pygame.display.set_caption(configs.get_game_name())
    
    screen = pygame.display.set_mode(configs.get_display_size())
    
    ship = Ship(screen)
    
    while True:
        
        game_functions.check_events()
        game_functions.update_screen(game_configs, screen, ship)




run_game()
