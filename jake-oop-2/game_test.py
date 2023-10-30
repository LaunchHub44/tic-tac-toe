import pytest
import game    # game.py is imported, as name "game"

def test_setPiece():
    tg = game.Game()
    assert tg.board[4] == None
    tg.set_piece(1,1, 'X')
    assert tg.board[4] == 'X'

def test_getPiece():
    tg = game.Game()
    assert tg.get_piece(1,1) == None
    tg.set_piece(1,1, 'O')
    assert tg.get_piece(1,1) == 'O'
    
def test_validPoint():
    tg = game.Game()
    assert tg.board[4] == None
    assert tg.is_valid_point(1,1) == True

def test_winner():
    tg = game.Game()
    
    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(0,0,'X')
    tg.set_piece(1,0,'X')
    tg.set_piece(2,0,'X')
    assert tg.find_winner() == 'X'

    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(1,0,'X')
    tg.set_piece(2,0,'X')
    tg.set_piece(0,1, 'X')
    assert tg.find_winner() == None

    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(0,1,'X')
    tg.set_piece(1,1,'X')
    tg.set_piece(2,1,'X')
    assert tg.find_winner() == 'X'

    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(0,0,'X')
    tg.set_piece(0,1,'X')
    tg.set_piece(0,2,'X')
    assert tg.find_winner() == 'X'

    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(0,0,'X')
    tg.set_piece(1,1,'X')
    tg.set_piece(2,2,'X')
    assert tg.find_winner() == 'X'

    tg.board = [None,None,None, None,None,None, None,None,None]
    tg.set_piece(2,0,'X')
    tg.set_piece(1,1,'X')
    tg.set_piece(0,2,'X')
    assert tg.find_winner() == 'X'