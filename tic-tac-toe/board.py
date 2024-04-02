class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    # single list to represent 3x3 board

    def display_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def update_board(self, position, symbol):
        self.board[position] = symbol

    def is_position_empty(self, position):
        return self.board[position] == ' '
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def is_full(self):
        return self.board.count(' ') == 0

    def check_winner(self):
        for row in range(3):
            if self.board[row*3] == self.board[row*3 + 1] == self.board[row*3 + 2] != ' ':
                return True
        for col in range(3):
            if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False