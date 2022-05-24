from constants import *

# Function to create the initial snake
def generate_snake(board):
    _snake = []
    head_row = NUM_ROWS // 2
    head_col = NUM_COLS // 2

    # Add the head and 2 tail pieces
    _snake.append((head_row, head_col))         # Head of the snake
    _snake.append((head_row + 1, head_col))     # First piece of the tail
    _snake.append((head_row + 2, head_col))     # Second piece of the tail
    _snake.append((head_row + 3, head_col))     # Second piece of the tail
    _snake.append((head_row + 4, head_col))     # Second piece of the tail
    _snake.append((head_row + 5, head_col))     # Second piece of the tail

    # Update the board tiles to show the snake
    board[head_row][head_col] = TILES['HEAD']
    board[head_row + 1][head_col] = TILES['TAIL']
    board[head_row + 2][head_col] = TILES['TAIL']
    board[head_row + 3][head_col] = TILES['TAIL']
    board[head_row + 4][head_col] = TILES['TAIL']
    board[head_row + 5][head_col] = TILES['TAIL']

    return _snake

# Function to change the direction of the snake
def change_dir(controller, head_dir):
    if len(controller.move_queue) == 0:
        return
    head_dir[0] = controller.dequeue()

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
    elif collision == 'APPLE':
        pass

    # Update the tiles on the board
    board[caboose[0]][caboose[1]] = TILES['EMPTY']      # The old end of the tail becomes an empty tile
    board[head[0]][head[1]] = TILES['TAIL']             # The old head becomes a tail tile
    board[snake[0][0]][snake[0][1]] = TILES['HEAD']     # The new head becomes a head tile

# Function to handle the snake on each move
def handle_snake(snake, board, controller, head_dir, game_over):
    change_dir(controller, head_dir)                    # Check to see if a movement key was pressed
    move_snake(snake, board, head_dir[0], game_over)    # Move the snake