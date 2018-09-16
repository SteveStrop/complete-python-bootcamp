import random


class Match:
    def __init__(self):
        self.players = None
        self.starting_player = None  # index number of starting player 0 or 1
        self.current_player = None  # index number of current player 0 or 1


    def print_instructions(self):

        self.clear_screen()
        instructions = (
            'To play, enter your names when asked.',
            'Use the number keys to enter your moves:\n'
            '7|8|9',
            '-+-+-',
            '4|5|6',
            '-+-+-',
            '1|2|3'
        )
        for line in instructions:
            print(line)

    @staticmethod
    def clear_screen():
        pass
        #  print('\n' * 100)

    def flip_for_start(self):
        input(f'{self.players[0]}, press a key to toss for start')
        flip = random.randint(0, 1)
        if flip == 1:
            print(f"Tails you loose.It's {self.players[1]}'s go.")
        else:
            print(f'Heads you win! You go first {self.players[0]}.')
        input('Press any key to continue')
        self.starting_player=flip

    def get_player_names(self):
        """Gets user names for player one two"""
        self.players = []
        for i in range(2):
            inpt = input(f'Please enter you name Player {i+1}:\n')
            if inpt.strip() == '':
                inpt = f'Player {i+1}'  # default is Player 1 or 2
            self.players.append(inpt)


class Game:

    def __init__(self):
        self.tokens = ('X', 'O', ' ')  # (player 1 marker, player 2 marker, empty square marker)
        self.board = ['|'] + [self.tokens[2]] * 9
        self.winner = None
        self.over_message = None

    def draw_board(self):
        """takes a length 10 list and displays elements 1-9 as a tic tac toe board.
        @:param board: 10 element list"""
        top_row = \
            f'\t {self.board[7]} | {self.board[8]} | {self.board[9]} '
        middle_row = \
            f'\t {self.board[4]} | {self.board[5]} | {self.board[6]} '
        bottom_row = \
            f'\t {self.board[1]} | {self.board[2]} | {self.board[3]} '
        verticals = '\t   |   |     '
        middles = '\t---+---+---'
        print(f'\n\n{verticals}\n{top_row}\n{middles}\n{middle_row}\n{middles}\n{bottom_row}\n{verticals}')
        print('\n' * 2)

    def get_move(self, player):
        player = match.players[player]
        num = ''
        first_loop = True
        while not num:
            # set prompt string
            if first_loop:
                prompt = f"Ok {player}, your turn...\n"  # first time only
            else:
                prompt = "Try again...\n"  # if looped at least once already
            first_loop = False
            # get number input
            num = input(prompt)
            # check is a number
            num = self.is_number(num)
            if not num:
                continue
            # check num is in range
            num = self.in_range(num)
            if not num:
                continue
            # check square available
            num = is_space(self.board, num, self.tokens[2])
            if not num:
                continue
        return num

    def check_winner(self, token):
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
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == token:
                return 1
        # no winner so check for draw
        if blank not in self.board:
            return -1  # it's a draw
        # no draw
        return 0  # still playing

    @staticmethod
    def is_number(n):
        if n.isnumeric():
            return int(n)
        print(f'{n} is not a number!')
        return False

    @staticmethod
    def in_range(n):
        if n in range(0, 10):
            return n
        print(f'{n} is out of range. Try a number from 1 to 9')
        return False


def init_game(m):
    if m.players is None:
        m.get_player_names()
        m.flip_for_start()
    m.starting_player = int(not m.starting_player)
    m.current_player = m.starting_player
    b = Game()
    m.clear_screen()
    b.draw_board()
    return b


def is_space(board, position, space=' '):
    """ @:param: space: character to use as a space default is ' ' """
    if board[position] == space:
        return position
    print("Sorry, that square is already taken!")
    return False


def play_move(board, position, token):
    board.board[position] = token
    match.clear_screen()
    board.draw_board()


def game_over(message):
    print(message[1] * 50)
    print(message[0].center(50, message[1]))
    print(message[1] * 50)


if __name__ == '__main__':
    match = Match()
    match.print_instructions()
    # loop until user quits
    while input("\n\n\nReady to play? (y/n)") != 'n':
        game = init_game(match)
        # loop until a winner or stalemate
        while game.winner != 1:
            # alternate player each turn
            match.current_player = int(not match.current_player)
            # get current_player player's move
            move = game.get_move(match.current_player)
            # update board with latest move
            play_move(game, move, game.tokens[match.current_player])
            # check for a winner (or draw)
            winner = game.check_winner(game.tokens[match.current_player])
            if winner == -1:  # we have a draw
                game.over_message = (f' Oh shame! A draw ', '-')
                break
            elif winner == 1:  # we have a winner
                game.over_message = (
                    f" Congratulations {match.players[match.current_player]}!! You're the winner ", '*')
                break
            # no winner or draw so loop:
            continue
        game_over(game.over_message)
    print('Bye!')
