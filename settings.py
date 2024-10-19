class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.title = 'Alien Invasion'
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
