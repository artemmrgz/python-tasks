import argparse
from tasks.checkers import is_yes
from tasks.file_manager import FileOperator


class TextParser(FileOperator):

    def count(self, to_find):
        return self.content.count(to_find)

    def replace(self, to_find, to_change, occurrences=1):
        new = self.content.replace(to_find, to_change, occurrences)
        self.save(new)


def create_parser():
    parser = argparse.ArgumentParser(description='Count or replace strings in a file')
    parser.add_argument('path', help='Path to file')
    parser.add_argument('to_find', help='String that should be found in the file')
    parser.add_argument('to_replace', nargs='?', default=None, help='String that should be changed to. \
                                                                    It\'s empty by default')
    return parser.parse_args()


def main():
    args = create_parser()
    text_object = TextParser(args.path)
    counts = text_object.count(args.to_find)
    if args.to_replace:
        if counts > 1 and is_yes(
                f"We found {counts} occurrences of the string. Type 'y' or 'yes' if you want to change all of them "):
            text_object.replace(args.to_find, args.to_replace, counts)
        else:
            text_object.replace(args.to_find, args.to_replace)
        print('File was changed')
    else:
        print(counts)


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("File can't be found, please check and try again")
