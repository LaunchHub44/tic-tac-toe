import os      # https://docs.python.org/3/library/os.html 
import sys     # https://docs.python.org/3/library/sys.html
import game
import random

def main():
    tg = game.Board()

    # Determine number of players
    #   NOTE:  not robust enough.  So, invalid input will be 1 player
    #
    # TODO: Make it robust
    #
    players = int(input("How many players? "))
    if players <= 1:
        players = 1
    elif players >= 2:
        players = 2
    
    # TODO: Choose symbol
    sym = 'O'

    while True:
        x = None
        y = None

        x = input(f"Player {sym}, please enter X value: ")
        x = int(x)
        y = input(f"Player {sym}, please enter Y value: ")
        y = int(y)

        if tg.is_valid_point(x,y):
            tg.set_piece(x,y, sym)
            if sym == 'O':
                if players == 1 and tg.get_winner() is None:
                    # Now, 'X' is computer
                    sym = 'X'
                    x,y = tg.get_random_valid_point()
                    tg.set_piece(x,y, sym)
                    sym = 'O'
                else:
                    sym = 'X'
            else:
                sym = 'O'
        else:
            print(f"index is not valid: {x}, {y}")    
        tg.display()

        if tg.get_winner() is not None: 
            print(f'Winner: {tg.get_winner()}')
            sys.exit(0)      # exit on my own



if __name__ == '__main__':
    main()