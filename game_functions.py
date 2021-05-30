import sys
import pygame
from bullet import Bullet


def key_event(configs, screen, event, ship, bullets):
    
    keyboard_buttons = {
            pygame.K_SPACE: shot_fire,
            pygame.K_RIGHT: move_ship,
            pygame.K_LEFT: move_ship, 
    }
    
    # fire event if that exist
    if event.key in keyboard_buttons.keys():
        keyboard_buttons[event.key](configs, screen, event, ship, bullets)
   

def shot_fire(configs, screen, event, ship, bullets):
    if event.type == pygame.KEYDOWN: 
        new_bullet = Bullet(configs, screen, ship)
        bullets.add(new_bullet)
    
    

def move_ship(configs, screen, event, ship, bullets):
    
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
        
        
        
def check_events(configs, screen, ship, bullets):
    """ Listen events """
    for event in pygame.event.get():
         
        # Top bar exit button
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYBOARD and MOUSE shot event
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key_event(configs, screen, event, ship, bullets)
            

def update_screen(game_configs, screen, ship, bullets):
    """ Update sprites in the new screen """
    
    # Dawing
    screen.fill(game_configs.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()

    # Refresh Screen
    pygame.display.flip()    
    
