import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__() # creating instance of parent class
        self.screen = ai_game.screen

        # Loading alien image and setting rect attribute for it.
        self.image = pygame.image.load("bin/alien.bmp")
        self.rect = self.image.get_rect()

        # Putting them at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing exact horizontal position of alien.
        self.x = float(self.rect.x)


