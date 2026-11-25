import unittest

from textkit.wrap import wrap


class T(unittest.TestCase):
    def test_wrap(self):
        self.assertEqual(wrap('the quick brown fox', 10), ['the quick', 'brown fox'])
        self.assertEqual(wrap('a supercalifragilistic b', 5), ['a', 'supercalifragilistic', 'b'])
        self.assertEqual(wrap('', 5), [])
