import sys
import pygame
from bullet import Bullet
from alien import Alien


game_configs = ()
game_screen = ()

def set_globals(configs, screen):
    global game_configs
    global game_screen
    game_configs = configs
    game_screen = screen
            

        
def update_screen(ship, bullets, aliens):
    """ Update sprites in the new screen """
    
    # Dawing
    game_screen.fill(game_configs.background_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    
    aliens.draw(game_screen)

    # Refresh Screen
    pygame.display.flip()  

    

def update_bullets(bullets):
    """Update position of bullets and ger rid of old bullets."""
    
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
            
        
def check_events(ship, bullets):
    """ Listen events """
    for event in pygame.event.get():
         
        # Top bar exit button
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYBOARD and MOUSE shot event
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key_event(event, ship, bullets)
            
            

def key_event(event, ship, bullets):
    keyboard_buttons = {
            pygame.K_SPACE: shot_fire,
            pygame.K_RIGHT: move_ship,
            pygame.K_LEFT: move_ship,
            pygame.K_q: close_game, 
    }
    
    # fire event if that exist
    if event.key in keyboard_buttons.keys():
        keyboard_buttons[event.key](event, ship, bullets)


def close_game(*variables): 
    sys.exit()
    
    
def shot_fire(event, ship, bullets):
    if event.type == pygame.KEYDOWN and len(bullets) < game_configs.max_bullets: 
        new_bullet = Bullet(game_configs, game_screen, ship)
        bullets.add(new_bullet)
    
    

def move_ship(event, ship, bullets):
    
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

def create_fleet(aliens):
    """Create Aliens Line"""
    
    # Create an alien and find the number of aliens in a row
    # (Space between each alien is equal to one alien width.)
    
    alien = Alien(game_configs, game_screen)
    alien_width = alien.rect.width
    available_space_x = game_configs.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x / (2 * alien_width)
    
    for alien_number in range(int(number_aliens_x)):
        alien = Alien(game_configs, game_screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
    
    
    
    
    
    
    
