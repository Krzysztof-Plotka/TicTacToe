import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Board:
    def __init__(self):
        self.__board = [[None for x in range(3)]for x in range(3)]
        
    def print_board(self):
        self.__display_values = [[1,2,3],[4,5,6],[7,8,9]]
        print(' -----------')
        for row in range(3):
            print('|',end='')
            for index in range(3):
                if self.__board[row][index] :self.__display_values[row][index] = self.__board[row][index]
                print(f' {self.__display_values[row][index]} |',end='')
            print('\n -----------')

    def get_value(player:int, index:tuple) -> bool:
        if not self.__board[index[0]][index[1]]:
            self.__board[index[0]][index[1]] = 'X' if player else 'O'
            return True
        else:
            return False

board = Board()
player = 1 if input('Would you like to be player 1? Y/N') == 'Y' else 2
board.print_board()

