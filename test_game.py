from tictactoe.game import new_board, place, winner, is_full

def test_empty_board_no_winner():
    b = new_board()
    assert winner(b) is None
    assert not is_full(b)

def test_row_win():
    b = new_board()
    place(b,0,0,'X'); place(b,0,1,'X'); place(b,0,2,'X')
    assert winner(b) == 'X'

def test_col_win():
    b = new_board()
    place(b,0,1,'O'); place(b,1,1,'O'); place(b,2,1,'O')
    assert winner(b) == 'O'
