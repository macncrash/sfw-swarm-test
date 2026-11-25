import unittest

from textkit.words import word_count


class T(unittest.TestCase):
    def test_words(self):
        self.assertEqual(word_count(''), 0)
        self.assertEqual(word_count("it's a dog's life"), 4)
        self.assertEqual(word_count('one,two  three\nfour'), 4)
