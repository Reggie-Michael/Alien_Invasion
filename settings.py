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
        self.base_ship_speed = 1.5
        self.ship_speed = self.base_ship_speed
        self.is_fullscreen = False
        self.skip_intro = False

        # Bullet Settings
        self.base_bullet_speed = 2.0
        self.bullet_speed = self.base_bullet_speed
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15
        self.bullet_cooldown = 400  # 400 ms

        # Gameplay Settings
        self.level = 1
        self.isBossLevel = self.level % 5 == 0

        # Alien Settings
        self.alien_speed = 1.0 + (  # Base speed
            self.level * 0.05 if self.isBossLevel else 0.02
        )  # Increment by 0.02 each level and ).5 for boss level
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
