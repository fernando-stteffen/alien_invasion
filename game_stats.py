class GameStats():
    """Track statistics for Alien invasion."""
    
    def __init__(self, game_configs):
        self.configs = game_configs
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        
        
    
    def reset_stats(self):
        self.ship_lifes = self.configs.ship_lifes
        self.score = 0
        
