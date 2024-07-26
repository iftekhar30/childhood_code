def sum(a,b,c):
    return a + b + c
def show_board(x_state, y_state):
    zero = "X" if x_state[0] == 1 else ("O" if y_state[0] == 1 else 0)
    one = "X" if x_state[1] == 1 else ("O" if y_state[1] == 1 else 1)
    two = "X" if x_state[2] == 1 else ("O" if y_state[2] == 1 else 2)
    three = "X" if x_state[3] == 1 else ("O" if y_state[3] == 1 else 3)
    four = "X" if x_state[4] == 1 else ("O" if y_state[4] == 1 else 4)
    five = "X" if x_state[5] == 1 else ("O" if y_state[5] == 1 else 5)
    six = "X" if x_state[6] == 1 else ("O" if y_state[6] == 1 else 6)
    seven = "X" if x_state[7] == 1 else ("O" if y_state[7] == 1 else 7)
    eight = "X" if x_state[8] == 1 else ("O" if y_state[8] == 1 else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"--|--|--")
    print(f" {three} | {four} | {five} ")
    print(f"--|--|--")
    print(f" {six} | {seven} | {eight} ")


def check_win(x_state, y_state):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            return 0
        
        if sum(y_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            return 1  
        
    return 2


print("Welcome to tic tac toe")
x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
while True:
    if turn == 1:
        print("X's turn")
        pos = int(input("Choose a number between 0-8:" ))
        x_state[pos] = 1
        show_board(x_state, y_state)
        if check_win(x_state, y_state) == 0:
            print("X wins")
            break
        turn -= 1
    else:
        print("O's turn")
        pos = int(input("Choose a number between 0-8:" ))
        y_state[pos] = 1
        show_board(x_state, y_state)
        turn += 1
        if check_win(x_state, y_state) == 1:
            print("O wins")
            break
        