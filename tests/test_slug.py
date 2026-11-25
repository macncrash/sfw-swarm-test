import unittest

from textkit.slug import slugify


class T(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(slugify('Hello, World!'), 'hello-world')
        self.assertEqual(slugify('  many   spaces  '), 'many-spaces')
        self.assertEqual(slugify('Crème brûlée'), 'creme-brulee')
        self.assertEqual(slugify('---'), '')
