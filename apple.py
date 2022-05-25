from random import randint
from constants import TILES

# Function to spawn an apple on the board
def spawn_apple(board):
    # Get a list of all the empty tiles on the board
    empty_tiles = []
    for row in board:
        for col in row:
            tile = board[row][col]
            if tile == TILES['EMPTY']:
                empty_tiles.append((row, col))

    # Randomly pick one of these empty tiles to spawn the apple
    idx = randint(0, len(empty_tiles) - 1)
    board[empty_tiles[idx][0]][empty_tiles[idx][1]] = TILES['APPLE']