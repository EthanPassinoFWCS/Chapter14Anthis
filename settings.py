class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 1280 # sets screen width VARIABLE.
        self.screen_height = 720 # sets screen height VARIABLE.
        self.bg_color = (230, 230, 230) # sets background color VARIABLE.
        # This can also be used to make an options file that is editable in-game by the user with the use of json.
        # To use this, import it in the main game.

        # Ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3 # 3 pixels wide
        self.bullet_height = 15 # 15 pixels high
        self.bullet_color = (60, 60, 60) # dark gray
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        # Fleet_direction of 1 represents right; =1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase difficulty by increasing speed."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
