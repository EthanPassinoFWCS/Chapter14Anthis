import sys
import pygame
from TIY2_Ship import Ship

# sys used to exit game, pygame for functionality, settings is for the settings of the game.

class TIY1:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.screen_width = 1200 # sets screen width VARIABLE.
        self.screen_height = 800 # sets screen height VARIABLE.
        self.bg_color = (0, 255, 255) # sets background color VARIABLE.
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Alien Invasion")  # sets window title.
        self.ship = Ship(self)

    def _check_events(self): # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.

    def _update_screen(self):
        self.screen.fill(self.bg_color)  # fills the background with the rgb color.
        self.ship.blitme()
        pygame.display.flip()  # makes most recent drawn screen visible.

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.
            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = TIY1()
    ai.run_game()
