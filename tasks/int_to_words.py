class Number:
    """Converts integer to words
    Args:
        num (int): any integer
    """

    _ones = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
            9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
            15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    _tens = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
              8: 'восемьдесят', 9: 'девяносто'}
    _hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот',
                8: 'восемьсот', 9: 'девятьсот'}
    _thousands = {1: ('тысяча', 'тысячи', 'тысяч'),
                 2: ('миллион', 'миллиона', 'миллионов'),
                 3: ('триллион', 'триллиона', 'триллионов'),
                 4: ('квадриллион', 'квадриллиона', 'квадриллионов'),
                 5: ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),
                 6: ('секстиллион', 'секстиллиона', 'секстиллионов'),
                 7: ('септиллион', 'септиллиона', 'септиллионов'),
                 8: ('октиллион', 'октиллиона', 'октиллионов'),
                 9: ('нониллион', 'нониллиона', 'нониллионов')}
    _exceptions = {1: 'одна', 2: 'две'}

    def __init__(self, num):
        self.number = num

    def to_words(self) -> str:
        if self.number == 0:
            return 'ноль'
        return self._word_generator(self.number)

    def _word_generator(self, number, exception=False):
        if number < 0:
            return f'минус {self._word_generator(-number)}'
        if number < 20:
            if exception:
                return Number._exceptions[number]
            return Number._ones[number]
        if number < 100:
            return f'{Number._tens[number // 10]} {Number._ones[number % 10]}'
        if number < 1000:
            return f'{Number._hundreds[number // 100]} {self._word_generator(number % 100)}'
        for power in Number._thousands:
            if number < 1000 ** (power + 1):
                return self._thousands_constructor(number, power)

    def _thousands_constructor(self, number, power):
        quotient, remainder = divmod(number, 1000 ** power)
        from_1000_to_2999 = quotient < 3 and power == 1
        if quotient == 1:
            word = self._thousands[power][0]
        elif 1 < quotient < 5:
            word = self._thousands[power][1]
        else:
            word = self._thousands[power][2]
        return f'{self._word_generator(quotient, exception=from_1000_to_2999)} {word} {self._word_generator(remainder)}'


def main():
    number = int(input('Please enter the number: '))
    num = Number(number)
    output = num.to_words()
    print(output)


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Value should be integer')