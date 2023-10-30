import pytest
import game

def test_init():
    tg = game.Board()    # this already calls __init__(), which is a constructor
    assert len( tg.board ) != 0
    assert len( tg.board ) == 9

def test_init2():
    tg = game.Board()
    assert tg.board[4] == None

def test_setPiece():
    # Initializing 
    tg = game.Board()

    # checking the pre-condition
    assert tg.get_piece(0,0) == None

    # Action
    tg.set_piece(0,0, 'X')  

    # testing the post-condition
    assert tg.get_piece(0,0) == 'X'

def test_getPiece():
    tg = game.Board()
    assert tg.get_piece(2,1) == None

    tg.set_piece(2,1, 'O')
    assert tg.get_piece(2,1) == 'O'

def test_valid_point():
    tg = game.Board()
    assert tg.is_valid_point(0,0) == True
    assert tg.is_valid_point(1,2) == True

def test_valid_point_taken():
    tg = game.Board()
    tg.board = [None,None,None, None,'X',None, None,None,None]
    assert tg.is_valid_point(1,1) == False
    assert tg.is_valid_point(1,2) == True


def test_valid_point_negative():
    tg = game.Board()
    assert tg.is_valid_point(-1,0) == False
    assert tg.is_valid_point(3,0) == False

def test_InvalidPiece():
    tg = game.Board()
    tg.is_valid_piece('A') == False
    tg.is_valid_piece('x') == True

def test_get_random_point():
    tg = game.Board()
    tg.board = [None, 'x','x', 'o','o','o', 'x','o','x']
    assert tg.get_random_valid_point() == (0,0)

    tg.board = ['x','o','x', 'x','o','o', 'o','x','x']
    assert tg.get_random_valid_point() == None


def test_winner():
    tg = game.Board()
    assert tg.get_winner() == None
    
    tg.board = [None,None,None, 'X','X',None, None,None,None]
    assert tg.get_winner() == None

    tg.board = [None,None,None, 'X','X','X', None,None,None]
    assert tg.get_winner() == 'X'

    tg.board = [None,'O',None, None,'O',None, None,'O',None]
    assert tg.get_winner() == 'O'

    tg.board = ['O',None,None, None,'O',None, None,None,'O']
    assert tg.get_winner() == 'O'

    # Same Case:
    tg.board = [None,None,'X', None,'X',None, 'X', None,None]
    assert tg.get_winner() == 'X'

    tg.board = [None,None,'O', None,'O',None, 'O', None,None]
    assert tg.get_winner() == 'O'

