class Number:
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    dozens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
              8: 'eighty', 9: 'ninety'}
    others = {1: 'thousand', 2: 'million', 3: 'billion'}

    def __init__(self, num):
        self.num = num
        self.words = self.verbalize()

    def verbalize(self):
        if self.num == 0:
            return 'zero'
        return self._word_generator(self.num)

    def _word_generator(self, number):
        if number < 0:
            return f'negative {self._word_generator(-number)}'
        if number < 20:
            return Number.ones[number]
        if number < 100:
            return f'{Number.dozens[number // 10]} {Number.ones[number % 10]}'
        if number < 1000:
            return self.to_segment(number, 100, 'hundred')
        for power, name in Number.others.items():
            if number < 1000 ** (power + 1):
                return self.to_segment(number, 1000 ** power, name)

    def to_segment(self, dividend, divisor, word):
        return f'{self._word_generator(dividend // divisor)} {word} {self._word_generator(dividend % divisor)}'


def main():
    try:
        number = int(input('Please enter the number: '))
        print(Number(number))
    except ValueError:
        print('Value should be integer')


if __name__ == '__main__':
    main()