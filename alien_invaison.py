import sys
import pygame
import time
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(None, 48)  # Set font and size
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.default_screen_width, self.settings.default_screen_height)
        )
        self.ship = Ship(self)
        pygame.display.set_caption(self.settings.title)

    def display_text(self, text):
        """Render and display text on the screen."""
        text_surface = self.font.render(text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(600, 400))  # Center of the screen
        self.screen.blit(text_surface, text_rect)

    def run_typing_effect(self):
        """Run the typing effect for the welcome text."""
        start_time = time.time()

        while self.settings.current_index < len(self.settings.welcome_text):
            # Check how much time has passed for typing effect
            if time.time() - start_time >= self.settings.typing_speed:
                self.settings.displayed_text += self.settings.welcome_text[
                    self.settings.current_index
                ]
                self.settings.current_index += 1
                start_time = time.time()  # Reset timer

            # Fill the screen and display the current text
            self.screen.fill("cyan")
            self.display_text(self.settings.displayed_text)
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit the frame rate

        # After displaying the full text, show a blank screen for 2 seconds
        pygame.time.wait(1000)  # Wait for 1 second
        self.settings.displayed_text = ""  # Clear displayed text for the next loop
        self.settings.current_index = 0  # Reset index for potential further use
        self.screen.fill("#00000010")
        pygame.display.flip()  # Update the display
        self.clock.tick(60)
        pygame.time.wait(2000)  # Wait for 2 seconds

    def quit_game(self):
        """End the game loop."""
        self.settings.running = False
        sys.exit()

    def run_game(self):
        """Start the main loop for the game."""
        while self.settings.running:
            self._check_events()
            if not self.settings.welcomed_user:
                self.run_typing_effect()
                self.settings.welcomed_user = True

            self.ship.update()
            self._update_screen()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Responds to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            self.quit_game()
        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.settings.ship_speed = self.settings.base_ship_speed * 2  # Speed up
        elif event.key == pygame.K_F11:
            self.toggle_fullscreen()
        elif event.key == pygame.K_RIGHT:
            self.ship.direction = "right"
            # self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.direction = "left"
            # self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.direction = ""
            # self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.direction = ""
            # self.ship.moving_left = False
        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.settings.ship_speed = self.settings.base_ship_speed  # Reset speed

    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        if self.settings.is_fullscreen:
            # Set back to windowed mode
            self.screen = pygame.display.set_mode(
                (
                    self.settings.default_screen_width,
                    self.settings.default_screen_height,
                )
            )
            self.settings.is_fullscreen = False  # Update fullscreen state
        else:
            # Set to fullscreen mode
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self.settings.is_fullscreen = True  # Update fullscreen state

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
