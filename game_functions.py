import sys
import pygame


def check_events(ship):
    """ Respond to keyboard and mouse events """
    for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                print("event key:" + str(event.key))
                print("pygame key:" + str(pygame.K_LEFT))
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    print("Moving to the right")
                    ship.moving_right = True
                
                if event.key == pygame.K_LEFT:
                    print("Moving to the left")
                    ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False

            

def update_screen(game_configs, screen, ship):
    """ Update sprites in the new screen """
    
    # Dawing
    screen.fill(game_configs.background_color)
    ship.blitme()

    # Refresh Screen
    pygame.display.flip()    
    
