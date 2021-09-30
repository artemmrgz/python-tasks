import sys
import argparse
from tasks.file_manager import FileOperator

def is_lucky_moscow(ticket):
    first_part, second_part = ticket[:3], ticket[3:]
    first_numbers = map(int, list(first_part))
    second_numbers = map(int, list(second_part))
    return sum(first_numbers) == sum(second_numbers)


def is_lucky_piter(ticket):
    numbers = list(map(int, list(ticket)))
    even = filter(lambda x: x % 2 == 0, numbers)
    odd = filter(lambda x: x % 2 != 0, numbers)
    return sum(even) == sum(odd)


def choose(method):
    methods = {'moscow': is_lucky_moscow,
               'piter': is_lucky_piter}
    return methods.get(method)


def find_valid_tickets(text):
    tickets = text.split(' ')
    valid_tickets = filter(lambda x: len(x) == 6, tickets)
    return valid_tickets


class InputError(Exception):
    pass


def get_args():
    parser = argparse.ArgumentParser(description='Program counts number of lucky tickets from selected file')
    parser.add_argument('path', help='path to file with tickets')
    parser.add_argument('method', help='method of counting lucky tickets (Moscow or Piter)')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    return args.path, args.method.lower()


def main():
    path_to_file, method = get_args()
    content = FileOperator(path_to_file).content
    tickets = find_valid_tickets(content)
    if not choose(method):
        raise InputError('Incorrect method selected')
    lucky_tickets = list(filter(choose(method), tickets))
    print(len(lucky_tickets))


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("File can't be found, please check and try again")
    except InputError as e:
        print(e)
