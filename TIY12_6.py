import sys
import pygame
from TIY12_6Settings import Settings
from TIY12_6Ship import Ship
from TIY12_6Bullet import Bullet

# sys used to exit game, pygame for functionality, settings is for the settings of the game.

class AlienInvasion:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.settings = Settings()  # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Alien Invasion")  # sets window title.

        self.ship = Ship(self)  # creating ship object
        self.bullets = pygame.sprite.Group() # creating a group of bullet sprites.

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
            self.ship.moving_down = True # basically sets a flag to let the ship know it must move right.
        elif event.key == pygame.K_LEFT: # check if event key is left arrow
            self.ship.moving_up = True # basically sets a flag to let the ship know it must move left.
        elif event.key == pygame.K_q: # checks if key pressed was q
            sys.exit() # exits the program
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event): # keyup event helper.
        if event.key == pygame.K_RIGHT: # checks if the key that was released is right arrow.
            self.ship.moving_down = False # if it is we stop moving right.
        elif event.key == pygame.K_LEFT: # checks if the key that was released is left arrow.
            self.ship.moving_up = False # if it is we stop moving left.

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed: # checks bullets on screen and if there are less than the number of bullets allowed in settings, they fire a bullet.
            new_bullet = Bullet(self) # creating bullet object.
            self.bullets.add(new_bullet) # adding this new bullet to the group.

    def _update_bullets(self): # updating bullets helper method
        self.bullets.update() # updating bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right > bullet.screen_rect.right:
                self.bullets.remove(bullet)
        # Debug stuff: print(len(self.bullets))
        # goes through a copy of the sprite list, and removes any bullet below and at y cord 0 from the sprite list.

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # fills the background with the rgb color.
        self.ship.blitme()  # drawing ship to screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() # goes through each bullet in the group of sprites and draws them to the screen.
        pygame.display.flip()  # makes most recent drawn screen visible.

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.
            self.ship.update() # updating ship
            self._update_bullets() # updating bullets
            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
