from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    
    @staticmethod
    def print_board_numbs():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        return [i for i,spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return False
        return False
    
    def winner(self, square, letter):
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in row]):
            return True
        
        if square % 2 == 0:
            diagnal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagnal1]):
                return True
            diagnal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagnal2]):
                return True
            
        return False
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbs()
    
    letter = "X"
    while game.empty_squares():
        if letter == "0":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + 'wins')
                return letter
            
            letter = '0' if letter == 'X' else 'X'
        
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('0')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)