import argparse
from tasks.checkers import is_valid


class FibonacciSequence:
    '''Class for generating Fibonacci sequence from start to stop.
    Start and stop values are excluded if they are part of the sequence
    '''
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.sequence = self.__generate_sequence()

    def __repr__(self):
        return ', '.join(self.values_to_str())

    def __generate_sequence(self, first=0, second=1, seq=None):
        if not seq:
            seq = []
        if first > self.start:
            seq.append(first)
        if second >= self.stop:
            return seq
        return self.__generate_sequence(second, first+second, seq)

    def values_to_str(self):
        return map(str, self.sequence)


def create_parser():
    parser = argparse.ArgumentParser(description='Program shows Fibonacci sequence in the specified range',
                                     usage="To start program type 'fibonacci.py <start value> <stop value>'")
    parser.add_argument('start', type=float, help='first number of sequence')
    parser.add_argument('stop', type=float, help='second number of sequence')
    return parser.parse_args()


def main():
    args = create_parser()
    start, stop = args.start, args.stop
    if not all([is_valid(start), is_valid(stop)]):
        raise ValueError("Value can't be negative")
    if start > stop:
        start, stop = stop, start
    sequence = FibonacciSequence(start, stop)
    print(sequence)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
