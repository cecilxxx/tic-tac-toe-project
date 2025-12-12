# Tic-Tac-Toe

board = [" "] * 9


def display_board(board):
    """Prints the current board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def choose_x_o():
    """
    Player 1 chooses X or O.
    Return (player1_symbol, player2_symbol)
    """
    while True:
        choice = input("Player 1, choose your symbol (X or O): ").strip().upper()

        if choice == "X":
            return "X", "O"
        elif choice == "O":
            return "O", "X"
        else:
            print("Invalid choice. Please type X or O.")


def modify_pos(player, position):
    real_position = position - 1

    if board[real_position] != " ":
        print("This position is already occupied.")
        return False

    board[real_position] = player
    return True


def play_turn(player):
    while True:
        pos_str = input(f"{player}, please enter the position you want to mark (1-9): ")

        if not pos_str.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(pos_str)

        if position < 1 or position > 9:
            print("Please enter a number from 1 to 9.")
            continue

        if modify_pos(player, position):
            # the player has chose correctly, needs to be tested
            return


def check_for_win_condition(current_player):
    winning_combos = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6),
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] == current_player:
            return True

    return False


def check_draw():
    return all(cell != " " for cell in board)


def main():
    global board
    board = [" "] * 9
    
    player1, player2 = choose_x_o()
    print(f"Player 1 is {player1}, Player 2 is {player2}\n")

    current_player = player1

    while True:
        display_board(board)
        play_turn(current_player)

        # check win 
        if check_for_win_condition(current_player):
            display_board(board)
            print(f"{current_player} wins! 🎉")
            break

        # check draw
        if check_draw():
            display_board(board)
            print("It's a draw!")
            break

        # switch player
        current_player = player2 if current_player == player1 else player1

            


if __name__ == "__main__":
    main()
