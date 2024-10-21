import sys
import pygame
import time
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Alien


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
        pygame.display.set_caption(self.settings.title)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Track when the last bullet was fired
        self.last_bullet_time = 0  # Initialize with 0 (no bullet fired yet)

    def display_text(self, text):
        """Render and display text on the screen."""
        text_surface = self.font.render(text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(600, 400))  # Center of the screen
        self.screen.blit(text_surface, text_rect)

    def _skip_intro(self):
        """Immediately fill in the entire welcome text."""
        self.settings.displayed_text = self.settings.welcome_text
        self.settings.current_index = len(self.settings.welcome_text)
        self.settings.skip_intro = False  # Reset skip flag

        # Immediately display the full text
        self.screen.fill("cyan")
        self.display_text(self.settings.displayed_text)
        pygame.display.flip()  # Update the display

        self.settings.welcomed_user = True

    def run_typing_effect(self):
        """Run the typing effect for the welcome text."""
        start_time = time.time()

        while self.settings.current_index < len(self.settings.welcome_text):

            # Check events to allow skipping
            self._check_events()

            # Check if the intro should be skipped
            if self.settings.skip_intro:
                self._skip_intro()
                break

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
        self.settings.welcomed_user = True

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

            self.ship.update()
            self._fire_bullets()  # Fire bullets during each loop
            self._update_bullets()
            self._update_aliens()
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
            self.settings.bullet_speed = self.settings.base_bullet_speed * 2  # Speed up
            self.settings.ship_speed = self.settings.base_ship_speed * 2  # Speed up
        elif event.key == pygame.K_F11:
            self.toggle_fullscreen()
        elif event.key == pygame.K_RIGHT:
            self.ship.direction = "right"
            # self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.direction = "left"
            # self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.is_firing = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if not self.settings.welcomed_user:
            self.settings.skip_intro = True
        if event.key == pygame.K_RIGHT:
            self.ship.direction = ""
            # self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.direction = ""
            # self.ship.moving_left = False
        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.settings.ship_speed = self.settings.base_ship_speed  # Reset speed
            self.settings.bullet_speed = self.settings.base_bullet_speed  # Reset speed
        elif event.key == pygame.K_SPACE:
            self.ship.is_firing = False

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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()

    def _update_bullets(self):
        """Update postion of bullets and get rid of old bullets."""

        # Update bullet positions.
        self.bullets.update()

        # Remove bullets that have gone above range
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Fires bullets
        # self._fire_bullets()

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

        # Check if the ship is firing and if enough time has passed since the last bullet
        if (
            self.ship.is_firing
            and len(self.bullets) < self.settings.bullets_allowed
            and current_time - self.last_bullet_time >= self.settings.bullet_cooldown
        ):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            # Update the time the last bullet was fired
            self.last_bullet_time = current_time

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row

        Args:
            x_position (float): position to place alien
        """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien to get its size
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Calculate the maximum number of rows that can fit, while keeping a 3-alien-height gap at the bottom
        max_fleet_rows = (
            self.settings.screen_height - 3 * alien_height
        ) // alien_height
        fleet_rows = min((self.settings.level // 10) + 1, max_fleet_rows)
        print(f"Fleet rows: {fleet_rows}")

        # Loop through rows and columns to create aliens
        for row in range(fleet_rows):
            current_y = alien_height + (row * (2 * alien_height))
            for col in range(self.settings.screen_width // (2 * alien_width)):
                current_x = alien_width + (col * (2 * alien_width))
                self._create_alien(current_x, current_y)

    def _update_aliens(self):
        """Update the positions of all aliens in  the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Responds appropraitely if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
