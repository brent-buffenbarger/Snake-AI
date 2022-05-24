import numpy as np
from constants import *

board = np.zeros((NUM_ROWS, NUM_COLS)) # 2D array of integers ranging from 0-3 (see 'tiles' dictionary)

def set_tile(row, col, state):
    if 0 <= state <= 3:
        board[row][col] = state
    else:
        print(f'{state} is an invalid state for a board tile.')