import argparse


def find(text, string_to_find):
    output = text.count(string_to_find)
    return output


def file_reader(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def write_to_file(path_to_file, text):
    with open(path_to_file, 'w') as f:
        f.write(text)


def change_string(text, string_to_find, string_to_change):
    occurrence_count = find(text, string_to_find)
    answer = 'no'
    if occurrence_count > 1:
        answer = input(f"We found {occurrence_count} occurrences of the string. Type 'y' or 'yes' if you want to change all of them ").lower()
    if answer == 'y' or answer == 'yes':
        return text.replace(string_to_find, string_to_change)
    return text.replace(string_to_find, string_to_change, 1)


def create_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('path', help='Path to file')
    parser.add_argument('to_find', help='String that should be found in the file')
    parser.add_argument('-r', '--replace', help='String that should be changed to')
    return parser.parse_args()


if __name__ == '__main__':
    args = create_parser()
    try:
        text = file_reader(args.path)
        if not args.c:
            print(find(text, args.to_find))
        else:
            changed_text = change_string(text, args.to_find, args.c)
            write_to_file(args.path, changed_text)
    except FileNotFoundError:
        print("File can't be found, please check and try again")


