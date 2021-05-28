import sys
import pygame
from config import Configs

def run_game():
    
    pygame.init()
    
    game_config = Configs()
    screen = pygame.display.set_mode(
        (game_config.screen_width, game_config.screen_height)
    )
    pygame.display.set_caption(game_config.get_game_name())
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(game_config.background_color)
        pygame.display.flip()
        





run_game()
