import os
import sys

class TicTacToe:

    def __init__(self):
        """
        Constructor:
        """
        self.board = [ None,None,None,  None,None,None, None,None,None,]

    def set_piece(self, x, y, piece):
        if x < 0 or x > 2:
            raise IndexError("x coordinate must be between 0 and 2")
        if y < 0 or y > 2:
            raise IndexError("y coordinate must be between 0 and 2")
        
        idx = x*3 + y
        self.board[ idx ] = piece

    def get_piece(self, x, y) -> str:
        if x < 0 or x > 2:
            raise IndexError("x coordinate must be between 0 and 2")
        if y < 0 or y > 2:
            raise IndexError("y coordinate must be between 0 and 2")

        idx = x*3 + y
        return self.board[idx]


    def winner(self) -> str:
        """
        if the board is won for 'X', it will return 'X'
        if the board is won for 'O', it will return 'O'
        if the board is still in progress, it will return None
        """
        # case 1: horizontal
        #   it means:  idx 0,1,2 are same
        #   or  idx 3,4,5 are the same, or idx 6,7,8 are the same 
        for i in range(0,3):
            if self.board[i*3 ] == self.board[i*3 + 1] == self.board[i*3 + 2]:
                if self.board[i*3] is not None:
                    return self.board[i*3]
        # OR
        # for i in range(0,9,3):
        #   if self.board[i] == self.board[i+1] == self.board[i+2]:

        # case 2: vertical
        #   it means:  idx (0,3,6) / (1,4,7) / (2,5,8) is the same.
        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                if self.board[i] is not None:
                    return self.board[i]
        
        # case 3: diagonal
        #   it means: idx (0, 4, 8) or (2, 4, 6)
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board[0] is not None:
                return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6]:
            if self.board[2] is not None:
                return self.board[4]
        
        return None
    
    def print_board(self, turn):
        for i in range(0,9,3):
            print( self.board[i:i+3])
        print(f"--- {turn} ---")
