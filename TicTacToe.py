def init_round(state):
    if not state['players']:
        state['players'] = get_player_names()
    state['starting_player'] = int(not state['starting_player'])
    state['current_player'] = state['starting_player']
    state['board'] = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    state['result'] = 0
    return state


def init():
    state = {}
    state['players'] = []
    state['tokens'] = ('X', 'O')
    state['starting_player'] = 0
    return state


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
    """takes a 3x 3 matrix and displays it as a tic tac toe board"""
    clear_screen()
    top_row = f'\t {board[7]} | {board[8]} | {board[9]} '
    middle_row = f'\t {board[4]} | {board[5]} | {board[6]} '
    bottom_row = f'\t {board[1]} | {board[2]} | {board[3]} '
    verticals = '\t   |   |     '
    middles = '\t---+---+---'
    print(f'\n\n{verticals}\n{top_row}\n{middles}\n{middle_row}\n{middles}\n{bottom_row}\n{verticals}')
    print('\n' * 2)


def clear_screen():
    print('\n' * 100)


def get_result(board, token):
    """Returns 1 if a winning line found
    Returns 0 if no winning lines
    Returns -1 if stalemate"""
    token = app['tokens'][token]
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
    for line in winning_lines:
        for pos in line:
            if board[pos] != token:
                break  # break if no winning token at position: pos in the line
        else:  # checked all elements in a line without breaking so is a winner!!
            return 1  # we have a winner
    if ' ' not in board:
        return -1  # it's a draw
    return 0  # still playing


def get_player_names():
    """Gets user input for player one and player two"""
    players = []
    for i in range(2):
        inpt = input(f'Please enter you name Player {i+1}:\n')
        if inpt.strip() == '':
            inpt = f'Player{i}'
        players.append(inpt)
        clear_screen()
    return players


def validate_num(str):
    if str.isnumeric():
        return str
    return -1


def get_move(board, player):
    player = app['players'][player]
    inpt = 0
    while board[inpt] != ' ':
        inpt = int(validate_num(input(f"Ok {player}, your turn...\n")))
        while not (inpt in range(1, 10)):
            inpt = int(validate_num(input('oops! Try again\n')))
        if board[inpt] == ' ':
            return inpt
        inpt = int(validate_num(
            input(f"Sorry {player}, that square is already taken!\nTry again...\n")))
    return inpt


def play_move(board, move, token):
    board[move] = token
    return board


def end_message(message):
    for _ in range(3):
        print(message[1] * 50)
    print(message[0].center(50, message[1]))
    for _ in range(3):
        print(message[1] * 50)


if __name__ == '__main__':
    app = init()
    print_instructions()
    while input("\n\n\nReady to play? (y/n)") == 'y':
        app = init_round(app)
        draw_board(app['board'])
        # loop until a winner or stalemate
        while app['result'] != 1:
            # alternate current_player player each turn
            app['current_player'] = int(not app['current_player'])
            # get current_player player's move
            move = get_move(app['board'], app['current_player'])
            # update board with latest move
            board = play_move(app['board'], move, app['tokens'][app['current_player']])
            draw_board(app['board'])
            result = get_result(app['board'], app['current_player'])
            if result == -1:  # we have a draw
                message = (f' Oh shame! A draw ', '-')
                break
            elif result == 1:
                message = (f" Congratulations {app['players'][app['current_player']]}!! You're the winner ", '*')
                break

        end_message(message)
