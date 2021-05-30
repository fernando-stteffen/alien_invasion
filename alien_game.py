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

    while True:

        game_functions.check_events(configs, screen, ship, bullets)
        
        ship.update()
        bullets.update()
        
        game_functions.update_screen(configs, screen, ship, bullets)




run_game()
