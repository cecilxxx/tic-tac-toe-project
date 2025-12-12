# tic_tac_toe.py
def display_board(board):
    """Print the board. `board` is a list of 9 strings (either "1"-"9" or "X"/"O")."""
    h_line = "---+---+---"
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(h_line)
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(h_line)
    print(f" {board[6]} | {board[7]} | {board[8]}")


def make_move(board, position, symbol):
    """
    Try to place `symbol` ("X" or "O") at `position` (1-9) on `board`.
    Returns True if the move succeeded, False otherwise.
    """
    if position < 1 or position > 9:
        print("Invalid position. Choose a number from 1 to 9.")
        return False

    index = position - 1  # convert human number (1-9) to list index (0-8)

    if board[index] in ("X", "O"):
        print("Field already taken. Choose a different one.")
        return False

    board[index] = symbol
    return True


def switch_player(current_player):
    """Return the other player symbol."""
    return "O" if current_player == "X" else "X"


def input_position(board, current_player):
    """
    Prompt the current player for a position.
    Validates input and returns an integer position (1-9).
    """
    while True:
        raw = input(f"Player {current_player}, choose a position (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        position = int(raw)
        if position < 1 or position > 9:
            print("Position must be between 1 and 9.")
            continue

        index = position - 1
        if board[index] in ("X", "O"):
            print("That square is already taken. Choose another.")
            continue

        return position


def check_winner(board, symbol):
    """Return True if `symbol` has a winning combination on `board`."""
    winning_combi = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in winning_combi:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def check_draw(board):
    """Return True if the board is full (all cells are 'X' or 'O') and no winner."""
    return all(cell in ("X", "O") for cell in board)


def choose_symbols():
    """Ask player 1 to pick X or O and return (player1_symbol, player2_symbol)."""
    while True:
        print("Player 1 please choose symbol X or O:")
        sym = input().strip().upper()
        if sym in ("X", "O"):
            return (sym, "O" if sym == "X" else "X")
        print("Invalid choice. Enter X or O.")


def play_round():
    """Play a single round of tic-tac-toe. Returns True if player wants another round."""
    # initialize board with numbers 1-9 for empty cells
    board = [str(i) for i in range(1, 10)]

    # choose symbols
    player_symbol_1, player_symbol_2 = choose_symbols()
    print(f"Player 1 is {player_symbol_1}, Player 2 is {player_symbol_2}.")

    # player 1 starts
    current_player = player_symbol_1
    winner = None

    while True:
        display_board(board)
        pos = input_position(board, current_player)
        moved = make_move(board, pos, current_player)
        if not moved:
            # should not happen because input_position already validates, but keep safe
            continue

        # check for win
        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} has won!")
            winner = current_player
            break

        # check for draw
        if check_draw(board):
            display_board(board)
            print("The game is a draw.")
            break

        # switch turn
        current_player = switch_player(current_player)

    # ask for another round
    while True:
        again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if again in ("yes", "y"):
            return True
        if again in ("no", "n"):
            return False
        print("Please answer yes or no.")


if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    while True:
        play_again = play_round()
        if not play_again:
            print("Thank you for playing. Goodbye!")
            break