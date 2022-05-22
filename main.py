import pygame
from renderer import Renderer, WIDTH, HEIGHT

# Setup our game window using WIDTH and HEIGHT from renderer.py
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake AI")

# Setup our Renderer to handle all of the drawing
renderer = Renderer(WIN)

# Define FPS to determine how quickly our game updates
FPS = 60

# Define our main function that will handle our game loop.
def main():
    clock = pygame.time.Clock() # Define clock so we can use FPS to control the speed of our game loop
    running = True # This boolean will be used to tell us when the game loop should end
    while running:
        clock.tick(FPS) # Controls the speed of our game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.draw()

    pygame.quit()


if __name__ == "__main__":
    main()