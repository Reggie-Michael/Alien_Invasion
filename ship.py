import os
import pygame
import utils
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set it's starting position.

        Args:
            ai_game (_type_): _description_
        """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # movement flag, start with a ship that is not moving
        self.direction = ""  # right | left
        # self.movingRight = False
        # self.moving_left = False

        # Load the ship image ad get its rect.
        # self.image = pygame.image.load(utils.get_file_path("ship.bmp"))
        self.image = pygame.image.load(utils.get_file_path("space_ship2.png"))
        # Scale the image to half its size
        # original_size = self.image.get_size()
        # new_size = (
        #     original_size[0] // 3,
        #     original_size[1] // 3,
        # )  # Halve width and height
        # self.image = pygame.transform.scale(self.image, new_size)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.is_firing = False

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flags."""

        if self.direction == "right" and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.direction == "left" and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
