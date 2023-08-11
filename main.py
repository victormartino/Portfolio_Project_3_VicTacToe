import copy

board = '   |   |   \n' \
        '___________\n' \
        '   |   |   \n' \
        '___________\n' \
        '   |   |   '

board_list = list(board)

r1c1 = 1
r1c2 = 5
r1c3 = 9
r2c1 = 25
r2c2 = 29
r2c3 = 33
r3c1 = 49
r3c2 = 53
r3c3 = 57

possible_choices = {11: r1c1, 12: r1c2, 13: r1c3, 21: r2c1, 22: r2c2, 23: r2c3, 31: r3c1, 32: r3c2, 33: r3c3}
# board_list[r3c3] = "X"

# print("".join(board_list))

example12 = copy.copy(board_list)
example12[r1c2] = "X"
example31 = copy.copy(board_list)
example31[r3c1] = "X"

instructions = (f"\nThis is how you play. First you type the row number (1, 2, 3), then the column number (1, 2, 3),\n"
                f"so if you would like to place your mark on the second column of the first row, just type '12',"
                f"\nwithout quotes,"
                f" and you will get this:\n\n{''.join(example12)}\n\nLikewise, if you would like to place your mark on the "
                f"first row of the third column, \njust type '31', again without quotes, and you will get this:"
                f"\n\n{''.join(example31)}\n\nAre you ready? Let's begin!")

available_choices = copy.copy(possible_choices)
game_board = copy.copy(board_list)


def x_player():
    player_choice = input(f'{player1}: Where would you like to place your X?\n')
    if int(player_choice) not in possible_choices:
        print('Invalid option. Try again.')
        repeat_instructions = input('Would you like to read the instructions again? Type yes or no\n').lower()
        if repeat_instructions == 'yes':
            print(instructions)
        else:
            x_player()
    elif int(player_choice) not in available_choices:
        print('This position already has a mark on it')
        x_player()
    else:
        game_board[available_choices[int(player_choice)]] = 'X'
        del available_choices[int(player_choice)]
        print("".join(game_board))


def o_player():
    player_choice = input(f'{player2}: Where would you like to place your O?\n')
    if int(player_choice) not in possible_choices:
        print('Invalid option. Try again.')
        repeat_instructions = input('Would you like to read the instructions again? Type yes or no\n').lower()
        if repeat_instructions == 'yes':
            print(instructions)
        else:
            o_player()
    elif int(player_choice) not in available_choices:
        print('This position already has a mark on it')
        o_player()
    else:
        game_board[available_choices[int(player_choice)]] = 'O'
        del available_choices[int(player_choice)]
        print("".join(game_board))


def check_winner():
    if game_board[r1c1] == game_board[r1c2] == game_board[r1c3] and game_board[r1c1] != ' ':
        return True
    elif game_board[r2c1] == game_board[r2c2] == game_board[r2c3] and game_board[r2c1] != ' ':
        return True
    elif game_board[r3c1] == game_board[r3c2] == game_board[r3c3] and game_board[r3c1] != ' ':
        return True
    elif game_board[r1c1] == game_board[r2c2] == game_board[r3c3] and game_board[r1c1] != ' ':
        return True
    elif game_board[r1c1] == game_board[r2c1] == game_board[r3c1] and game_board[r1c1] != ' ':
        return True
    elif game_board[r1c2] == game_board[r2c2] == game_board[r3c2] and game_board[r1c2] != ' ':
        return True
    elif game_board[r1c3] == game_board[r2c3] == game_board[r3c3] and game_board[r1c3] != ' ':
        return True
    else:
        return False


print("Hello human, I'm VicTacToe, your new favorite game!")
player1 = input('Player 1, please enter your name:\n').title()
player2 = input('Player 2, please enter your name:\n').title()
read_instructions = input('Would you like to read the instructions? Type "yes" or "no"\n').lower()
if read_instructions == 'yes':
    print(instructions)


keep_going = "yes"
while keep_going == 'yes':
    while len(available_choices) > 0:
        x_player()
        if check_winner():
            print(f'Game over! The winner is {player1}')
            break
        elif len(available_choices) != 0:
            o_player()
            if check_winner():
                print(f'Game over! The winner is {player2}')
                break
    if not check_winner():
        print("It's a draw!")
    keep_going = input('Would you like to play again? Type "yes" or "no"\n').lower()
    if keep_going == 'yes':
        available_choices = copy.copy(possible_choices)
        game_board = copy.copy(board_list)

print("\nThank you for playing VicTacToe. See you next time, I hope you have a great day!")