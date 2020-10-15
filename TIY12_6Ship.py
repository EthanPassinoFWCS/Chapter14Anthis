import pygame

class Ship:

    def __init__(self, ai_game):
        # getting the screen
        self.screen = ai_game.screen

        # getting the settings
        self.settings = ai_game.settings

        # getting game screen data.
        self.screen_rect = ai_game.screen.get_rect()
        # rectangle screen data.

        self.image = pygame.image.load("bin/spaceship.bmp")
        # ship image.

        self.image = pygame.transform.rotate(self.image, -90)
        # sets the image to rotate -90 degrees

        self.rect = self.image.get_rect()
        # Get ship rectangles.

        self.rect.midleft = self.screen_rect.midleft
        # setting ship location on screen, in this case middle bottom.

        # Decimal value for the ships horizontal position
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # checking if the flag moving right is true and if the location of it is not too far right on the screen.
            self.y += self.settings.ship_speed # if it is true we move right by changing the x by 1
        if self.moving_up and self.rect.top > 0: # checking if the flag moving left is true and if its not off of the screen to the left.
            self.y -= self.settings.ship_speed # if it is true we move left by changing the x by -1
        self.rect.y = self.y # updating the x position when we move or update.

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # this method is used to draw a image to the screen.
