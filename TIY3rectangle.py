import pygame
from pygame.sprite import Sprite


class Rectangle(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.rectangle_color
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.rectangle_width, self.settings.rectangle_height)
        self.rect.topright = self.screen_rect.topright

        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= (0 - self.rect.height):
            return True

    def update(self):
        self.y += (self.settings.rectangle_speed * self.settings.rectangle_direction)
        self.rect.y = self.y

    def draw_rectangle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def replace_rectangle(self):
        self.rect.topright = self.screen_rect.topright
        self.y = float(self.rect.y)
