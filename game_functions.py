import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


game_configs = ()
game_screen = ()

def set_globals(configs, screen):
    global game_configs
    global game_screen
    game_configs = configs
    game_screen = screen
            

        
def update_screen(ship, bullets, aliens, play_button, stats, scoreboard):
    """ Update sprites in the new screen """
    
    # Dawing
    game_screen.fill(game_configs.background_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    
    aliens.draw(game_screen)
    scoreboard.score_draw()
  
    if not stats.game_active:
          game_screen.fill(game_configs.background_color)
          play_button.draw_button()
    
    
    # Refresh Screen
    pygame.display.flip()  

    

def update_bullets(bullets, aliens, ship_height, stats, scoreboard):
    """Update position of bullets and ger rid of old bullets."""
    
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    
    check_bullet_colission(bullets,aliens, ship_height, stats, scoreboard)
    
   
def check_bullet_colission(bullets,aliens, ship_height, stats, scoreboard):
    # Kill event        
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    
    if collisions:
        for aliens in collisions.values():
            stats.score += game_configs.alien_points * len(aliens)
            scoreboard.prepare_score()
            check_high_score(stats, scoreboard)
    
    if len(aliens) == 0:
        # Wining Level
        bullets.empty()
        game_configs.level_up()
        stats.level += 1
        scoreboard.prepare_level()
        create_fleet(aliens, ship_height)

    
    
   
def update_aliens(aliens, ship, bullets, stats, scoreboard):
    
    check_fleet_edges(aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
       ship_hited(ship, aliens, bullets, stats, scoreboard)
        
    check_aliens_bottom(aliens, ship, bullets, stats, scoreboard)
        
def check_aliens_bottom(aliens, ship, bullets, stats, scoreboard):
    screen_rect = game_screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hited(ship, aliens, bullets, stats, scoreboard)
            break
        
def ship_hited(ship, aliens, bullets, stats, scoreboard):
    """Descres life sigment"""
    stats.ship_lifes -= 1
    
    if stats.ship_lifes > 0:
    # Clear Screen
        aliens.empty()
        bullets.empty()
        
        create_fleet(aliens, ship.rect.height)
        ship.center_ship()
        
        
        # Update Scoreboard.
        scoreboard.prepare_ships()
        
        #pause
        sleep(2)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
            
            
        
def check_events(ship, bullets, play_button, stats, aliens, score_board):
    """ Listen events """
    for event in pygame.event.get():
         
        # Top bar exit button
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYBOARD 
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key_event(event, ship, bullets)
        
        # Mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                stats, play_button, mouse_x, mouse_y, ship, aliens, bullets,
                score_board
            )


def check_play_button(stats, play_button, mouse_x, mouse_y, 
                      ship, aliens, bullets, score_board):
    clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not stats.game_active:
        # Reset game
        game_configs.initialize_dynamic_configs()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game
        stats.reset_stats()
        stats.game_active = True
        score_board.prepare_score()
        score_board.prepare_high_score()
        score_board.prepare_level()
        score_board.prepare_ships()
        
        
        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        # Create a new row and center ship
        create_fleet(aliens, ship.rect.height)
        ship.center_ship()
        


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


def check_high_score(stats, scoreboard):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prepare_high_score()


    
    
    
    
    
    
