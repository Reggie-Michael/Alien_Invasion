Certainly! Here’s a revised version of the README to cover all the files with descriptions of their roles and configurations:

---

# Alien Invasion Game

A classic arcade-style game where the player controls a spaceship to fend off waves of aliens. The game supports increasing difficulty, unique alien types, and various scoring and level features.

## Table of Contents
- [Alien Invasion Game](#alien-invasion-game)
  - [Table of Contents](#table-of-contents)
  - [Game Overview](#game-overview)
  - [Setup and Installation](#setup-and-installation)
  - [File Structure](#file-structure)
  - [Classes and Configurations](#classes-and-configurations)
- [Alien Invasion Game](#alien-invasion-game-1)
  - [Overview](#overview)
  - [File Structure](#file-structure-1)
    - [alien\_invasion.py](#alien_invasionpy)
      - [Class: AlienInvasion](#class-alieninvasion)
    - [settings.py](#settingspy)
      - [Class: Settings](#class-settings)
      - [Key Attributes](#key-attributes)
    - [alien.py](#alienpy)
      - [Class: Alien](#class-alien)
    - [ship.py](#shippy)
      - [Class: Ship](#class-ship)
    - [bullet.py](#bulletpy)
      - [Class: Bullet](#class-bullet)
    - [scoreboard.py](#scoreboardpy)
      - [Class: Scoreboard](#class-scoreboard)
    - [button.py](#buttonpy)
      - [Class: Button](#class-button)
    - [game\_stats.py](#game_statspy)
      - [Class: GameStats](#class-gamestats)
    - [utils.py](#utilspy)
  - [Gameplay](#gameplay)
  - [Future Enhancements](#future-enhancements)
  - [How to Play](#how-to-play)
  - [Contributing](#contributing)

## Game Overview

The **Alien Invasion Game** challenges players to protect their spaceship from waves of increasingly powerful aliens. Each alien type has unique health points and images, providing a dynamic and challenging experience. Players can advance levels, track scores, and achieve new high scores.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Install required packages**:
   Ensure `pygame` is installed. You can install it via:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   You have two options to run the game:
   - **From the source code**: Execute the following command in your terminal or command prompt:
     ```bash
     python alien_invasion.py
     ```
   - **From the executable**: Run the executable file (e.g., `AlienInvasion.exe` on Windows).


## File Structure

```plaintext
|-- alien_invaision.py         # Main file containing game-play and merging game elements
|-- alien.py         # Alien configurations and behaviors
|-- ship.py          # Ship configurations and controls
|-- bullet.py        # Bullet properties and behavior
|-- scoreboard.py    # Scoring and game level display
|-- button.py        # Button functionality for game actions
|-- game_stats.py     # Game state management and statistics tracking
|-- utils.py         # Utility functions for common game operations
|-- settings.py         # Game basic setting configurations
```

## Classes and Configurations

Here's a comprehensive README section that includes the `settings.py` file along with `alien_invasion.py` for your game. You can adjust the content to fit your style as needed:

---

# Alien Invasion Game

## Overview
Alien Invasion is an engaging game where players control a ship to fend off waves of alien invaders. The game features a variety of settings to enhance gameplay, including customizable screen dimensions, bullet configurations, and dynamic alien behaviors.

## File Structure

### alien_invasion.py

This is the main file that connects the game elements together, managing the game flow and functionalities. The core class is `AlienInvasion`, which contains methods to run the game, handle events, and update the game state.

#### Class: AlienInvasion

- **`__init__()`**: Initializes the game settings, creates game objects, and sets up the display.
- **`display_text(text)`**: Renders and displays text on the screen.
- **`_skip_intro()`**: Skips the intro text, immediately displaying the full welcome message.
- **`run_typing_effect()`**: Displays the welcome text with a typing effect.
- **`quit_game()`**: Ends the game loop.
- **`run_game()`**: Starts the main loop for the game, handling events and updating game elements.
- **`_check_events()`**: Responds to keypress and mouse events.
- **`_check_keydown_events(event)`**: Handles key press events.
- **`_check_keyup_events(event)`**: Handles key release events.
- **`toggle_fullscreen()`**: Toggles between fullscreen and windowed mode.
- **`_update_screen()`**: Updates the display, showing the current game state.
- **`_update_bullets()`**: Updates the positions of bullets and removes old bullets.
- **`_reset_game()`**: Resets the game to default values.
- **`_ship_hit()`**: Responds to the ship being hit by an alien.
- **`_check_bullet_alien_collisions()`**: Checks for collisions between bullets and aliens.
- **`_repopulate_aliens()`**: Repopulates the fleet of aliens if all are destroyed.
- **`_fire_bullets()`**: Creates and adds new bullets to the game.
- **`_create_alien(x_position, y_position)`**: Creates an alien and places it at the specified coordinates.
- **`_create_fleet()`**: Creates the fleet of aliens on the screen.
- **`_update_aliens()`**: Updates the positions of all aliens in the fleet.
- **`_check_fleet_edges()`**: Responds if any aliens have reached an edge of the screen.
- **`_change_fleet_direction()`**: Changes the direction of the entire fleet when an edge is reached.
- **`_start_game()`**: Runs the necessary functions to start the game.
- **`_check_play_button_click(mouse_pos)`**: Starts a new game when the player clicks the "Play" button.
- **`_check_aliens_bottom()`**: Checks if any aliens have reached the bottom of the screen.

### settings.py

This file contains the settings for the Alien Invasion game, allowing customization of various game parameters.

#### Class: Settings

- **`__init__()`**: Initializes the game settings, including screen dimensions, background color, bullet settings, and gameplay parameters.
- **`initialize_dynamic_settings()`**: Initializes settings that change dynamically based on the game progress, such as alien speed and scoring.
- **`increase_speed()`**: Increases speed settings based on the current game progress.
- **`update_increment()`**: Updates the increment counter and checks if it's a boss level.

#### Key Attributes

- **Screen Settings**
  - `title`: Title of the game.
  - `default_screen_width`: Default width of the game window.
  - `default_screen_height`: Default height of the game window.
  - `bg_color`: Background color of the game.
  - `is_fullscreen`: Boolean indicating if the game is in fullscreen mode.
  - `welcome_text`: Welcome message displayed to the user.

- **Bullet Settings**
  - `bullet_width`: Width of the bullets.
  - `bullet_height`: Height of the bullets.
  - `bullet_color`: Color of the bullets.
  - `bullets_allowed`: Maximum number of bullets allowed on the screen at once.
  - `bullet_cooldown`: Time delay between firing bullets.

- **Gameplay Settings**
  - `ship_limit`: Number of ships the player has (player health).
  - `speedup_scale`: Factor by which the speed increases as the game progresses.
  - `score_scale`: Factor by which the alien points increase.

- **Alien Settings**
  - `fleet_drop_speed`: Speed at which the alien fleet drops.


### alien.py

Defines the `Alien` class, representing individual aliens with customizable images, health points, and behaviors based on level. Alien type and image size adjust based on the game level:

#### Class: Alien

- **Attributes**:
  - `alien_types`: List of alien types.
  - `alien_attributes`: List of dictionaries, each with image paths and HP values.
- **Initialization**:
  - Sets alien type, health, and image scaling depending on the current level.
- **Methods**:
  - `check_edges`: Checks if an alien has reached the screen's edge.
  - `update`: Adjusts alien movement based on speed and direction settings.

### ship.py

Defines the `Ship` class, responsible for managing the player’s spaceship:

#### Class: Ship

- **Attributes**:
  - `screen`, `screen_rect`: The display screen and dimensions.
  - `settings`: Game settings, including ship speed.
  - `direction`: Tracks movement direction.
- **Initialization**:
  - Sets the ship’s initial position, movement direction, and image.
- **Methods**:
  - `blitme`: Draws the ship at its current position.
  - `center_ship`: Centers the ship for a new round or reset.
  - `update`: Updates the ship’s position based on movement flags.

### bullet.py

Defines the `Bullet` class for handling bullets fired by the ship:

#### Class: Bullet

- **Attributes**:
  - `screen`, `settings`: Settings like bullet color, speed, and size.
  - `color`: Bullet color.
- **Initialization**:
  - Sets the bullet’s initial position based on the ship’s current position.
- **Methods**:
  - `update`: Moves the bullet up the screen.
  - `draw_bullet`: Draws the bullet.

### scoreboard.py

Manages the score display and other game information:

#### Class: Scoreboard

- **Attributes**:
  - `score`, `high_score`, `level`: Tracks score, high score, and level.
  - `text_color`, `font`: Scoreboard font and color settings.
- **Initialization**:
  - Prepares initial score, level, and ship count.
- **Methods**:
  - `prep_score`, `prep_high_score`, `prep_level`: Render images of score, high score, and level.
  - `show_score`: Draws scores and ships remaining.

### button.py

Defines the `Button` class to handle game buttons:

#### Class: Button

- **Attributes**:
  - `width`, `height`: Button size.
  - `button_color`, `text_color`: Colors for button and text.
- **Initialization**:
  - Sets button dimensions, color, and text properties.
- **Methods**:
  - `_prep_msg`: Converts the message text to an image.
  - `draw_button`: Draws the button on the screen with text.

### game_stats.py

Tracks and manages game statistics:

#### Class: GameStats

- **Attributes**:
  - `high_score`: Highest score achieved.
  - `ships_left`, `score`, `level`: Tracks lives, score, and level progression.
- **Initialization**:
  - Resets stats when starting or resetting the game.
- **Methods**:
  - `reset_stats`: Resets stats that change during gameplay.
  - `next_round`: Advances the game level and updates settings.

### utils.py

Utility functions to support common game operations:

- **Functions**:
  - `get_file_path`: Returns the image path based on the folder and filename.
  - `get_value_by_level`: Determines an alien type based on the current level, with special handling for multiples of 10.

## Gameplay

- **Objective**: Control the spaceship to destroy waves of aliens and progress through levels.
- **Controls**: Use arrow keys to move left and right, and spacebar to fire bullets.
- **Scoring**: Points are awarded based on aliens destroyed, with high scores tracked.

## Future Enhancements
- Adding more alien types with unique behaviors.
- Power-ups for the spaceship.
- Enhanced visual and sound effects for better player engagement.

## How to Play

- Use the arrow keys to move your ship.
- Press the spacebar to shoot bullets at the aliens.
- Avoid alien projectiles to preserve your ship's lives.
- Aim to achieve the highest score possible!

## Contributing

Contributions are welcome! Feel free to submit issues, pull requests, or suggest features.

