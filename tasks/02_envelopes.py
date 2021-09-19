class Envelope:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fits_into(self, other) -> bool:
        '''Checks if sides of object lesser than other object's sides.
        Bigger side is always first
        '''
        side_a, side_b = sorted((self.a, self.b))
        other_a, other_b = sorted((other.a, other.b))

        return side_a < other_a and side_b < other_b


def is_valid(value):
    return value > 0


def main():
    flag = True
    while flag:
        print('Please enter sides of first envelope')
        a = float(input('Enter side a: '))
        b = float(input('Enter side b: '))
        print('Please enter sides of second envelope')
        c = float(input('Enter side c: '))
        d = float(input('Enter side d: '))
        if is_valid(a) and is_valid(b) and is_valid(c) and is_valid(d):
            first_env = Envelope(a, b)
            second_env = Envelope(c, d)
            if first_env.fits_into(second_env):
                print('First envelope can be fitted into second one')
            else:
                print('First envelope can\'t be fitted into second one')
            answer = input("Press 'y' or 'yes' if you want to continue ").lower()
            if answer != 'y' and answer != 'yes':
                flag = False
        else:
            print('Value should be non-negative number')


if __name__ == '__main__':
    main()
