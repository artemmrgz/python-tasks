import argparse
from tasks.checkers import is_valid, is_yes

class Chessboard:
    '''Class for chessboard constructing
    Args:
            height (int): number of rows
            width (int): length of rows
    '''

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = self.create_board()

    def __repr__(self):
        return '\n'.join(self.rows_to_str())

    def create_board(self):
        board = [['*' for _ in range(self.width)] for _ in range(self.height)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    board[i][j] = ' '
        return board

    def rows_to_str(self):
        return [''.join(rows) for rows in self.board]


def get_args():
    parser = argparse.ArgumentParser(description='Program draws a chessboard with height and width provided by user',
                                     usage="To start program type 'chessboard.py <height> <width>'")
    parser.add_argument('height', type=int, help='height of the chessboard')
    parser.add_argument('width', type=int, help='width of the chessboard')
    args = parser.parse_args()
    return args.height, args.width


def main():
    height, width = get_args()
    if not all([is_valid(height), is_valid(width)]):
        raise ValueError('Value should be non-negative integer')
    board = Chessboard(height, width)
    print(board)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
