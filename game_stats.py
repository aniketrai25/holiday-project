class GameStats():
    """Track statistics for Space Invaders"""

    def __init__(self, ai_settings):
        """Initialise statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start the game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
