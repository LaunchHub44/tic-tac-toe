import pytest
from tictactoe import TicTacToe     # This will help naming short.

def test_init():
    t = TicTacToe()
    assert len(t.board) == 9
    assert None in t.board

def test_init_negative():
    t = TicTacToe()
    assert "O" not in t.board

def test_set_piece():
    t = TicTacToe()
    t.set_piece( 0,1, 'X')      # We are setting 'X' to (0,1)
    assert t.board[1] == 'X'    # (0,1) should be index 1

def test_set_piece_exception():
    t = TicTacToe()
    with pytest.raises(IndexError):
        t.set_piece(-1,1,'X')
    with pytest.raises(IndexError):
        t.set_piece(0,3,'X')

def test_get_piece_exception():
    t = TicTacToe()
    with pytest.raises(IndexError):
        s1 = t.get_piece(-1,1)
    with pytest.raises(IndexError):
        s2 = t.get_piece(0,3)


def test_get_piece():
    t = TicTacToe()
    # self.board is now ['None', 'None', .... ]

    # Testing (0,1) cell.
    assert t.get_piece(0,1) == None   # (0,1) was initialized with None.
    t.set_piece(0,1, 'O')
    assert t.get_piece(0,1) == 'O'    # After I set, value must change.

    # Testing (2,1) cell.
    assert t.get_piece(2,1) == None
    t.set_piece(2,1, 'X')
    assert t.get_piece(2,1) == 'X'

def test_winner_horizontal():
    t = TicTacToe()
    t.board[0] = 'O'
    t.board[1] = 'O'
    t.board[2] = 'O'
    #  board is [ O, O, O, None, None ...]
    #
    #  O O O
    #  . . .
    #  . . .
    assert t.winner() == 'O'

def test_winner_vertical():
    t = TicTacToe()
    t.board[1] = 'X'
    t.board[4] = 'X'
    t.board[7] = 'X'
    #
    #  . X .
    #  . X .
    #  . X .
    assert t.winner() == 'X'

def test_winner_diag():
    t = TicTacToe()
    t.board[0] = 'O'
    t.board[4] = 'O'
    t.board[8] = 'O'
    assert t.winner() == 'O'

    t = TicTacToe()
    t.board[2] = 'X'
    t.board[4] = 'X'
    t.board[6] = 'X'
    assert t.winner() == 'X'

    t = TicTacToe()
    t.board[0] = 'O'
    assert t.winner() == None

def test_winner_negative():
    t = TicTacToe()
    t.board[1] = 'O'
    t.board[2] = 'O'
    t.board[3] = 'O'

    #  . O O
    #  O . .
    #  . . . 
    assert t.winner() == None    

