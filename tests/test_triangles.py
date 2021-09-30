from unittest import TestCase, mock
from tasks import triangles


class TestTriangles(TestCase):

    def test_triangle_class(self):
        triangle = triangles.Triangle('first', 3, 4.5, 5)
        self.assertEqual(triangle.area, 6.67)

    def test_parse_input(self):
        self.assertEqual(triangles.parse_input('first ,  3, 4, 5'), ('first', 3, 4, 5))
        self.assertRaises(triangles.InputError, triangles.parse_input, 'first, 3, 5')

    def test_main(self):
        with mock.patch('tasks.triangles.input', side_effect=['first ,  3, 4.5, 5',
                                                              'second, 1, 5, 3',
                                                              'third, -5, 6, 7']):
            with mock.patch('tasks.triangles.is_yes', return_value=False):
                self.assertEqual(triangles.main(), None)
                self.assertRaises(ValueError, triangles.main)
                self.assertRaises(ValueError, triangles.main)
