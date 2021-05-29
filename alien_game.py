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

        print(str(fps))
        game_functions.check_events(ship)
        
        ship.update()
        
        game_functions.update_screen(configs, screen, ship)




run_game()
