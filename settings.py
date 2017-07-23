import pygame

class Settings():
    """A class to store all settings for a game"""
    def intialise_dynamic_settings(self):
        """Initialise settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5

        # fleet_direction of 1 is right; -1 is left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 700
        self.bg_colour = (255, 255, 255)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 0

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (65, 105, 225)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 is right; -1 is left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.intialise_dynamic_settings()

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *=  self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        
