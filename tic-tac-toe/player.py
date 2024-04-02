import time
import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol    # symbol is 'X' or 'O'

    # to get the next move for the player given a board
    def get_move(self, board):
        pass    # base player class

class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, board):
        print('Computer\'s turn...')
        time.sleep(1)    # to make the computer's move seem more natural
        square = random.choice(board.available_moves())
        return square
    
    def __str__(self):
        return f"ComputerPlayer: {self.symbol}"

class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, board):
        print('Now it\'s your turn.')
        move = input('Enter your move (0-8): ')
        try:
            move = int(move)
            if move < 0 or move > 8:
                raise ValueError
            if not board.is_position_empty(move):
                print('Invalid move. The space is not empty. Please try again.')
            else:
                return move
        except ValueError:
            print('Invalid move. Please enter a number between 0 and 8.')

    def __str__(self):
        return f"HumanPlayer: {self.symbol}"
