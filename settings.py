class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.title = "Alien Invasion"
        self.default_screen_width = 1200
        self.default_screen_height = 800
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.running = True
        self.welcome_text = f"Welcome to {self.title}"
        self.welcomed_user = False
        self.displayed_text = ""
        self.current_index = 0
        self.typing_speed = 0.1  # Time in seconds between character displays
        self.is_fullscreen = False
        self.skip_intro = False

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7
        self.bullet_cooldown = 400  # 400 ms

        # Gameplay Settings
        self.ship_limit = 3  # Player health
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.increment_counter = 1  # Tracks progress

        self.initialize_dynamic_settings()

        # Alien Settings
        self.fleet_drop_speed = 10

    def initialize_dynamic_settings(self):
        """Initialize settings that change dynamically."""
        self.is_boss_level = (
            self.increment_counter % 5 == 0 and self.increment_counter >= 5
        )
        self.base_ship_speed = 1.5
        self.ship_speed = self.base_ship_speed
        self.base_bullet_speed = 2.0
        self.bullet_speed = self.base_bullet_speed

        # Alien speed and points depend on increment_counter and boss level
        increment_amount = 0.05 if self.is_boss_level else 0.02
        self.alien_speed = 1.0 + (
            self.increment_counter * increment_amount
        )  # Increment by 0.02 each step, 0.05 for boss steps

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring: Different points for normal and boss levels, scaling the score
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings based on the current game progress."""
        self.base_ship_speed *= self.speedup_scale
        self.base_bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def update_increment(self):
        """Update increment counter and re-check boss level."""
        self.increment_counter += 1
        self.is_boss_level = self.increment_counter % 5 == 0
        self.initialize_dynamic_settings()  # Reinitialize settings after an increment
