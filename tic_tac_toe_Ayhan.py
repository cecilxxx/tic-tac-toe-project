player1 = set()
player2 = set()
winning_sets = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
run = True
win = False
draw = False


# 1 2 3
# 4 4 6
# 7 8 9

def check_winning(player1,player2,winning_set,win):
    for winning_set in winning_sets:
        if winning_set.issubset(player1) == True:
            print('Player 1 has wo! Congratulations!')
            win = True
            return win
        elif winning_set.issubset(player2) == True:
            print('Player 2 has won! Congratulations!')
            win = True
            return win


def check_draw(player1,player2,draw):
    union_of_players = player1.union(player2)
    if union_of_players == {1,2,3,4,5,6,7,8,9}:
        print('The Game is over because the board is full')
        draw = True
    return draw


def print_board(player1,player2,player1_symb,player2_symb):
    board_list = [1,2,3,4,5,6,7,8,9]
    for x in player1:
        board_list[x-1] = player1_symb
    for x in player2:
        board_list[x-1] = player2_symb
    print("- - - - - - - - - -")
    print("- ", board_list[0], " - ", board_list[1], " - ", board_list[2], " -")
    print("- - - - - - - - - -")
    print("- ", board_list[3], " - ", board_list[4], " - ", board_list[5], " -")
    print("- - - - - - - - - -")
    print("- ", board_list[6], " - ", board_list[7], " - ", board_list[8], " -")
    print("- - - - - - - - - -")


def player_move(player,numner_player,non_playing_player):
    stop = False
    while stop == False:
        stop1 = False
        while stop1 == False:
            phrase_move = 'Player ' + str(numner_player) + ' make your move:'
            fieldchar = input(phrase_move)
            if (fieldchar in {'1','2','3','4','5','6','7','8','9'}) == True:
                field = int(fieldchar)
                stop1 = True
            else:
                print('You need to type a number between 1 and 9')
                

        occupied_fields = player.union(non_playing_player)
        if (field in occupied_fields) == False:
            player.add(field)
            stop = True
            return player
        else:
            print('This field is occupied. Try again.')



def start_game():
    print('Welcome to our Tic Tac Toe Game.')
    print('The fields are represented by numbers and if a player wants to occupy a field they types in the respective number.')
    stop_sym = False
    while stop_sym == False:
        player1_symb = input('Player 1 choose between X and Y: ')
        if player1_symb == 'X':
            player2_symb = 'Y'
            print('Player 2 your symbol is then Y')
            stop_sym = True
        elif player1_symb == 'Y':
            player2_symb = 'X'
            print('Player 2 your symbol is then X')
            stop_sym= True
        else:
            print('Invalid choice Player 1! Try again')
    return player1_symb,player2_symb
    

player1_symb,player2_symb = start_game()
while run:
    print_board(player1,player2,player1_symb,player2_symb)
    player_move(player1,1,player2)
    draw = check_draw(player1,player2,draw)
    if draw == True:
        break
    win = check_winning(player1,player2,winning_sets,win)
    if win == True:
        break
    print_board(player1,player2,player1_symb,player2_symb)
    player_move(player2,2,player1)
    draw = check_draw(player1,player2,draw)
    if draw == True:
        break
    win = check_winning(player1,player2,winning_sets,win)
    if win == True :
        break
    