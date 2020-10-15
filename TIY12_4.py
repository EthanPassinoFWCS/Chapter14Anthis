import sys
import pygame
from TIY12_4Settings import Settings
from TIY12_4Ship import Ship


# sys used to exit game, pygame for functionality, settings is for the settings of the game.

class TIY4:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.settings = Settings()  # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Alien Invasion")  # sets window title.

        self.ship = Ship(self)  # creating ship object

    def _check_events(self): # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.
            elif event.type == pygame.KEYDOWN: # checks if key was pressed
                self._check_keydown_events(event) # runs our helper method for keydown events.
            elif event.type == pygame.KEYUP: # checks if someone stops pressing a key.
                self._check_keyup_events(event) # runs our helper method for keyup events.

    def _check_keydown_events(self, event): # keydown event helper.
        if event.key == pygame.K_RIGHT: # checks if event key is right arrow
            self.ship.moving_right = True # basically sets a flag to let the ship know it must move right.
        elif event.key == pygame.K_LEFT: # check if event key is left arrow
            self.ship.moving_left = True # basically sets a flag to let the ship know it must move left.
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q: # checks if key pressed was q
            sys.exit() # exits the program

    def _check_keyup_events(self, event): # keyup event helper.
        if event.key == pygame.K_RIGHT: # checks if the key that was released is right arrow.
            self.ship.moving_right = False # if it is we stop moving right.
        elif event.key == pygame.K_LEFT: # checks if the key that was released is left arrow.
            self.ship.moving_left = False # if it is we stop moving left.
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # fills the background with the rgb color.
        self.ship.blitme()  # drawing ship to screen.
        pygame.display.flip()  # makes most recent drawn screen visible.

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.
            self.ship.update()
            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = TIY4()
    ai.run_game()
