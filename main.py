import pygame
import numpy as np
from renderer import Renderer
from snake import generate_snake, handle_snake
from controller import Controller
from constants import *

# Setup a dictionary to map keyboard inputs to actions
ACTION_KEYS = {
    pygame.K_UP: DIRECTIONS['UP'],
    pygame.K_RIGHT: DIRECTIONS['RIGHT'],
    pygame.K_DOWN: DIRECTIONS['DOWN'],
    pygame.K_LEFT: DIRECTIONS['LEFT']
}

class SnakeGame:
    def __init__(self):
        # Setup our game window using WIDTH and HEIGHT from renderer.py
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake AI")
        pygame.font.init()

        # Setup our controller, renderer, snake, and movement direction
        self.controller = Controller()
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        self.renderer = Renderer(self.window, self.board)
        self.snake = generate_snake(self.board)
        self.head_dir = [DIRECTIONS['UP']] # This should be contained in a list so we can mutate it elsewhere
        self.game_status = [False, True]   # [0] = game_over and [1] = spawn_apple

        # Define FPS to determine how quickly our game updates
        self.fps = 10

    def reset_game(self):
        self.game_status[0] = False
        self.game_status[1] = True
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        self.head_dir[0] = DIRECTIONS['UP']
        self.snake = generate_snake(self.board)
        self.renderer.board = self.board
        self.controller.clear_queue()

    def start(self):
        clock = pygame.time.Clock() # Define clock so we can use FPS to control the speed of our game loop
        running = True # This boolean will be used to tell us when the game loop should end
        self.renderer.draw(len(self.snake) - 3, self.game_status[0]) # Draw the initial frame
        while running:
            clock.tick(self.fps) # Controls the speed of our game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Check for keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key in ACTION_KEYS:
                        self.controller.enqueue(ACTION_KEYS[event.key]) # If a direction key was pressed, add that action to the controller queue
                    elif event.key == pygame.K_SPACE and self.game_status[0]:
                        self.reset_game()

            handle_snake(self.snake, self.board, self.controller, self.head_dir, self.game_status)
            self.renderer.draw(len(self.snake) - 3, self.game_status[0])

        pygame.quit()

# Define our main function that will define a SnakeGame object and start the game loop
def main():
    game = SnakeGame()
    game.start()

if __name__ == "__main__":
    main()