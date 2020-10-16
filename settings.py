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
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1.5 # 1 speed
        self.bullet_width = 3 # 3 pixels wide
        self.bullet_height = 15 # 15 pixels high
        self.bullet_color = (60, 60, 60) # dark gray
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet direction, 1 represents right; -1 represents left.
        self.fleet_direction = 1
