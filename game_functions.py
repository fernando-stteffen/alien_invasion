import sys
import pygame


def key_event(event, ship):
    
    keyboard_buttons = {
            pygame.K_RIGHT: move_ship(event, ship),
            pygame.K_LEFT: move_ship(event, ship), 
    }
    
    
    # fire event if that exist
    if event.key in keyboard_buttons.keys():
        keyboard_buttons[event.key]
        

def move_ship(event, ship):
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT: 
            ship.moving_right = True
        else:
            ship.moving_left = True
            
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        else:
            ship.moving_left = False
        
        
        
def check_events(ship):
    """ Listen events """
    for event in pygame.event.get():
         
        # Top bar exit button
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYBOARD and MOUSE shot event
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key_event(event, ship)
            

def update_screen(game_configs, screen, ship):
    """ Update sprites in the new screen """
    
    # Dawing
    screen.fill(game_configs.background_color)
    ship.blitme()

    # Refresh Screen
    pygame.display.flip()    
    
