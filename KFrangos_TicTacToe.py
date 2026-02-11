#creating the board
board = ["-","-","-",
         "-","-","-",
            "-","-","-"]
#displaying the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#playing the game
def play_game():
    display_board()
    while True:
        #player 1 turn
        position = input("Player 1, choose a position from 1-9: ")
        board[int(position)-1] = "X"
        display_board()
        #check for win or tie
        if check_win():
            print("Player 1 wins!")
            break
        elif check_tie():
            print("It's a tie!")
            break
        #player 2 turn
        position = input("Player 2, choose a position from 1-9: ")
        board[int(position)-1] = "O"
        display_board()
        #check for win or tie
        if check_win():
            print("Player 2 wins!")
            break
        elif check_tie():
            print("It's a tie!")
            break
#check for win
def check_win():
    #check rows
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    #check columns
    elif board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True
    #check diagonals
    elif board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True
    else:
        return False
    

#check for tie
def check_tie():
    if "-" not in board:
        return True
    else:
        return False
play_game()
