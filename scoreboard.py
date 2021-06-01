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
        self.prepare_high_score()
        
        
    def prepare_score(self):
        """ Render score text """
        
        rounded_score = int(round(self.stats.score, - 1))
        score_str = score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            "Score | "+score_str, True, self.text_color
        )
        
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()       
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prepare_high_score(self):
        rounded_high_score = int(round(self.stats.high_score, - 1))
        high_score_str = score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(
            "High-Score | "+high_score_str, True, self.text_color
        )
        
        
        # Display the score at the top right of the screen
        self.high_score_rect = self.high_score_image.get_rect()       
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
        
        
    def score_draw(self):
        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        