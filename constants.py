WIDTH, HEIGHT = 600, 600
BOARD_WIDTH, BOARD_HEIGHT = 500, 500
TILE_WIDTH, TILE_HEIGHT = 25, 25
X_OFFSET, Y_OFFSET = (WIDTH - BOARD_WIDTH) // 2, (HEIGHT - BOARD_HEIGHT) // 2 # Offsets so we can center our board
NUM_ROWS, NUM_COLS = BOARD_HEIGHT // TILE_HEIGHT, BOARD_WIDTH // TILE_WIDTH

# Define our color variables
BACKGROUND_COLOR = (29, 60, 50)
LIGHT_TILE_COLOR = (29, 60, 50)
DARK_TILE_COLOR = (24, 47, 41)
BORDER_COLOR = (255, 255, 255)
SNAKE_HEAD_COLOR = (5, 100, 57)
SNAKE_TAIL_COLOR = (10, 177, 102)
APPLE_COLOR = (255, 0, 0)

# Define the meanings of the tile numbers
TILES = {
    'EMPTY': 0,
    'APPLE': 1,
    'HEAD': 2,
    'TAIL': 3
}

# Define the meanings of the direction numbers
DIRECTIONS = {
    'UP': 0,
    'RIGHT': 1,
    'DOWN': 2,
    'LEFT': 3
}