# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function for displaying the board
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

# Function to check win
def check_win(board, i):
    if ((board[0] == board[1] == board[2]) or
        (board[3] == board[4] == board[5]) or
        (board[6] == board[7] == board[8]) or
        (board[0] == board[3] == board[6]) or
        (board[1] == board[4] == board[7]) or
        (board[2] == board[5] == board[8]) or
        (board[0] == board[4] == board[8]) or
        (board[2] == board[4] == board[6])):
        return True
    return False

# Function to check if cell is already taken
def is_taken(board, num):
    if str(board[num - 1]) in "XO":
        return True
    return False


# Let Player 1 chose symbol
print('Welcome in the tic-tac-toe game!')
while True:
    symbol1 = input("Player 1, choose X or O: ").upper()
    if symbol1 in ["X", "O"]:
        symbol2 = "O" if symbol1 == "X" else "X"
        break
    print("Invalid choice. Please enter X or O.")

print(f'Player 1 chose {symbol1}, Player 2 is assigned {symbol2}')


i = 1
moves = 0

while True:
   print_board()

    # Ask current player for a move
   num = int(input(f"Player {i}, enter a number between 1 and 9: "))
   if 1 <= num <= 9:
        # Check if cell is taken
        if is_taken(board, num):
            print("Cell already taken. Choose another one.")
            continue
        # Place symbol on the board
        board[num - 1] = symbol1 if i == 1 else symbol2
        moves += 1
   else:
        print("Please enter a number from 1 to 9.")
        continue
   
   if check_win(board, i):
        print_board()
        print(f"Congratulations, Player {i}! You won the game.")
        break
 
   # Check for draw
   if moves == 9:
        print_board()
        print("It's a draw!")
        break

    # Switch player
   i = 2 if i == 1 else 1




# Tic-tac-toe game
#if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
 #   print("Welcome to a new round of Tic-Tac-Toe!")


