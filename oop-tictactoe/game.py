import os, sys
import tictactoe
import random

if __name__ == '__main__':

    board = tictactoe.TicTacToe()
    #   - Java does this:
    #     TicTacToe board = new TicTacToe();

    turn =0
    while board.winner() != 'X' and board.winner() != 'O':
        p1_x = int(input("Set an X coordinate. "))
        p1_y = int(input("Set a Y coordinate. "))
        board.set_piece(p1_x, p1_y, 'O')
        board.print_board(turn)

        turn += 1
        if turn >= 9:
            print("DRAW")
            sys.exit(0)      # If it's draw, exit

        # Study This logic!
        p2_x = p1_x
        p2_y = p1_y
        while board.get_piece(p2_x, p2_y) != None:
            p2_x = random.randint(0,2)
            p2_y = random.randint(0,2)
        board.set_piece(p2_x, p2_y, 'X')
        board.print_board(turn)

        turn += 1

    winner = board.winner()
    print(f"WINNER: {winner}")

    