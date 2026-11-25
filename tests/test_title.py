import unittest

from textkit.title import title_case


class T(unittest.TestCase):
    def test_title(self):
        self.assertEqual(title_case('the lord of the rings'), 'The Lord of the Rings')
        self.assertEqual(title_case('what it is made of'), 'What It Is Made Of')
