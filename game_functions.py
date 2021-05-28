import sys
import pygame


def check_events():
    """ Respond to keyboard and mouse events """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def update_screen(game_configs, screen, ship):
    """ Update sprites in the new screen """
    
    # Dawing
    screen.fill(game_configs.background_color)
    ship.blitme()

    # Refresh Screen
    pygame.display.flip()    
    
