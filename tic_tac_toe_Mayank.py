# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def create_board():
    return [" " for i in range(9)]


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    return

print("Current Board positions")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

def is_valid_move(board, position):
    if position < 1 or position > 9:
        print("Wrong Entry!, Please enter from 1 to 9.")
        return False
    index = position -1
    if board[index] != " ":
        print("The block is already filled. Please choose another.")
        return False

    return True


def make_your_choice():
    name1 = input("Player 1, Please Enter your name: ")
    name2 = input("Player 2, Please Enter your name: ")
    while True:
        choice = input("Please choose one of the following: X or O")
        
        if choice == "X":
            print(f"{name1} is X, {name2} is O.")
            return choice
        elif choice == "O":
            print(f"{name1} is O, {name2} is X.")
            return choice
        else:
            print("Invalid choice. Please enter X or O.")



def make_move(board,player,position):
    print(f"{player} is making a move.")
    index = position -1
    board[index] = player
    return

def check_winner(board,player):
    winnings = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]
    for a, b, c in winnings:
        if board[a] == board[b] == board[c] == player:
            print(f"Congratulations! {player} has won.")
            return True
        
    return False

def is_draw(board):
    result = " " not in board
    return result

def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"
    


def play_game():
    print("Welcome to Jungle and let's play Tic-Tac-Toe!")
    

    board = create_board()
    current_player =  make_your_choice()
    
    while True:
        print_board(board)

        move = int(input(f"Player {current_player}, please enter your move from 1 to 9: "))
        position = move
        if not is_valid_move(board,position):
            continue

        make_move(board, current_player, position)

        if check_winner(board, current_player):
            print_board(board)
            break
        current_player = switch_player(current_player)
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Tic-tac-toe game
if __name__ == "__main__":
    play_game()
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
