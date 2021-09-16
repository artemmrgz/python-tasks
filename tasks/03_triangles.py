import math


class InputError(Exception):
    pass


def calculate_area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    result = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return round(result, 2)


def is_valid(a, b, c):
    return (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)


def generate_output(triangles_list):
    output = ['============= Triangles list: ===============']
    for counter, triangle in enumerate(triangles_list, 1):
        output.append(f"{counter}. [{triangle.get('name')}]: {triangle.get('area')} cm")
    return '\n'.join(output)


def main():
    triangles = []
    flag = True
    while flag:
        input_string = input('Enter triangle name and 3 sizes using comma as a delimiter ')
        input_values = input_string.split(',')
        if len(input_values) != 4:
            raise InputError('Input should consist of 4 arguments')
        stripped_values = list(map(lambda x: x.strip(), input_values))
        name, sides = stripped_values[0], stripped_values[1:]
        side_a, side_b, side_c = map(lambda x: float(x), sides)
        if not is_valid(side_a, side_b, side_c):
            raise ValueError('Sides should be positive and sum of any of two sides should be bigger than third one')
        area = calculate_area(side_a, side_b, side_c)
        triangles.append({'name': name, 'area': area})
        answer = input("Press 'y' or 'yes' if you want to continue ").lower()
        if answer != 'y' and answer != 'yes':
            flag = False

    triangles.sort(reverse=True, key=lambda x: x.get('area'))
    return triangles


if __name__ == "__main__":
    try:
        result = main()
        print(generate_output(result))
    except InputError as e:
        print(e)
    except ValueError as e:
        print(e)
