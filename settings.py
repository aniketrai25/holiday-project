import pygame

class Settings():
    """A class to store all settings for a game"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 700
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (65, 105, 225)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed_factor = 1.2
        self.fleet_drop_speed = 2
        # fleet_direction of 1 is right; -1 is left
        self.fleet_direction = 1
        
        
