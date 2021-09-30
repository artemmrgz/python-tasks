from unittest import mock, TestCase
from collections import namedtuple
from tasks.sequence import Sequence, main

class TestSequence(TestCase):

    def test_sequence_class(self):
        seq = Sequence(9)
        self.assertEqual(str(seq), '0, 1, 2')

        seq = Sequence(0)
        self.assertEqual(str(seq), '')

        seq = Sequence(4.1)
        self.assertEqual(str(seq), '0, 1, 2')

    def test_main(self):
        FakeParser = namedtuple('FakeParser', ['number'])
        parser1 = FakeParser(8)
        parser2 = FakeParser(-4)
        with mock.patch('tasks.sequence.create_parser', side_effect=[parser1, parser2]):
            with mock.patch('tasks.sequence.print', return_value='fake_output'):
                self.assertEqual(main(), None)
                self.assertRaises(ValueError, main)
