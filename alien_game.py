import pygame
import game_functions 

from pygame.sprite import Group
from config import Configs
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



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
    
    stats = GameStats(configs)
    scoreboard = Scoreboard(configs, screen, stats)
    
    # Play Button
    
    play_button = Button(configs, screen, "Play")
    
    while True:
        
        #Listen
        game_functions.check_events(ship, bullets, play_button, stats, aliens)
        
        # Upadating Elements
        if stats.game_active:
            ship.update()
            game_functions.update_bullets(bullets,aliens, ship.rect.height)
            game_functions.update_aliens(aliens, ship, bullets, stats)
        
        game_functions.update_screen(
            ship, bullets, aliens, play_button, stats, scoreboard
        )




run_game()
