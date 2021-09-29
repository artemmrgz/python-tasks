import math
from tasks.checkers import is_yes


class InputError(Exception):
    pass


class Triangle:
    '''The class holds triangle object data.
    Note that the sum of any two sides should be bigger than third one
    '''

    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self) -> float:
        semi_perimeter = (self.a + self.b + self.c) / 2
        result = math.sqrt(semi_perimeter *
                           (semi_perimeter - self.a) *
                           (semi_perimeter - self.b) *
                           (semi_perimeter - self.c))
        return round(result, 2)


def parse_input(input_str):
    '''Parses string into four parts.
    Returns tuple of name(str) and three sides(float)
    '''
    values = input_str.split(',')
    if len(values) != 4:
        raise InputError('Input should consist of 4 arguments separated by comma')
    stripped_values = list(map(lambda x: x.strip(), values))
    name, sides = stripped_values[0], stripped_values[1:]
    side_a, side_b, side_c = map(lambda x: float(x), sides)
    return name, side_a, side_b, side_c


def is_valid(a, b, c):
    return (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)


def generate_output(triangles_list):
    output = ['============= Triangles list: ===============']
    for counter, triangle in enumerate(triangles_list, 1):
        output.append(f"{counter}. [{triangle.name}]: {triangle.area} cm")
    return '\n'.join(output)


def main():
    triangles = []
    while True:
        input_string = input('Enter triangle name and 3 sizes using comma as a delimiter ')
        try:
            name, side_a, side_b, side_c = parse_input(input_string)
        except InputError as e:
            if is_yes(f"{e}. Press 'y' or 'yes' if you want to try again "):
                continue
            break

        if not is_valid(side_a, side_b, side_c):
            raise ValueError('Sides should be positive and sum of any of two sides should be bigger than third one')
        triangle = Triangle(name, side_a, side_b, side_c)
        triangles.append(triangle)
        if not is_yes("Press 'y' or 'yes' if you want to continue "):
            break

        triangles.sort(reverse=True, key=lambda x: x.area)
        output = generate_output(triangles)
        print(output)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
