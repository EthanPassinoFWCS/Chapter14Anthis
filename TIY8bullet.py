import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        # Initializing parent class, getting information from other classes.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.screen_rect = self.screen.get_rect()

        # Creating a bullet at 0, 0 and then setting it to the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = ai_game.ship.rect.center

        # Storing bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        # Moving the bullet up the screen when you shoot it.
        self.x += self.settings.bullet_speed
        # Updating bullet position
        self.rect.x = self.x

    def draw_bullet(self):
        # Drawing the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
