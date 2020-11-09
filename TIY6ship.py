import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        # getting the screen
        self.screen = ai_game.screen

        # getting the settings
        self.settings = ai_game.settings

        # getting game screen data.
        self.screen_rect = ai_game.screen.get_rect()
        # rectangle screen data.

        self.image = pygame.image.load("bin/spaceship.bmp")
        # ship image.

        self.rect = self.image.get_rect()
        # Get ship rectangles.

        self.rect.midbottom = self.screen_rect.midbottom
        # setting ship location on screen, in this case middle bottom.

        # Decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: # checking if the flag moving right is true and if the location of it is not too far right on the screen.
            self.x += self.settings.ship_speed # if it is true we move right by changing the x by 1
        if self.moving_left and self.rect.left > 0: # checking if the flag moving left is true and if its not off of the screen to the left.
            self.x -= self.settings.ship_speed # if it is true we move left by changing the x by -1
        self.rect.x = self.x # updating the x position when we move or update.

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # this method is used to draw a image to the screen.
