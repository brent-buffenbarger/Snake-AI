from random import randint

class Apple:
    def __init__(self, board):
        self.x_pos = None
        self.y_pos = None
        self.board = board
    
    def spawn(self):
        row = randint(0, len(self.board.TILES) - 1)
        col = randint(0, len(self.board.TILES[0]) - 1)
        tile = self.board.TILES[row][col]
        self.x_pos = tile.x_pos
        self.y_pos = tile.y_pos