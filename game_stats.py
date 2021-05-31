class GameStats():
    """Track statistics for Alien invasion."""
    
    def __init__(self, game_configs):
        self.configs = game_configs
        self.reset_stats()
        
    
    def reset_stats(self):
        self.ships_left = self.configs.ship_lifes
