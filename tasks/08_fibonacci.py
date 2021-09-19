class FibonacciSequence:
    '''Class for generating Fibonacci sequence from start to stop.
    Start and stop values are excluded if they are part of the sequence
    '''
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.sequence = self.__generate_sequence()

    def __repr__(self):
        return ','.join(self.values_to_str())

    def __generate_sequence(self, first=0, second=1, seq=None):
        if not seq:
            seq = []
        next = first + second
        if next >= self.stop:
            return seq
        if next > self.start:
            seq.append(next)
        return self.__generate_sequence(second, next, seq)

    def values_to_str(self):
        return map(str, self.sequence)


def is_valid(value):
    return value >= 0


def main():
    start = float(input('Please enter the first number of the range: '))
    stop = float(input('Please enter the last number of the range: '))
    if is_valid(start) and is_valid(stop):
        if start > stop:
            start, stop = stop, start
        sequence = FibonacciSequence(start, stop)
        print(sequence)
    else:
        print("Value can't be negative")


if __name__ == '__main__':
    main()
