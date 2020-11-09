class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 1280 # sets screen width VARIABLE.
        self.screen_height = 720 # sets screen height VARIABLE.
        self.bg_color = (230, 230, 230) # sets background color VARIABLE.
        # This can also be used to make an options file that is editable in-game by the user with the use of json.
        # To use this, import it in the main game.

        # Ship settings
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.5  # 1 speed
        self.bullet_width = 15  # 15 pixels wide
        self.bullet_height = 3  # 3 pixels high
        self.bullet_color = (60, 60, 60) # dark gray
        self.bullets_allowed = 1
        self.bullets_left = 3

        # Rectangle Settings
        self.rectangle_speed = 0.5
        self.rectangle_width = 15
        self.rectangle_height = 75
        self.rectangle_color = (60, 60, 60)

        # How quickly the game speeds up and how quickly the rectangles point number increases.
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.rectangle_speed = 0.5

        # Scoring
        self.rectangle_points = 10
        self.rectangle_direction = 1


    def increase_speed(self):
        """Increase difficulty by increasing speed."""
        self.rectangle_speed *= self.speedup_scale
        self.rectangle_points = int(self.rectangle_points * self.score_scale)
