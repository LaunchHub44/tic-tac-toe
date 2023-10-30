import game

# We can test this!
def validate_input(x:str, y:str) -> (int, int):
    ix = int(x)
    iy = int(y)
    
    # TODO: replace "True" to some meaningful validation logic.
    if 0 <= ix <= 2 and 0 <= iy <=2:
        return( int(x), int(y))
    else:
        return None

# We can't test functions with "input()" statement.
def get_input() -> (int, int):
    x = int(input("Player 1, set your X coordinate: "))
    y = int(input("Player 1, set your Y coordinate: "))

    return validate_input(x,y)    

def main():
    p1_piece = None
    p2_piece = None
    game_won = None

    while p1_piece != 'X' and p1_piece != 'O':
        p1_piece = input("Player 1: X or O? ")
        if p1_piece.upper() != 'X' and p1_piece.upper() != 'O':
            print(f"{p1_piece} is not a valid symbol.")
        p1_piece = p1_piece.strip()
        p1_piece = p1_piece.upper()

    if p1_piece.upper() == 'X':
        p2_piece = 'O'
    elif p1_piece.upper() == 'O':
        p2_piece = 'X'
    print(f"Player 2 is {p2_piece}")

    play = game.Game()

    current_player = p1_piece

    # Loop condition, (if winner is not found)
    while game_won == None:
        if current_player == p1_piece:
            p1_x, p1_y = get_input()

            if play.is_valid_point(p1_x, p1_y) == True:
                play.set_piece(p1_x, p1_y, p1_piece)
                play.display()
                game_won = play.find_winner()
                if game_won != None:
                    break
                current_player = p2_piece
            else:
                print("Invalid coordinates")
                continue
        
        if current_player == p2_piece:
            p2_x, p2_y = get_input()

            if play.is_valid_point(p2_x, p2_y):
                play.set_piece(p2_x, p2_y, p2_piece)
                play.display()
                game_won = play.find_winner()
                if game_won != None:
                    break

                current_player = p1_piece
            else:
                print("Invalid coordinates")
                continue
    
    print(f"{game_won} wins!")

if __name__ == '__main__': 
    main()