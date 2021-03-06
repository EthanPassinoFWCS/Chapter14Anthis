import sys
import pygame
from TIY2settings import Settings
from TIY2ship import Ship
from TIY2bullet import Bullet
from TIY2rectangle import Rectangle
from time import sleep
from TIY2button import Button
from TIY2scoreboard import Scoreboard
from TIY2game_stats import GameStats

# sys used to exit game, pygame for functionality, settings is for the settings of the game.


class RectangleGame:
    def __init__(self):
        pygame.init()  # initialize pygame

        self.settings = Settings()  # creating setting init

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # The above sets the display info height and width from the settings class.

        pygame.display.set_caption("Rectangle Game")  # sets window title.

        self.ship = Ship(self)  # creating ship object

        # Creating instance of Gamestats class
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.bullets = pygame.sprite.Group() # creating a group of bullet sprites.
        self.rectangles = pygame.sprite.Group() # creating a group of rectangle sprites.
        self.rectangles.add(Rectangle(self))

        # Make the play button
        self.play_button = Button(self, "Play")


    def _check_events(self): # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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
        elif event.key == pygame.K_p:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos, key_press=True)

    def _check_keyup_events(self, event): # keyup event helper.
        if event.key == pygame.K_RIGHT: # checks if the key that was released is right arrow.
            self.ship.moving_down = False # if it is we stop moving right.
        elif event.key == pygame.K_LEFT: # checks if the key that was released is left arrow.
            self.ship.moving_up = False # if it is we stop moving left.

    def _check_play_button(self, mouse_pos, key_press=False):
        """Start new game when player clicks on play."""
        if (self.play_button.rect.collidepoint(mouse_pos) or key_press) and not self.stats.game_active:
            # Reset dynamic settings
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_bullets()

            # Getting rid of remaining aliens and bullets
            self.bullets.empty()

            # Create a new fleet and center the ship
            self.ship.center_ship()

            # Make sure that the rectangle is repositioned
            for rectangle in self.rectangles.sprites():
                rectangle.replace_rectangle()

            # Make sure bullets_left is 3
            self.stats.bullets_left = 3

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed: # checks bullets on screen and if there are less than the number of bullets allowed in settings, they fire a bullet.
            new_bullet = Bullet(self) # creating bullet object.
            self.bullets.add(new_bullet) # adding this new bullet to the group.

    def _update_bullets(self): # updating bullets helper method
        self.bullets.update() # updating bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right > bullet.screen_rect.right:
                self.bullets.remove(bullet)
                self.stats.bullets_left-=1
                if self.stats.bullets_left == 0:
                    self.stats.game_active = False
        # goes through a copy of the sprite list, and removes any bullet below and at y cord 0 from the sprite list.
        self._check_bullet_rectangle_collisions()

    def _check_bullet_rectangle_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.rectangles, True, False)

        if collisions:
            self.stats.score += self.settings.rectangle_points
            self.sb.prep_score()
            self.sb.check_high_score()
            self.settings.increase_speed()

    def _update_rectangle(self):
        self._check_rectangle_edges()
        self.rectangles.update()

    def _check_rectangle_edges(self):
        for rectangle in self.rectangles.sprites():
            if rectangle.check_edges():
                self._change_rectangle_direction()
                break

    def _change_rectangle_direction(self):
        self.settings.rectangle_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # fills the background with the rgb color.
        self.ship.blitme()  # drawing ship to screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() # goes through each bullet in the group of sprites and draws them to the screen.

        for rectangle in self.rectangles.sprites():
            rectangle.draw_rectangle()

        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()  # makes most recent drawn screen visible.

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.

            if self.stats.game_active:
                self.ship.update() # updating ship
                self._update_bullets() # updating bullets
                self._update_rectangle()

            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = RectangleGame()
    ai.run_game()
