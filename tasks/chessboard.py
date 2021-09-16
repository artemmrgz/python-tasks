import argparse


class Chessboard:
    def __init__(self, height, width):
        self.height = self.__check_value(height)
        self.width = self.__check_value(width)

    def __str__(self):
        board = self.__create_board()
        rows_to_str = [''.join(rows) for rows in board]
        return '\n'.join(rows_to_str)


    @staticmethod
    def __check_value(value):
        if value > 0:
            return value
        raise ValueError('Incorrect value. Value should be non-negative integer')


    def __create_board(self):
        board = [['*' for i in range(self.width)] for j in range(self.height)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    board[i][j] = ' '
        return board


def create_parser():
    parser = argparse.ArgumentParser(description='Program draws a chessboard with height and width provided by user')
    parser.add_argument('height', type=int, help='height of the chessboard')
    parser.add_argument('width', type=int, help='width of the chessboard')
    return parser.parse_args()


if __name__ == '__main__':
    args = create_parser()
    try:
        board = Chessboard(args.height, args.width)
        print(board)
    except ValueError as e:
        print(e)