class GameStats():
    """Track statistics for Alien invasion."""
    
    def __init__(self, game_configs):
        self.configs = game_configs
        self.reset_stats()
        self.game_active = True
        
    
    def reset_stats(self):
        self.ship_lifes = self.configs.ship_lifes
