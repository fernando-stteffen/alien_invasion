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

def update_aliens(aliens):
    
    check_fleet_edges(aliens)
    aliens.update()
            
        
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


def get_max_alien_x(alien_width):
    """Get numbers of alien fit in a row"""
    
    available_space_x = game_configs.screen_width - (2 * alien_width)
    max_aliens_x = int(available_space_x / (2 * alien_width))
    
    return max_aliens_x
    
def get_max_alien_y(alien_height, ship_height):
    """Determine the numbers of aliens fit on Y"""
    
    available_space_y = (
        game_configs.screen_height - (3 * alien_height) - ship_height
    )
    max_aliens_y = int(available_space_y / (2 * alien_height))
    return max_aliens_y 
    
    

def create_alien(aliens, alien_number, alien_row):
    alien = Alien(game_configs, game_screen)
    
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * alien_row
    
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    
    aliens.add(alien)


def create_fleet(aliens, ship_height):
    """Create Aliens Line"""
    
    # Create an alien and find the number of aliens in a row
    # (Space between each alien is equal to one alien width.)
    
    alien = Alien(game_configs, game_screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    max_aliens_x = get_max_alien_x(alien_width)
    max_aliens_y = get_max_alien_y(alien_height, ship_height)
    
    for alien_row in range(max_aliens_y):
        for alien_number in range(max_aliens_x):
            create_alien(aliens, alien_number, alien_row)
    
    
def check_fleet_edges(aliens):
    """Respond appropriately if any aliens have reached an edge"""
    
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break
            

def change_fleet_direction(aliens):
    """ Drop all fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_configs.aliens_drop_speed
    game_configs.aliens_direction *= -1



    
    
    
    
    
    
