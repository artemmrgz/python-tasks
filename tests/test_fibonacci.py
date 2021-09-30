from unittest import mock, TestCase
from tasks.fibonacci import FibonacciSequence, main


class TestSequence(TestCase):

    def test_fibonacci_class(self):
        fib = FibonacciSequence(2, 34)
        self.assertEqual(fib.sequence, [3, 5, 8, 13, 21])

        fib = FibonacciSequence(0.8, 5)
        self.assertEqual(repr(fib), '1, 1, 2, 3')

    def test_main(self):
        with mock.patch('tasks.fibonacci.get_args', side_effect=[(2, 10), (-4, 4)]):
            with mock.patch('tasks.fibonacci.print', return_value='fake_output'):
                self.assertEqual(main(), None)
                self.assertRaises(ValueError, main)
