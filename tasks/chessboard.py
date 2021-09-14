import argparse


class Chessboard:
    def __init__(self, height, width):
        self.height = self.__check_value(height)
        self.width = self.__check_value(width)

    def __str__(self):
        return self.__create_board()

    @staticmethod
    def __check_value(value):
        if isinstance(value, int) and value >= 0:
            return value
        raise ValueError('Incorrect value. Value should be non-negative integer')

    def __create_board(self):
        board = [['*' for i in range(self.width)] for j in range(self.height)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    board[i][j] = ' '
        board = [''.join(i) for i in board]
        result = '\n'.join(board)
        return result


def create_parser():
    parser = argparse.ArgumentParser(description='Program draws a chessboard with height and width provided by user')
    parser.add_argument('height', help='height of the chessboard')
    parser.add_argument('width', help='width of the chessboard')
    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = create_parser()
        board = Chessboard(args.height, args.width)
        print(board)
    except ValueError as e:
        print(e)