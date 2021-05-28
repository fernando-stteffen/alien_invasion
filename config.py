class Configs():
    
    def __init__(self):
        # Game About:
        self.game_name = "Alien Invasion"
        self.game_version = "0.0.1"
        
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        
    def get_game_name(self):
        return self.game_name + " - v" + self.game_version 
        
