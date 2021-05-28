import pygame
import game_functions 

from config import Configs
from ship import Ship

def run_game():
    
    pygame.init()
    
    game_configs = Configs()
    screen = pygame.display.set_mode(
        (game_configs.screen_width, game_configs.screen_height)
    )
    pygame.display.set_caption(game_configs.get_game_name())
    
    ship = Ship(screen)
    
    while True:
        
        game_functions.check_events()
        game_functions.update_screen(game_configs, screen, ship)




run_game()
