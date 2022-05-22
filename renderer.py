import pygame

# Initialize some dimension variables
WIDTH, HEIGHT = 600, 600
BOARD_WIDTH, BOARD_HEIGHT = 500, 500
TILE_WIDTH, TILE_HEIGHT = 25, 25
X_OFFSET, Y_OFFSET = (WIDTH - BOARD_WIDTH) // 2, (HEIGHT - BOARD_HEIGHT) // 2 # Offsets so we can center our board
NUM_ROWS, NUM_COLS = BOARD_HEIGHT // TILE_HEIGHT, BOARD_WIDTH // TILE_WIDTH

# Define our color variables
BACKGROUND_COLOR = (37, 51, 68)
LIGHT_TILE_COLOR = (37, 51, 68)
DARK_TILE_COLOR = (31, 39, 54)
BORDER_COLOR = (255, 255, 255)
SNAKE_COLOR = (45, 139, 212)

# Define a class that handles all of the drawing for the game
class Renderer:
    def __init__(self, window):
        self.window = window

    # Function used to draw our checkered game board
    def draw_board(self):
        # Draw a small white border around the entire board
        border_thickess = 1
        border_width = NUM_COLS * TILE_WIDTH + (2 * border_thickess)
        border_height = NUM_ROWS * TILE_HEIGHT + (2 * border_thickess)
        border_x_pos = X_OFFSET - border_thickess
        border_y_pos = Y_OFFSET - border_thickess
        pygame.draw.rect(self.window, BORDER_COLOR, pygame.Rect(border_x_pos, border_y_pos, border_width, border_height))

        # Loop through the rows and columns and draw a rectangle at each spot
        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                # If the row number plus col number is even, draw a LIGHT tile, otherwise draw a DARK tile
                color = LIGHT_TILE_COLOR if (i + j) % 2 == 0 else DARK_TILE_COLOR
                x_pos = (i * TILE_WIDTH) + X_OFFSET
                y_pos = (j * TILE_HEIGHT) + Y_OFFSET
                pygame.draw.rect(self.window, color, pygame.Rect(x_pos, y_pos, TILE_WIDTH, TILE_HEIGHT))

    # Define a draw function to handle our rendering
    def draw(self):
        self.window.fill(BACKGROUND_COLOR) # Set the background color of the window
        self.draw_board() # Draw the checkered game board
        pygame.display.update() # Update our display to reflect changes on screen