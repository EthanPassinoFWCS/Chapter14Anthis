import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

# sys used to exit game, pygame for functionality, settings is for the settings of the game.


class AlienInvasion:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.settings = Settings()  # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Alien Invasion")  # sets window title.

        # Creating instance of Gamestats class
        self.stats = GameStats(self)

        self.ship = Ship(self)  # creating ship object
        self.bullets = pygame.sprite.Group() # creating a group of bullet sprites.
        self.aliens = pygame.sprite.Group() # creating a group of alien sprites.

        self._create_fleet() # creating the fleet.

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Getting number of aliens per row.
        available_space_x = self.settings.screen_width - (2 * alien_width) # gets space available by removing two aliens (the edges of the screen) from the length.
        number_aliens_x =   available_space_x // (2 * alien_width) # Basically one alien is technically two (because its space counts as one) so we check how many 2 we can draw to screen.

        # Getting the number of rows of aliens that fits on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Creating full fleet of aliens:

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

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
        elif event.key == pygame.K_q: # checks if key pressed was q
            sys.exit() # exits the program
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event): # keyup event helper.
        if event.key == pygame.K_RIGHT: # checks if the key that was released is right arrow.
            self.ship.moving_right = False # if it is we stop moving right.
        elif event.key == pygame.K_LEFT: # checks if the key that was released is left arrow.
            self.ship.moving_left = False # if it is we stop moving left.

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed: # checks bullets on screen and if there are less than the number of bullets allowed in settings, they fire a bullet.
            new_bullet = Bullet(self) # creating bullet object.
            self.bullets.add(new_bullet) # adding this new bullet to the group.

    def _update_bullets(self): # updating bullets helper method
        self.bullets.update() # updating bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # goes through a copy of the sprite list, and removes any bullet below and at y cord 0 from the sprite list.

        # Check for any bullets that hit aliens. If so we get rid of bullet and alien.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if not self.aliens:
            # Destroy bullets and create a new fleet if no aliens.
            self.bullets.empty() # deletes all bullets.
            self._create_fleet() # creates new fleet.

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # fills the background with the rgb color.
        self.ship.blitme()  # drawing ship to screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() # goes through each bullet in the group of sprites and draws them to the screen.
        self.aliens.draw(self.screen) # drawing all aliens in the sprite group to the screen surface.
        pygame.display.flip()  # makes most recent drawn screen visible.

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Stuff done when the ship gets hit"""

        if self.stats.ships_left > 0:
            # Decrease number of ships left.
            self.stats.ships_left -= 1

            # Delete remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.

            if self.stats.game_active: # basically stuff in this if statement only runs if the game is active.
                self.ship.update() # updating ship
                self._update_bullets() # updating bullets
                self._update_aliens() # updating aliens
                self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
