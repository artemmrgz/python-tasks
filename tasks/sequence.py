import math
import argparse
from tasks.checkers import is_valid


class Sequence:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return ', '.join(map(str, self.row_sequence))

    @property
    def row_sequence(self):
        border = math.ceil(math.sqrt(self.n))
        return list(range(border))


def get_args():
    parser = argparse.ArgumentParser(description='Program shows sequence of comma-separated natural numbers, '
                                                 'whose square is less than the given number')
    parser.add_argument('number', type=float, help='number which will be considered as border')
    args = parser.parse_args()
    return args.number


def main():
    value = get_args()
    if not is_valid(value):
        raise ValueError('Value should be non-negative number')
    sequence = Sequence(value)
    print(sequence)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
