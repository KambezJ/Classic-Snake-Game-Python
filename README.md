# Snake Game v2: A Classic Snake Game Built with Python and Tkinter

## Overview
This project is a modern rendition of the classic Snake game, built entirely in Python using the Tkinter library for GUI development. It showcases essential programming skills such as GUI programming, event-driven logic, and game state management. The game features:

- **Real-Time Animation:** Smooth snake movement and dynamic food placement rendered on a grid-based canvas.
- **Interactive Gameplay:** Direction control using arrow keys and a restart option upon game over.
- **Sound Effects and Background Music:** Implemented using `pygame` for an immersive experience.
- **Dynamic UI:** Real-time score tracking and responsive game-over messages displayed on-screen.

## Features

### Core Features
1. **Grid-Based Gameplay**
   - The game operates on a 25x25 grid where each tile represents a game cell.
2. **Real-Time Snake Movement**
   - The snake moves seamlessly, with its body following the head.
3. **Food Placement and Consumption**
   - Food appears at random grid locations. Eating food increases the snake's length and score.
4. **Collision Detection**
   - Detects collisions with the snake's body or game boundaries, ending the game.
5. **Restart Functionality**
   - Pressing the spacebar resets the game state and restarts gameplay.
6. **Background Music and Sound Effects**
   - Looping background music and sound effects for eating food or game over.

### Enhancements
- **Centered Game Window**
  - The game window is dynamically centered on the user's screen for a better user experience.
- **Customizable Settings**
  - Easily modify grid size, tile size, or game speed by adjusting constants.

## How to Play
1. Use the **arrow keys** to control the snake's movement.
2. Avoid colliding with the walls or your own body.
3. Eat the red food to grow the snake and increase your score.
4. Press **spacebar** to restart the game after the game is over.

## Screenshots

<img src="https://i.imgur.com/t4r8Vgp.png" height="50%" width="50%" alt="Game Start"/> <img src="https://i.imgur.com/BdJG4d2.png" height="50%" width="50%" alt="Game End"/>

## Getting Started

### Prerequisites
- Python 3.9 or 3.11 (those two are confirmed to be compatible with the dependencies/packages)
- Required libraries:
  - `pygame`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snake-game-v2.git
   cd snake-game-v2
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```
3. Place your sound files (`8bitmusic.mp3`, `crunch.wav`, `gameover.wav`) in the project directory.

### Running the Game
Run the `snake_game.py` file:
```bash
python snake_game.py
```

## Code Overview

### Key Components

#### 1. **Snake Movement and Body Management**
- Movement logic ensures the snake's body follows the head.
- The `move()` function handles updates to the snake's position and checks for collisions.

#### 2. **Food Placement**
- Randomized placement ensures food appears within the grid.
- The snake's body is extended when food is consumed.

#### 3. **Event Handling**
- Key presses control the snake's direction (`Up`, `Down`, `Left`, `Right`).
- The spacebar resets the game after a game over.

#### 4. **Sound Effects**
- Background music is played continuously using `pygame.mixer`.
- Sound effects for food consumption and game over are triggered asynchronously using `threading`.

### File Structure
```
/project-folder
  |-- snake_game.py          # Main game logic
  |-- 8bitmusic.mp3          # Background music file
  |-- crunch.wav             # Sound effect for eating food
  |-- gameover.wav           # Sound effect for game over
```

## Future Enhancements
1. **Levels and Difficulty**
   - Introduce multiple levels with increasing speed or obstacles.
2. **Leaderboard**
   - Track and display high scores.
3. **Customizable Themes**
   - Allow users to select different snake and background themes.
4. **Mobile Compatibility**
   - Adapt the game for touch-based controls on mobile devices.
5. **Power-Ups**
   - Add special items for temporary boosts or effects.

## Skills Demonstrated

### Core Python Skills
1. **Object-Oriented Programming (OOP):**
   - Encapsulation of game entities (`Tile` class) for reusability and clarity.
2. **Event-Driven Programming:**
   - Use of `Tkinter` events to handle real-time user input.
3. **GUI Development with Tkinter:**
   - Creating, updating, and managing game elements on a canvas.
4. **Multithreading:**
   - Asynchronous sound playback using Python's `threading` module.
5. **Randomization:**
   - Generating random grid positions for food placement.
6. **Algorithmic Thinking:**
   - Efficiently updating the snake's movement and detecting collisions.
7. **Collision Detection:**
   - The game includes logic to detect collisions with walls, the snake's own body, and the food.
8. **File Handling (Audio Playback):**
   - Python library pygame is used for playing background music and sound effects.

### Additional Skills
- **Game State Management:**
  - Managing and updating the game's dynamic state variables (e.g., `score`, `game_over`).
- **File Handling for Audio Playback:**
  - Integration of `pygame` for background music and effects.

## Acknowledgements
- Background music from pixabay.
- Sound effects from pixabay.
