import pygame
import game_functions 

from config import Configs
from ship import Ship

def run_game():
    
    pygame.init()
    
    game_config = Configs()
    screen = pygame.display.set_mode(
        (game_config.screen_width, game_config.screen_height)
    )
    pygame.display.set_caption(game_config.get_game_name())
    
    ship = Ship(screen)
    
    while True:
        
        game_functions.check_events()
        
        screen.fill(game_config.background_color)
        ship.blitme()
        pygame.display.flip()
        





run_game()
