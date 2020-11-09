class GameStats:
    """Tracks game stats for Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.get_high_score()
        self.high_score = 0

        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Creating statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        with open("highscore.txt", "w+") as f:
            score = f.readline()
            if score == "" or score == "0":
                f.write(str(self.high_score))
            elif int(score) < self.high_score:
                f.write(str(self.high_score))

    def get_high_score(self):
        with open("highscore.txt", "w+") as f:
            content = f.readline()
            if content != "":
                self.high_score = int(content)
            else:
                f.write("0")


