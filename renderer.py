import pygame
from constants import *

# Define a class that handles all of the drawing for the game
class Renderer:
    def __init__(self, window, board):
        self.window = window
        self.board = board

    # Function used to draw our checkered game board
    def draw_board(self):
        # Draw a small white border around the entire board
        border_thickess = 1
        border_width = NUM_COLS * TILE_WIDTH + (2 * border_thickess)
        border_height = NUM_ROWS * TILE_HEIGHT + (2 * border_thickess)
        border_x_pos = X_OFFSET - border_thickess
        border_y_pos = Y_OFFSET - border_thickess
        pygame.draw.rect(self.window, BORDER_COLOR, pygame.Rect(border_x_pos, border_y_pos, border_width, border_height))

        # Loop through the tiles from our Board instance and draw each one
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # Calculate the x and y position of the tile
                x_pos = j * TILE_WIDTH + X_OFFSET
                y_pos = i * TILE_HEIGHT + Y_OFFSET

                # even ID tiles have light color, dark otherwise
                color = LIGHT_TILE_COLOR if (i + j) % 2 == 0 else DARK_TILE_COLOR

                # Check to see if the tile is not empty and change the color accordingly
                if self.board[i][j] == TILES['HEAD']:
                    color = SNAKE_HEAD_COLOR
                elif self.board[i][j] == TILES['TAIL']:
                    color = SNAKE_TAIL_COLOR
                elif self.board[i][j] == TILES['APPLE']:
                    color = APPLE_COLOR
                
                # Add the tile to the canvas
                pygame.draw.rect(self.window, color, pygame.Rect(x_pos, y_pos, TILE_WIDTH, TILE_HEIGHT))

    # Define a draw function to handle our rendering
    def draw(self):
        self.window.fill(BACKGROUND_COLOR)  # Set the background color of the window
        self.draw_board()                   # Draw the current state of the board
        pygame.display.update()             # Update our display to reflect changes on screen