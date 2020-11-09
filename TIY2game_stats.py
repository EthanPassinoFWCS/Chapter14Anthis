class GameStats:
    """Tracks game stats for Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Creating statistics that can change during the game"""
        self.bullets_left = self.settings.bullet_limit
