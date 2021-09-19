import argparse
import os


def find(text, string_to_find):
    '''Counts all occurrences of string in text'''
    output = text.count(string_to_find)
    return output


def file_reader(path_to_file):
    fullpath = os.path.join(os.path.dirname(__file__), path_to_file)
    with open(fullpath) as f:
        content = f.read()
    return content


def write_to_file(path_to_file, text):
    with open(path_to_file, 'w') as f:
        f.write(text)


def create_parser():
    parser = argparse.ArgumentParser(description='Count or replace strings in a file')
    parser.add_argument('path', help='Path to file')
    parser.add_argument('to_find', help='String that should be found in the file')
    parser.add_argument('to_replace', nargs='?', default=None, help='String that should be changed to. \
                                                                    It\'s empty by default')
    return parser.parse_args()


def main():
    args = create_parser()
    try:
        text = file_reader(args.path)
        counts = find(text, args.to_find)
        if not args.to_replace:
            print(counts)
        elif counts > 1:
            answer = input(f"We found {counts} occurrences of the string."
                           f"Type 'y' or 'yes' if you want to change all of them ").lower()
            if answer == 'y' or answer == 'yes':
                changed_text = text.replace(args.to_find, args.r)
            else:
                changed_text = text.replace(args.to_find, args.r, 1)
            write_to_file(args.path, changed_text)
    except FileNotFoundError as e:
        print("File can't be found, please check and try again")


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("File can't be found, please check and try again")
