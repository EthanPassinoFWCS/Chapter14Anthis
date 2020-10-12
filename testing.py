import sys
import pygame
from settings import Settings
from ship import Ship

# sys used to exit game, pygame for functionality, settings is for the settings of the game.

class AlienInvasion:
    def __init__(self):
        pygame.init() # initialize pygame

        self.settings = Settings() # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Alien Invasion") # sets window title.

        self.ship = Ship(self) # creating ship object

    def run_game(self):
        while True: # always running
            for event in pygame.event.get(): # getting a event invoked from pygame or the user.
                if event.type == pygame.QUIT: # checking if that event is quit.
                    sys.exit() # exiting the application.
            self.screen.fill(self.settings.bg_color) # fills the background with the rgb color.
            self.ship.blitme() # drawing ship to screen.
            pygame.display.flip() # makes most recent drawn screen visible.

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
