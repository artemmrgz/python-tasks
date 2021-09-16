def check_envelopes(a, b, c, d):
    if a == c and b == d:
        return 'Equal'

    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c

    if a >= c and b >= d:
        return 'First is bigger'
    if a <= c and b <= d:
        return 'Second is bigger'
    return 'No one'


def main():
    flag = True
    while flag:
        print('Please enter sides of first envelope')
        a = float(input('Enter side a: '))
        b = float(input('Enter side b: '))
        print('Please enter sides of second envelope')
        c = float(input('Enter side c: '))
        d = float(input('Enter side d: '))

        result = check_envelopes(a, b, c, d)
        print(result)
        answer = input("Press 'y' or 'yes' if you want to continue ").lower()
        if answer != 'y' and answer != 'yes':
            flag = False


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Integer or float number expected')
