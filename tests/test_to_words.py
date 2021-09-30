from unittest import TestCase, mock
from tasks.int_to_words import Number, main


class TestToWords(TestCase):

    def test_number_class(self):
        num = Number(12345)
        self.assertEqual(num.stringify(), 'двенадцать тысяч триста сорок пять')

        num = Number(0)
        self.assertEqual(num.stringify(), 'ноль')

        num = Number(-123)
        self.assertEqual(num.stringify(), 'минус сто двадцать три')

    def test_main(self):
        with mock.patch('tasks.int_to_words.input', side_effect=['123', '45.5', 'abc']):
            with mock.patch('tasks.int_to_words.print', return_value='fake_output'):
                self.assertEqual(main(), None)
                self.assertRaises(ValueError, main)
                self.assertRaises(ValueError, main)
