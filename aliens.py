import pygame
import utils
from pygame.sprite import Sprite


class Alien(Sprite):
    """A Class to represent a single alien in the fleet."""

    alien_types = [0, 1, 2]
    alien_attributes = [
        {"image": "alien.bmp", "hp": 1},
        {"image": "alien2.png", "hp": 2},
        {"image": "SpiderBot2.png", "hp": 3},
    ]

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # alien type to determine health, and image
        alien_index = utils.get_value_by_level(self.settings.increment_counter)
        self.type = (
            alien_index if alien_index in self.alien_types else 0
        )  # for later when type is passed from game and it is outside tuple range

        set_alien = self.alien_attributes[self.type]
        # load the alien image and set it's rect attribute
        self.image = pygame.image.load(utils.get_file_path(set_alien.get("image")))
        if self.type > 0:
            # Scale the image to half its size
            original_size = self.image.get_size()
            new_size = (
                original_size[0] // 2,
                original_size[1] // 2,
            )  # Halve width and height
            self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Alien stats
        alien_hp = set_alien.get("hp")
        self.health = alien_hp + (
            alien_hp
            * (self.settings.increment_counter // (10 * len(self.alien_attributes)))
        )
        if self.settings.is_boss_level:
            self.health = self.health * (self.settings.increment_counter // 5)

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
