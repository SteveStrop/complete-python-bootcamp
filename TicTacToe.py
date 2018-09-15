import random


class Game:
    def __init__(self):
        self.players = None
        self.tokens = ('X', 'O', ' ')  # (player 1 marker, player 2 marker, empty square marker)
        self.starting_player = None  # index number of starting player 0 or 1
        self.current_player = None  # index number of current player 0 or 1
        self.board = None
        self.winner = None
        self.over_message = None

    @staticmethod
    def print_instructions():

        instructions = (
            'To play enter your names when asked.',
            'Use the number keys to enter your moves:\n'
            '7|8|9',
            '-+-+-',
            '4|5|6',
            '-+-+-',
            '1|2|3'
        )
        clear_screen()
        for line in instructions:
            print(line)

    def flip_for_start(self):
        input(f'{self.players[0]}, press a key to toss for start')
        flip = random.randint(0, 1)
        if flip == 1:
            print(f"Tails you loose.It's {self.players[1]}'s go.")
        else:
            print(f'Heads you win! You go first {self.players[0]}.')
        input('Press any key to continue')
        return flip


def init_round(g):
    if g.players is None:
        g.players = get_player_names()
        g.starting_player = g.flip_for_start()
    g.starting_player = int(not g.starting_player)
    g.current_player = g.starting_player
    g.board = ['|'] + [g.tokens[2]] * 9  # | is a placeholder and cannot be used as a blank square marker
    clear_screen()
    draw_board(g.board)
    return g


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
    pass
    print('\n' * 100)


def check_winner(board, token):
    """Checks for winning lines in tic tac toe.
    Returns 1 if a winning line found
    Returns 0 if no winning lines
    Returns -1 if stalemate
    @:param token: integer index of character to check against
    @:param board: 10 element list, elements 1-9 represent tic tac toe board"""
    # get character used as an empty square (usually X or O)
    blank = game.tokens[2]
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


def is_number(n):
    if n.isnumeric():
        return int(n)
    print(f'{n} is not a number!')
    return False


def in_range(n):
    if n in range(0, 10):
        return n
    print(f'{n} is out of range. Try a number from 1 to 9')
    return False


def is_space(board, position, space=' '):
    """ @:param: space: character to use as a space default is ' ' """
    if board[position] == space:
        return position
    print("Sorry, that square is already taken!")
    return False


def get_move(board,player):
    player = game.players[player]
    num = ''
    first_loop = True
    while not num:
        # set prompt string
        if first_loop:
            prompt = f"Ok {player}, your turn...\n"  # first time only
        else:
            prompt = "Try again...\n"   # if looped at least once already
        first_loop = False
        # get number input
        num = input(prompt)
        # check is a number
        num = is_number(num)
        if not num:
            continue
        # check num is in range
        num = in_range(num)
        if not num:
            continue
        # check square available
        num = is_space(board, num, game.tokens[2])
        if not num:
            continue
    return num


def play_move(board, position, token):
    board[position] = token
    clear_screen()
    draw_board(board)
    return board


def game_over(message):
    print(message[1] * 50)
    print(message[0].center(50, message[1]))
    print(message[1] * 50)


if __name__ == '__main__':
    game = Game()
    game.print_instructions()
    # loop until user quits
    while input("\n\n\nReady to play? (y/n)") != 'n':
        init_round(game)
        # loop until a winner or stalemate
        while game.winner != 1:
            # alternate player each turn
            game.current_player = int(not game.current_player)
            # get current_player player's move
            move = get_move(game.board, game.current_player)
            # update board with latest move
            board = play_move(game.board, move, game.tokens[game.current_player])
            # check for a winner (or draw)
            winner = check_winner(game.board, game.tokens[game.current_player])
            if winner == -1:  # we have a draw
                game.over_message = (f' Oh shame! A draw ', '-')
                break
            elif winner == 1:  # we have a winner
                game.over_message = (
                    f" Congratulations {game.players[game.current_player]}!! You're the winner ", '*')
                break
            # no winner or draw so loop:
            continue
        game_over(game.over_message)
    print('Bye!')
