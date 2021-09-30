from unittest import mock, TestCase
from tasks.chessboard import Chessboard, main


class TestChessboard(TestCase):

    def test_chessboard_class(self):
        board = Chessboard(3, 4)
        self.assertEqual(repr(board), '* * \n * *\n* * ')

        board = Chessboard(0, 4)
        self.assertEqual(repr(board), '')

    def test_main(self):
        with mock.patch('tasks.chessboard.get_args', side_effect=[(3, 4), (-4, 4)]):
            with mock.patch('tasks.chessboard.print', return_value='fake_output'):
                self.assertEqual(main(), None)
                self.assertRaises(ValueError, main)
