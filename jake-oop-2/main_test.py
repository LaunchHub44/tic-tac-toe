import pytest
import tic_tac_toe_2

def test_validate_input():
    assert  tic_tac_toe_2.validate_input("1", "1") == (1,1)
    assert tic_tac_toe_2.validate_input("2", "1") == (2,1)
    assert tic_tac_toe_2.validate_input("3", "1") == None


