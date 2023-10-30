import random

ttc_grid = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"]
]

def setup():
    # Setup process
    p1_symbol = ""
    p2_symbol = ""

    while p1_symbol.upper() != "X" and p1_symbol.upper() != "O":
        p1_symbol = input("X or O? ")
        if p1_symbol.upper() == "X":
            p2_symbol = "O"
        elif p1_symbol.upper() == "O":
            p2_symbol = "X"
        else:
            print(f"{p1_symbol} is not a valid symbol.")
            p1_symbol = ""
            p2_symbol = ""
    return p1_symbol.upper() , p2_symbol.upper()

def game_won() -> str:
    """
    return value:
       'O'  :  'O' player won
       'X'  :  'X' player won
       None :  Game not finished, yet.
    """
    
    # winning condition 1:  horizontal
    for i in range(0,3):
        if ttc_grid[i][0] == ttc_grid[i][1] == ttc_grid[i][2]:
            if ttc_grid[i][0] != "[ ]":
                return ttc_grid[i][0]
    # winning condition 2:  vertical
    for i in range(0, 3):
        if ttc_grid[0][i] == ttc_grid[1][i] == ttc_grid[2][i]:
            if ttc_grid[0][i] != "[ ]":
                return ttc_grid[0][i]
    
    # winning condition 3:  diagonal
    if ( ttc_grid[0][0] == ttc_grid[1][1] == ttc_grid[2][2]) or ( ttc_grid[2][0] == ttc_grid[1][1] == ttc_grid[0][2]):
        if ttc_grid[1][1] != "[ ]":
            return ttc_grid[1][1]
    
    print("Game is not finished, yet")
    return None     # NULL or null
    

def print_board():
    #for i in range(0,3):
    #    print(ttc_grid[i])

    # How about this??  better?
    for line in ttc_grid:
        print(line)

    print()


def main():
    p1_symbol, p2_symbol = setup()
    print(f"P1: {p1_symbol},  P2: {p2_symbol}")

    # Game
    while game_won() == None:
        x = input("Enter x coordinate: (0-2)")
        y = input("Enter y coordinate: (0-2)")
        x = int(x)
        y = int(y)
        if ttc_grid[x][y] == "[ ]":
            ttc_grid[x][y] = f"[{p1_symbol}]"
        else:
            print("Coordinates occupied")
            continue

        print_board()
        if game_won() != None:
            break

        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while ttc_grid[x][y] != "[ ]":
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        ttc_grid[x][y] = f"[{p2_symbol}]"
    
        print_board()

    # Post-Game
    winner = game_won()
    print(f"Player({winner}) won!")
    print("Bye~~")
    

if __name__ == '__main__':
    main()