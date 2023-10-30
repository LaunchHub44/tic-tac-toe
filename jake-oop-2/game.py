class Game:
    # Initiates the game
    def __init__(self):
        self.board = [None,None,None, None,None,None, None,None,None]

    # Place pieces
    def set_piece(self, x, y, symbol):
        cell = y*3 + x
        self.board[cell] = symbol
    
    # Get cell occupant
    def get_piece(self, x, y):
        cell = y*3 + x
        return self.board[cell]
    
    def is_valid_point(self, x, y):
        viable_x = x
        viable_y = y

        if viable_x >= 0 and viable_x <= 2:
            viable_x = True
        if viable_y >= 0 and viable_y <= 2:
            viable_y = True
        
        if viable_x == True and viable_y == True:
            return True
        else:
            return False
    
    def find_winner(self):
        """
        returns 'O' or 'X' for a winner
        otherwise, returns None
        """
        # Horizontal win
        for idx in range(0, 9, 3):
            if self.board[idx] == self.board[idx+1] == self.board[idx+2]:
                if self.board[idx] == 'X':
                    return 'X'
                elif self.board[idx] == 'O':
                    return 'O'

        # Vertical win
        for idx in range(0, 3):
            if self.board[idx] == self.board[idx+3] == self.board[idx+6]:
                if self.board[idx] == 'X':
                    return 'X'
                elif self.board[idx] == 'O':
                    return 'O'
        
        # Diagonal win
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

        # No winner
        return None
    
    def display(self):
        """
        write print
        """
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:])