import argparse
from tasks.checkers import is_valid


class FibonacciSequence:
    '''Class for generating Fibonacci sequence from start to stop.
    Start and stop values are excluded if they are part of the sequence
    '''
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.sequence = self._generate_sequence()

    def __repr__(self):
        return ', '.join(map(str, self.sequence))

    def _generate_sequence(self, first=0, second=1, seq=None):
        if not seq:
            seq = []
        if first > self.start:
            seq.append(first)
        if second >= self.stop:
            return seq
        return self._generate_sequence(second, first+second, seq)


def get_args():
    parser = argparse.ArgumentParser(description='Program shows Fibonacci sequence in the specified range')
    parser.add_argument('start', type=float, help='first number of sequence')
    parser.add_argument('stop', type=float, help='second number of sequence')
    args = parser.parse_args()
    return args.start, args.stop


def main():
    start, stop = get_args()
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
