from tasks.checkers import is_valid, is_yes


class Envelope:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fits_into(self, other) -> bool:
        '''Checks if sides of object lesser than other object's sides.
        Sides are always sorted.
        '''
        side_a, side_b = sorted((self.a, self.b))
        other_a, other_b = sorted((other.a, other.b))

        return side_a < other_a and side_b < other_b


def ask_sides(env_number):
    print(f'Please enter sides of {env_number} envelope')
    side_1 = float(input('Enter side a: '))
    side_2 = float(input('Enter side b: '))
    return side_1, side_2


def main():
    while True:
        a, b = ask_sides('first')
        c, d = ask_sides('second')
        if not all([is_valid(a), is_valid(b), is_valid(c), is_valid(d)]):
            raise ValueError('Value should be non-negative number')
        first_env = Envelope(a, b)
        second_env = Envelope(c, d)
        if first_env.fits_into(second_env):
            print('First envelope can be put inside second one')
        elif second_env.fits_into(first_env):
            print('Second envelope can be put inside first one')
        else:
            print('Envelopes cannot be fitted inside one another ')
        if not is_yes("Press 'y' or 'yes' if you want to continue "):
            break


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
