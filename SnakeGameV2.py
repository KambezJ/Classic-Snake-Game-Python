# Snake game v2

import tkinter
import random
import pygame

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Initialize pygame.mixer for music and sounds
pygame.mixer.init()

# Load background music
try:
    pygame.mixer.music.load("8bitmusic.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)  # Loop indefinitely
except FileNotFoundError:
    print("Background music file '8bitmusic.mp3' not found.")

# Load sound effects
try:
    crunch_sound = pygame.mixer.Sound("crunch.wav")
    crunch_sound.set_volume(1)
    gameover_sound = pygame.mixer.Sound("gameover.wav")
    gameover_sound.set_volume(1)
except FileNotFoundError as e:
    print(f"Sound file not found: {e}")

# Game window setup
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0,
                        highlightthickness=0)
canvas.pack()

window.update_idletasks()  # To center window, must update geometry after the window is initialized and rendered

# Centering the game window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initialize the game
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)  # Single tile for the snake's head
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)  # Initial food position
snake_body = []  # Snake body (excluding head)
velocityX = 0
velocityY = 0
game_over = False
score = 0


def change_direction(e):
    """Handle direction change based on key input."""
    global velocityX, velocityY

    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0


def reset_game():
    """Resets the game to its initial state."""
    global snake, food, snake_body, velocityX, velocityY, game_over, score

    # Reset snake's position and direction
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0


def restart_game(e):
    """Handles the restart of the game when the spacebar is pressed."""
    global game_over
    if e and game_over and e.keysym == "space":
        reset_game()
        pygame.mixer.music.play(loops=-1)  # Restart music
        draw()


def move():
    """Update snake and game state."""
    global snake, food, snake_body, game_over, score

    if game_over:
        return

    # Check for collisions with walls
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        if gameover_sound:
            gameover_sound.play()
        return

    # Check for collisions with the snake's own body
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            if gameover_sound:
                gameover_sound.play()
            return

    # Check for snake and food collision
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1

        # Play crunch sound
        if crunch_sound:
            crunch_sound.play()

    # Move each segment to the position of the previous segment
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if i == 0:  # The first tile follows the snake's head
            tile.x = snake.x
            tile.y = snake.y
        else:  # Other tiles follow the previous one
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    # Move the snake's head
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


def draw():
    """Render the game on the canvas."""
    global snake, food, snake_body, game_over, score

    move()

    canvas.delete("all")

    # Draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")

    # Draw snake head
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green")

    # Draw snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="lime green")

    # Display game over text, play sound, and give restart instructions
    if game_over:
        pygame.mixer.music.stop()  # Stop the background music
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font="Arial 20", text=f"Game Over! Score: {score}",
                           fill="white")
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 20, font="Arial 15",
                           text="Press Space to Restart", fill="white")
    else:
        canvas.create_text(50, 20, font="Arial 10", text=f"Score: {score}", fill="white")  # display score

    # Schedule next frame
    if not game_over:
        window.after(100, draw)


# Bind Spacebar to the reset function
window.bind("<KeyPress-space>", restart_game)

# Bind keys for controlling the snake
window.bind("<KeyPress>", change_direction)

# Start the game
draw()

# Run the Tkinter main loop
window.mainloop()
