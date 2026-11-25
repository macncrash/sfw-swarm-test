import unittest

from textkit.roman import to_roman


class T(unittest.TestCase):
    def test_roman(self):
        self.assertEqual(to_roman(1994), 'MCMXCIV')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')
        with self.assertRaises(ValueError):
            to_roman(0)
