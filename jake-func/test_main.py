import pytest
import main

def test_convert2idx():
    assert main.convert2idx(0,0) == 0
    assert main.convert2idx(2,2) == 8
    assert main.convert2idx(3,0) == None
    assert main.convert2idx(0,3) == None

def test_convert2XY():
    assert main.convert2XY(0) == (0,0)
    assert main.convert2XY(4) == (1,1)
    assert main.convert2XY(8) == (2,2)
    assert main.convert2XY(3) == (0,1)
    assert main.convert2XY(2) == (2,0)

    assert main.convert2XY(-1) == None
    assert main.convert2XY(9) == None

def test_setPosition():
    board = []
    for i in range(0,9):
        board.append(None)

    assert main.setPosition(board, 'O', 0,0) == 'O'
    assert main.setPosition(board, 'X', 0,0) == None

def test_findWinner():
    def initBoard():
        board = []
        for i in range(0,9):
            board.append(None)
        return board
    
    board = initBoard()
    assert main.findWinner(board) == None
    
    board = initBoard()
    board[0] = 'O'
    board[4] = 'O'
    board[8] = 'O'
    assert main.findWinner(board) == 'O'