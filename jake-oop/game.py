import random

class Board:
    
    # Python constructor looks weird:
    def __init__(self):       # Same as  `public Athlete() {...}`
        self.board = [ None,None,None, None,None,None, None,None,None ]

    def set_piece(self, x, y, symbol):
        """
        assumption:  x,y are valid coordinate:  0,1, or 2.
        """
        idx = 3*y + x
        self.board[idx] = symbol

    def get_piece(self, x,y ):
        """
        assumption:  x,y are valid coordinate:  0,1, or 2.
        should return self.board[idx] relative to (x,y) pair.
        """
        idx = 3*y + x
        return self.board[idx]
    
    def get_random_valid_point(self):
        """
        should return (x,y) pair, where the point is playable.
        otherwise, return None
        """
        x = random.randint(0,2)
        y = random.randint(0,2)
        count = 0
        while not self.is_valid_point(x,y):
            count +=1
            x = random.randint(0,2)
            y = random.randint(0,2)
            if count > 20:
                return None
        return (x,y)

    def is_valid_point(self, x,y):
        """
        should return True or False.
        if (x,y) pair is a valid point, return True
        otherwise return False
        """
        valid_x = None
        valid_y = None

        if x >= 0 and x <= 2:
            valid_x = True
        if y >= 0 and y <= 2:
            valid_y = True
        
        if valid_x == True and valid_y == True:
            idx = 3*y + x
            if self.board[idx] == None:
                return True
            else:
                return False
        else:
            return False
        
    def is_valid_piece(self, symbol) -> bool:
        """
        should return True or False
        if symbol is x,X or o,O, return True
        otherwise, return False.
        """

        if symbol.upper() == 'X' or symbol.upper() == 'O':
            return True
        else:
            return False

    def get_winner(self) -> str:
        """
        should return 'O' or 'X', if the player wins the game.
        otherwise, return None
        """

        # vertical check
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2]:
                if self.board[i] == 'X':
                    return 'X'
                elif self.board[i] == 'O':
                    return 'O'
        
        # horizontal check
        for i in range(0, 2):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                if self.board[i] == 'X':
                    return 'X'
                elif self.board[i] == 'O':
                    return 'O'

        # diagonal check
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board[4] == 'X':
                return 'X'
            elif self.board[4] == 'O':
                return 'O'
        elif self.board[2] == self.board[4] == self.board[6]:
            if self.board[4] == 'X':
                return 'X'
            elif self.board[4] == 'O':
                return 'O'

        return None
    
    def display(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:])
        print("-----")
