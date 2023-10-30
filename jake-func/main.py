import os
import sys

def playerSetup() -> (str, str):
    p1_sym = input("Player 1: X or O? ")
    p2_sym = None

    if p1_sym.upper() == 'X':
        p2_sym = 'O'
    elif p1_sym.upper() == 'O':
        p2_sym == 'X'
    
    return (p1_sym, p2_sym)

def convert2idx(x,y):
    """
    return a converted index from (x,y)
    this index can be directly used for board

    return None for error.
    """
    if x > 2 or x < 0:
        return None
    if y > 2 or y < 0:
        return None

    point = 3*y + x
    return point

def convert2XY(idx):
    """
    return board index based on (x,y)
    return None for invalid index.
    """
    if idx > 8 or idx < 0:
        return None   
    return (idx%3, idx//3)
    

def setPosition(board, sym, x:int, y:int):
    """
    It should place a piece at a certain position.
    Return None as error value.
    Otherwise, return the symbol.
    """
    if board[ convert2idx(x,y) ] is not None:
        # cell is taken!
        return None

    board[ convert2idx(x,y) ] = sym
    return sym

def findWinner(board):
    """
    It should return 'O' if 'O' player made 3 in a row.
    It should return 'X' if 'X' player won.
    Otherwise return None
    """

    # Horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            if board[i] is not None:
                return board[i]
    
    # Vertical
    for i in (0,1,2):
        if board[i] == board[i+3] == board[i+6]:
            if board[i] is not None:
                return board[i]
    
    # Diagonal
    if board[0] == board[4] == board[8]:
        if board[4] is not None:
            return board[4]
    if board[2] == board[4] == board[6]:
        if board[4] is not None:
            return board[4]

    # Otherwise
    return None

def printBoard(board):
    print(board[:3])
    print(board[3:6]     )
    print(board[6:])

if __name__ == '__main__':
    p1_sym, p2_sym = playerSetup()
    board = []
    for i in range(0,9):
        board.append(None)
    
    round=0
    while findWinner(board) == None:
        curSymbol = p1_sym
        if round %2 == 1:
            curSymbol = p2_sym

        x = int(input(f"{curSymbol}, enter an X coordinate. "))
        y = int(input("Now, enter a Y coordinate. "))
        if setPosition(board, curSymbol, x,y) == None:
            print(f"Error")
            continue

        printBoard(board)

        round += 1
        if round >= 9:
            print("Draw!")
            sys.exit(0)
    
    print(f"{findWinner(board)} wins!")