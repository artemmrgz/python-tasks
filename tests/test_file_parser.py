import os
from unittest import TestCase, mock
from tasks.file_parser import TextParser, main


class FakeFile:
    def __init__(self):
        self.content = '''Once upon a time a girl named Cinderella lived with her stepmother and two stepsisters. 
        Poor Cinderella had to work hard all day long so the others could rest.'''

    def read(self):
        return self.content

    def write(self, new_text):
        self.content = new_text

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


class TestFileParser(TestCase):

    def test_editor_class(self):
        phrase = 'Cinderella'
        file = FakeFile()
        with mock.patch('tasks.file_manager.open', return_value=file):
            editor = TextParser('some/path')
            self.assertEqual(editor.count(phrase), 2)
            editor.replace(phrase, 'Snow White')
            self.assertEqual(file.content, '''Once upon a time a girl named Snow White lived with her stepmother and two stepsisters. 
        Poor Cinderella had to work hard all day long so the others could rest.''')

    def test_main(self):
        with mock.patch('tasks.file_parser.get_args', side_effect=[('some/path', 'a', 'b'), (os.path.abspath(__file__), 'a', 'b')]):
            with mock.patch('tasks.file_parser.TextParser.count', return_value=1):
                with mock.patch('tasks.file_parser.TextParser.replace', return_value=None):
                    self.assertRaises(FileNotFoundError, main)
                    self.assertEqual(main(), None)
