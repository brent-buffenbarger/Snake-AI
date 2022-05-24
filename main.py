import pygame
from renderer import Renderer
from snake import generate_snake, handle_snake
from board import board
from controller import Controller
from constants import *

# Setup our game window using WIDTH and HEIGHT from renderer.py
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake AI")

# Setup our controller, renderer, snake, and movement direction
controller = Controller()
renderer = Renderer(WIN, board)
snake = generate_snake(board)
head_dir = [DIRECTIONS['UP']] # This should be contained in a list so we can mutate it elsewhere
game_over = [False]           # This sohuld be contained in a list so we can mutate it elsewhere

# Define FPS to determine how quickly our game updates
FPS = 2

# Setup a dictionary to map keyboard inputs to actions
ACTION_KEYS = {
    pygame.K_UP: DIRECTIONS['UP'],
    pygame.K_RIGHT: DIRECTIONS['RIGHT'],
    pygame.K_DOWN: DIRECTIONS['DOWN'],
    pygame.K_LEFT: DIRECTIONS['LEFT']
}
    
# Define our main function that will handle our game loop.
def main():
    clock = pygame.time.Clock() # Define clock so we can use FPS to control the speed of our game loop
    running = True # This boolean will be used to tell us when the game loop should end
    renderer.draw() # Draw the initial frame
    while running:
        clock.tick(FPS) # Controls the speed of our game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check for keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key in ACTION_KEYS:
                    controller.enqueue(ACTION_KEYS[event.key]) # If a direction key was pressed, add that action to the controller queue

        handle_snake(snake, board, controller, head_dir, game_over)
        renderer.draw()

    pygame.quit()


if __name__ == "__main__":
    main()