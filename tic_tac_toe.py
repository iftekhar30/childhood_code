def draw_board(back_board):
    print(f"-{back_board[0]}-|-{back_board[1]}-|-{back_board[2]}")
    print(f"-{back_board[3]}-|-{back_board[4]}-|-{back_board[5]}")
    print(f"-{back_board[6]}-|-{back_board[7]}-|-{back_board[8]}")
    return ""


def win(back_board, sign, user):
        win = False 
        back_board[user] = sign
    
        front_board = draw_board(back_board)

        print(front_board)
        for i in range(3):
            if back_board[i*3:i*3+3] == [sign, sign, sign]:
                print(f"{sign} won")
                win = True

        for i in range(3):
            if [back_board[i], back_board[i+3], back_board[i+2*3]] == [sign, sign, sign]:
                print("X won")
                win = True

        if [back_board[0], back_board[4], back_board[8]] == [sign, sign, sign]:
                print("X won")
                win = True
        elif [back_board[2], back_board[4], back_board[6]] == [sign, sign, sign]:
                print("X won")
                win = True

        return win


def is_draw(board):
    draw = True
    for i in board:
        if i in "012345678":
            draw = False

    return draw


def play_game():
    back_board = [
    '0','1','2',
    '3', '4', '5',
    '6', '7', '8'
    ]  
    con = True
    players = ["X", "Y"]
    current = players[0]
    while con:
        try:
            print("Choose position 0-8")
            pos = int(input(f"{current}: "))
            if back_board[pos] in "012345678":
                if win(back_board, current, pos):
                    con = False
                    break
                elif is_draw(back_board):
                    print("Draw")
                    con = False
                    break
                if current == players[0]:
                    current = players[1]
                else:
                    current = players[0]
            else:
                print("Position taken")

        except:
             print("Invalid input")


print(play_game())
