class Configs():
    
    def __init__(self):
        # Game About:
        self.game_name = "Alien Invasion"
        self.game_version = "0.0.9"
        
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        
        
        # Ship configs
        self.ship_lifes = 3
        
        # Bullet configs
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.max_bullets = 3
        
        
        # Alien configs
        self.aliens_drop_speed = 10
     
        # leveling scale
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_configs()
        
        
    def initialize_dynamic_configs(self):
        """ Change when level up """
        self.ship_speed = 1.5
        self.aliens_speed = 1
        self.bullet_speed = 3
        # Direction 1 = right, -1 = left
        self.aliens_direction = 1
        
    
    def level_up(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.aliens_speed *= self.speedup_scale
        
        
        
    def get_game_name(self):
        return self.game_name + " - v" + self.game_version 
        
    
    def get_display_size(self):
        return ((self.screen_width, self.screen_height))
