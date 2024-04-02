import time
from board import Board
from player import HumanPlayer, ComputerPlayer

class Game:
    def __init__(self, human_symbol='X', computer_symbol='O'):
        self.board = Board()
        self.human = HumanPlayer(human_symbol)
        self.computer = ComputerPlayer(computer_symbol)
        self.current_player = self.human    # by default, human goes first
        self.players = {human_symbol: self.human, computer_symbol: self.computer}

    def switch_player(self):
        self.current_player = self.computer if self.current_player == self.human else self.human

    def play(self):
        game_over = False
        while not game_over:
            self.board.display_board()
            move = self.current_player.get_move(self.board)
            self.board.update_board(move, self.current_player.symbol)

            if self.board.check_winner():
                self.board.display_board()
                print(f'{self.current_player} wins!')
                game_over = True
            elif self.board.is_full():
                self.board.display_board()
                print('It\'s a tie!')
                game_over = True
            else:
                self.switch_player()

        self.post_game_over_message()
    
    def post_game_over_message(self):
        time.sleep(1)
        print('Game over! Thanks for playing!')

if __name__ == '__main__':
    game = Game()
    game.play()