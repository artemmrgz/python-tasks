import math


class Sequence:
    def __init__(self, n):
        self.n = self.__is_valid(n)

    def __str__(self):
        sequence = self.generate_sequence()
        nums_to_str = map(str, sequence)
        return ','.join(nums_to_str)

    @staticmethod
    def __is_valid(number):
        if number >= 0:
            return number
        raise ValueError('Value should be non-negative number')

    def generate_sequence(self):
        border = math.ceil(math.sqrt(self.n))
        return [num for num in range(border)]


def main():
    try:
        value = float(input('Please enter a number: '))
        sequence = Sequence(value)
        print(sequence)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
