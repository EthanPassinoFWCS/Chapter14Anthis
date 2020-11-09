import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__() # creating instance of parent class
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading alien image and setting rect attribute for it.
        self.image = pygame.image.load("bin/alien.bmp")
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Putting them at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing exact horizontal position of alien.
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y
