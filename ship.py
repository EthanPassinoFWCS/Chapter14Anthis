import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        # getting game screen data.
        self.screen_rect = ai_game.screen.get_rect()
        # rectangle screen data.

        self.image = pygame.image.load("bin/ship.bmp")
        # ship image.

        self.rect = self.image.get_rect()
        # Get ship rectangles.

        self.rect.midbottom = self.screen_rect.midbottom
        # setting ship location on screen, in this case middle bottom.

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # this method is used to draw a image to the screen.
