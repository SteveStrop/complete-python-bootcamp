import random


class Match:
    def __init__(self):
        self.players = []
        self.starting_player = None
        self.current_player = None

    def print_instructions(self):

        self.clear_screen()
        instructions = (
            'Use the number keys to enter your moves:\n\n'
            '7|8|9',
            '-+-+-',
            '4|5|6',
            '-+-+-',
            '1|2|3\n'
        )
        for line in instructions:
            print(line)

    @staticmethod
    def clear_screen():
        pass
        print('\n' * 100)

    def get_player_names(self):
        """Gets user names for player one two"""
        for i in range(1, 3):
            inpt = input(f'\n\nPlease enter you name Player {i}:\n')
            if inpt.strip() == '':
                inpt = f'Player {i}'  # default is Player 1 or 2
            self.players.append(inpt)

    def flip_for_start(self):
        input(f'\n{self.players[0]}, press a key to see who goes first')
        flip = random.randint(0, 1)
        if flip == 0:
            print(f"It's Tails. {self.players[1]} goes first.")
        else:
            print(f'Heads! You go first, {self.players[0]}.')
        self.starting_player = flip
        self.current_player = flip


class Game(Match):

    def __init__(self):
        Match.__init__(self)
        self.tokens = ('X', 'O', ' ')  # (player 1 marker, player 2 marker, empty square marker)
        self.board = ['|'] + [self.tokens[2]] * 9
        self.winner = None
        self.message = None
        self.print_instructions()
        self.get_player_names()
        self.flip_for_start()

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
        player = self.players[player]
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
            num = self.is_space(num, self.tokens[2])
            if not num:
                continue
        return num

    def play_move(self, position, token):
        self.board[position] = token
        self.clear_screen()
        self.draw_board()

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

    def is_space(self, position, space=' '):
        """ @:param: space: character to use as a space default is ' ' """
        if self.board[position] == space:
            return position
        print("Sorry, that square is already taken!")
        return False

    def over_message(self):
        print(self.message[1] * 50)
        print(self.message[0].center(50, self.message[1]))
        print(self.message[1] * 50)

    def reset(self):
        self.board = ['|'] + [self.tokens[2]] * 9
        self.winner = None
        self.message = None
        self.current_player = int(not self.current_player)


if __name__ == '__main__':
    game = Game()

    # loop until user quits
    while input("\n\n\nReady to play? (y/n)") != 'n':

        game.draw_board()
        # loop until a winner or stalemate
        while game.winner != 1:
            # alternate player each turn
            game.current_player = int(not game.current_player)
            # get current_player player's move
            move = game.get_move(game.current_player)
            # update board with latest move
            game.play_move(move, game.tokens[game.current_player])
            # check for a winner (or draw)
            winner = game.check_winner(game.tokens[game.current_player])
            if winner == -1:  # we have a draw
                game.message = (f' Oh shame! A draw ', '-')
                break
            elif winner == 1:  # we have a winner
                game.message = (
                    f" Congratulations {game.players[game.current_player]}!! You're the winner ", '*')
                break
            # no winner or draw so loop:
            continue
        game.over_message()
        game.reset()
    print('Bye!')
