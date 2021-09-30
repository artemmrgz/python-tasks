from unittest import mock, TestCase
from tasks.sequence import SquaresSequence, main

class TestSequence(TestCase):

    def test_sequence_class(self):
        seq = SquaresSequence(9)
        self.assertEqual(str(seq), '0, 1, 2')

        seq = SquaresSequence(0)
        self.assertEqual(str(seq), '')

        seq = SquaresSequence(4.1)
        self.assertEqual(str(seq), '0, 1, 2')

    def test_main(self):
        with mock.patch('tasks.sequence.get_args', side_effect=[8, -4]):
            with mock.patch('tasks.sequence.print', return_value='fake_output'):
                self.assertEqual(main(), None)
                self.assertRaises(ValueError, main)
