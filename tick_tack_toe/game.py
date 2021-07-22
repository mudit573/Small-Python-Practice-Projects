import time
from player import HumanPlayer ,RandomComputerPlayer


class TicTackToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #single list for 3x3
        self.current_winner = None # track for winner


    def print_board(self):
        # getting rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3) ]:
            print('|' + '|'.join(row)+ '|')

    @staticmethod
    def print_board_nums():
        # 0|1|2 etc (tell us what number corresponds to which box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row)+ '|')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot ==' ']
       

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square , letter):
        # check row
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind + 1)* 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square %3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check Diagonal
        # but only if square is even number(0,2,4,6,8) as only possible move
        if square %2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]]# left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2= [self.board[i] for i in [2,4,6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all of these fail
        return False



def play(game,x_palyer, o_palyer, print_game=True):
    if print_game:
        game.print_board_nums()

        letter = 'x' # starting letter

        while game.empty_squares():
            # get the move from appropriate player
            if letter == 'O':
                square = o_palyer.get_move(game)
            else:
                square = x_palyer.get_move(game)

            
            #lets define a fun to make a move
            if game.make_move(square,letter):
                if print_game:
                    print(letter + 'make a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + 'wins!')
                    return letter


                letter = 'O' if letter == 'X' else 'X'

            #break
            time.sleep(0.8)


        if print_game:
                print("Its a tie!")



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t= TicTackToe()
    play(t,x_player,o_player,print_game=True)