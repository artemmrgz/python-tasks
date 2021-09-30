from unittest import TestCase, mock
from tasks.envelopes import Envelope, main


class TestEnvelopes(TestCase):

    def test_envelope_class(self):
        env1 = Envelope(3, 6)
        env2 = Envelope(3.5, 7)
        self.assertTrue(env1, env2)

        env1 = Envelope(6, 3)
        env2 = Envelope(3.5, 7)
        self.assertTrue(env1.fits_into(env2))

        env1 = Envelope(6, 3)
        env2 = Envelope(6, 4)
        self.assertFalse(env1.fits_into(env2))

    def test_main(self):
        with mock.patch('tasks.envelopes.ask_sides', side_effect=[(3, 6), (4, 7), (-4, 5), (2, 8)]):
            with mock.patch('tasks.envelopes.print', return_value='fake_output'):
                with mock.patch('tasks.envelopes.is_yes', return_value=False):
                    self.assertEqual(main(), None)
                    self.assertRaises(ValueError, main)
