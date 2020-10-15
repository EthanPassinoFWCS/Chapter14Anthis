import sys
import pygame


# sys used to exit game, pygame for functionality, settings is for the settings of the game.

class TIY5:
    def __init__(self):
        pygame.init()  # initialize pygame
        pygame.font.init() # you have to call this at the start,
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen_width = 1200 # sets screen width VARIABLE.
        self.screen_height = 800 # sets screen height VARIABLE.
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # The above sets the display info height and width from the settings class.
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        pygame.display.set_caption("Alien Invasion")  # sets window title.
        self.text = self.myfont.render(f"", True, self.green, self.blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screen_width // 2, self.screen_height // 2)

    def _check_events(self): # single leading underscores definte helper methods
        for event in pygame.event.get():  # getting a event invoked from pygame or the user.
            if event.type == pygame.QUIT:  # checking if that event is quit.
                sys.exit()  # exiting the application.
            if event.type == pygame.KEYDOWN:
                self.text = self.myfont.render(f"{event.key}", True, self.green, self.blue)
                self.textRect = self.text.get_rect()
                self.textRect.center = (self.screen_width // 2, self.screen_height // 2)

    def _update_screen(self):
        pygame.display.flip()  # makes most recent drawn screen visible.
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.text, self.textRect)

    def run_game(self):
        while True:  # always running
            self._check_events() # runs the check events method... which checks events by the user.
            self._update_screen() # runs the updating screen, which draws objects to the screen and backgrounds and such.


if __name__ == '__main__':
    ai = TIY5()
    ai.run_game()
