import os
from collections import namedtuple
from unittest import mock, TestCase
from tasks.tickets import is_lucky_moscow, is_lucky_piter, find_valid_tickets, main, InputError


class TestFileParser(TestCase):

    def test_is_lucky_moscow(self):
        self.assertTrue(is_lucky_moscow('123321'))
        self.assertFalse(is_lucky_moscow('123320'))

    def test_is_lucky_piter(self):
        self.assertTrue(is_lucky_piter('123163'))
        self.assertFalse(is_lucky_piter('123123'))

    def test_find_valid_tickets(self):
        self.assertEqual(len(list(find_valid_tickets('123 123456 1'))), 1)
        self.assertEqual(len(list(find_valid_tickets(''))), 0)

    def test_main(self):
        FakeParser = namedtuple('FakeParser', ['path', 'method'])
        parser1 = FakeParser('some/path', 'moscow')
        parser2 = FakeParser(os.path.abspath(__file__), 'some_method')
        with mock.patch('tasks.tickets.get_args', side_effect=[parser1, parser2]):
            self.assertRaises(FileNotFoundError, main)
            self.assertRaises(InputError, main)
