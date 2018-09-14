import random


def init():
    state = dict(players=[],
                 tokens=('X', 'O', '%'),  # (player 1 marker, player 2 marker, empty square marker)
                 starting_player=1)
    return state


def init_round(state):
    if not state['players']:
        state['players'] = get_player_names()
        state['starting_player'] = flip_for_start(state['players'])
    state['starting_player'] = int(not state['starting_player'])
    state['current_player'] = state['starting_player']
    state['board'] = ['|'] + [state['tokens'][2]] * 9  # | is a placeholder and cannot be used as a blank square marker
    state['result'] = 0
    state['game_over_message'] = ''
    clear_screen()
    return state


def flip_for_start(players):
    input(f'Hit any key to flip to start {players[0]}')
    flip = random.randint(0, 1)
    if flip == 0:
        print(f"Tails you loose.It's {players[1]}'s go.")
    else:
        print(f'Heads you win! You go first {players[0]}.')

    input('Hit any key to start')
    return flip


def print_instructions():
    clear_screen()
    instructions = (
        'To play enter your names when asked.',
        'Use the number keys to enter your moves:\n'
        '7|8|9',
        '-+-+-',
        '4|5|6',
        '-+-+-',
        '1|2|3'
    )
    for line in instructions:
        print(line)


def draw_board(board):
    """takes a length 10 list and displays elements 1-9 as a tic tac toe board.
    @:param board: 10 element list"""
    top_row = \
        f'\t {board[7]} | {board[8]} | {board[9]} '
    middle_row = \
        f'\t {board[4]} | {board[5]} | {board[6]} '
    bottom_row = \
        f'\t {board[1]} | {board[2]} | {board[3]} '
    verticals = '\t   |   |     '
    middles = '\t---+---+---'
    print(f'\n\n{verticals}\n{top_row}\n{middles}\n{middle_row}\n{middles}\n{bottom_row}\n{verticals}')
    print('\n' * 2)


def clear_screen():
    print('\n' * 100)


def get_result(board, token):
    """Checks for winning lines in tic tac toe.
    Returns 1 if a winning line found
    Returns 0 if no winning lines
    Returns -1 if stalemate
    @:param token: integer index of character to check against
    @:param board: 10 element list, elements 1-9 represent tic tac toe board"""
    # get character to check (usually X or O)
    token = app['tokens'][token]
    blank = app['tokens'][2]
    winning_lines = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
    # create a list of elements from board corresponding to each winning line and compare to a winning line of token
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == token:
            return 1
    # no winner so check for draw
    if blank not in board:
        return -1  # it's a draw
    # no draw
    return 0  # still playing


def get_player_names():
    """Gets user names for player one two"""
    players = []
    for i in range(2):
        inpt = input(f'Please enter you name Player {i+1}:\n')
        if inpt.strip() == '':
            inpt = f'Player {i+1}'  # default is Player 1 or 2
        players.append(inpt)
    return players


def get_int(string):
    """Returns integer value of string or zero if string not a number"""
    try:
        num = int(string)
        return num
    except ValueError:
        return 0


def is_space(board, position, space=' '):
    """ @:param: space: character to use as a space default is ' ' """
    return board[position] == space


def get_move2(board, player):
    player = app['players'][player]
    inpt = 0

    # loop while input is not in an empty square
    while board[inpt] != app['tokens'][2]:  #
        # get number input
        while not inpt:
            inpt = (input(f"Ok {player}, your turn...\n"))
            while not inpt:
                inpt = get_int(inpt)
            if not inpt:
                print("That's not a number! Try again.")
        # check number is valid
        while not (inpt in range(1, 10)):
            try:
                inpt = int((input('oops! Try again\n')))
            except ValueError:
                pass
        # return move if square is empty
    if board[inpt] == app['tokens'][2]:  #
        return inpt
        # else loop until it is
    while board[inpt] != app['tokens'][2]:  #
        try:
            inpt = int(input(f"Sorry {player}, that square is already taken!\nTry again...\n"))
        except ValueError:
            pass
    return inpt


def get_move(board, player):
    player = app['players'][player]
    inpt = 0
    print(board)
    print(f"board[inpt] = {board[inpt]}, token = {app['tokens'][2]}")
    # loop while input is not in an empty square
    while board[inpt] != app['tokens'][2]:  #
        # loop until number
        while not inpt:
            try:
                inpt = int((input(f"Ok {player}, your turn...\n")))
            except ValueError:
                print("That's not a number! Try again.")
        # check number is valid
        while not (inpt in range(1, 10)):
            try:
                inpt = int((input('oops! Try again\n')))
            except ValueError:
                pass
        # return move if square is empty
        if board[inpt] == app['tokens'][2]:  #
            return inpt
        # else loop until it is
        while board[inpt] != app['tokens'][2]:  #
            try:
                inpt = int(input(f"Sorry {player}, that square is already taken!\nTry again...\n"))
            except ValueError:
                pass
    return inpt


def play_move(board, position, token):
    board[position] = token
    return board


def game_over(message):
    for _ in range(3):
        print(message[1] * 50)
    print(message[0].center(50, message[1]))
    for _ in range(3):
        print(message[1] * 50)


if __name__ == '__main__':
    app = init()
    print_instructions()
    # loop until user quits
    while input("\n\n\nReady to play? (y/n)") != 'n':
        app = init_round(app)
        # loop until a winner or stalemate
        while app['result'] != 1:
            # alternate player each turn
            app['current_player'] = int(not app['current_player'])
            # get current_player player's move
            move = get_move(app['board'], app['current_player'])
            # update board with latest move
            board = play_move(app['board'], move, app['tokens'][app['current_player']])
            clear_screen()
            draw_board(app['board'])
            # check for a winner (or draw)
            result = get_result(app['board'], app['current_player'])
            if result == -1:  # we have a draw
                app['game_over_message'] = (f' Oh shame! A draw ', '-')
                break
            elif result == 1:  # we have a winner
                app['game_over_message'] = (
                    f" Congratulations {app['players'][app['current_player']]}!! You're the winner ", '*')
                break
        game_over(app['game_over_message'])
    print('Bye!')
