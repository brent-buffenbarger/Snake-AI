from constants import *
from random import randint

# Function to create the initial snake
def generate_snake(board):
    _snake = []
    head_row = NUM_ROWS // 2
    head_col = NUM_COLS // 2

    # Add the head and 2 tail pieces
    _snake.append((head_row, head_col))         # Head of the snake
    _snake.append((head_row + 1, head_col))     # First piece of the tail
    _snake.append((head_row + 2, head_col))     # Second piece of the tail

    # Update the board tiles to show the snake
    board[head_row][head_col] = TILES['HEAD']
    board[head_row + 1][head_col] = TILES['TAIL']
    board[head_row + 2][head_col] = TILES['TAIL']

    return _snake

# Function to figure out which direction the tail is moving
def find_tail_dir(snake):
    caboose = snake[-1]
    parent = snake[-2]

    # Check for UP direction
    if caboose[0] > parent[0]:
        return DIRECTIONS['UP']
    
    # Check for DOWN direction
    if caboose[0] < parent[0]:
        return DIRECTIONS['DOWN']

    # Check for RIGHT direction
    if caboose[1] < parent[1]:
        return DIRECTIONS['RIGHT']

    # Check for LEFT direction
    if caboose[1] > parent[1]:
        return DIRECTIONS['LEFT']
    
# Function to append to the tail of the snake
def append_to_tail(snake, board, caboose):
    snake.append((caboose[0], caboose[1]))
    board[caboose[0]][caboose[1]] = TILES['TAIL']

# Function to spawn an apple on the board
def spawn_apple(board):
    # Get a list of all the empty tiles on the board
    empty_tiles = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            tile = board[row][col]
            if tile == TILES['EMPTY']:
                empty_tiles.append((row, col))

    # Randomly pick one of these empty tiles to spawn the apple
    idx = randint(0, len(empty_tiles) - 1)
    board[empty_tiles[idx][0]][empty_tiles[idx][1]] = TILES['APPLE']

# Function to change the direction of the snake
def change_dir(controller, head_dir):
    if len(controller.move_queue) == 0:
        return

    # Make sure we are not trying to go in the opposite direction of the current direction
    new_dir = controller.dequeue()
    up_down = head_dir[0] == DIRECTIONS['UP'] and new_dir == DIRECTIONS['DOWN']
    down_up = head_dir[0] == DIRECTIONS['DOWN'] and new_dir == DIRECTIONS['UP']
    left_right = head_dir[0] == DIRECTIONS['LEFT'] and new_dir == DIRECTIONS['RIGHT']
    right_left = head_dir[0] == DIRECTIONS['RIGHT'] and new_dir == DIRECTIONS['LEFT']

    if up_down or down_up or left_right or right_left:
        return

    head_dir[0] = new_dir

# Function to check if the snake has collided with anything
def check_collision(snake, board, caboose):
    # Check to see if the head collided with a north or south wall
    if snake[0][0] < 0 or snake[0][0] >= NUM_COLS:
        print("NORTH SOUTH COLLISION")
        return 'CRASH'

    # Check to see if the head collided with an east or west wall
    if snake[0][1] < 0 or snake[0][1] >= NUM_ROWS:
        print("EAST WEST COLLISION")
        return 'CRASH'

    # Check to see if the snake collided with itself - excluding the caboose since the caboose will move
    if board[snake[0][0]][snake[0][1]] > TILES['APPLE'] and (snake[0][0], snake[0][1]) != (caboose[0], caboose[1]):
        print("SELF COLLISION")
        return 'CRASH'

    if board[snake[0][0]][snake[0][1]] == TILES['APPLE']:
        print("APPLE WAS EATEN")
        return 'APPLE'

# Function to move the snake - takes the board as a param so we can update tiles
def move_snake(snake, board, dir, game_over):
    # Remove the end of the snake
    caboose = snake.pop()

    # Insert a new head depending on the dir
    head = snake[0]
    if dir == DIRECTIONS['UP']:
        snake.insert(0, (head[0] - 1, head[1]))
    elif dir == DIRECTIONS['RIGHT']:
        snake.insert(0, (head[0], head[1] + 1))
    elif dir == DIRECTIONS['DOWN']:
        snake.insert(0, (head[0] + 1, head[1]))
    elif dir == DIRECTIONS['LEFT']:
        snake.insert(0, (head[0], head[1] - 1))

    # Check to see if the snake collided with anything
    collision = check_collision(snake, board, caboose)
    if collision == 'CRASH':
        game_over[0] = True
        return

    # Update the tiles on the board
    board[caboose[0]][caboose[1]] = TILES['EMPTY']      # The old end of the tail becomes an empty tile
    board[head[0]][head[1]] = TILES['TAIL']             # The old head becomes a tail tile
    board[snake[0][0]][snake[0][1]] = TILES['HEAD']     # The new head becomes a head tile

    if collision == 'APPLE':
        append_to_tail(snake, board, caboose)
        spawn_apple(board)

# Function to handle the snake on each move
def handle_snake(snake, board, controller, head_dir, game_status):
    if game_status[0]:
        game_status[1] = True
        return

    # Check to see if the apple needs to be spawned for the first time
    if game_status[1]:
        game_status[1] = False
        spawn_apple(board)

    change_dir(controller, head_dir)                    # Check to see if a movement key was pressed
    move_snake(snake, board, head_dir[0], game_status)    # Move the snake