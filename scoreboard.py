import pygame.font

class Scoreboard():
    
    def __init__(self, configs, screen, stats):
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.configs = configs
        self.stats = stats
        
        
        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prepare_score()
        
        
    def prepare_score(self):
        """ Render score text """
        
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color
        )
        
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()       
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def score_draw(self):
        
        self.screen.blit(self.score_image, self.score_rect)
        
