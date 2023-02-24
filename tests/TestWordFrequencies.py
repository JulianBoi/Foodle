import unittest
from lib.word_frequencies import word_frequencies

class TestWordFrequencies(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(word_frequencies("hello", 1), [("hello", 1)])

    def test_multiple_words(self):
        self.assertEqual(word_frequencies("baz bar foo foo zblah zblah zblah baz toto bar", 3), [("zblah", 3), ("bar", 2), ("baz", 2)])

    def test_same_frequency(self):
        self.assertEqual(word_frequencies("baz bar foo foo zblah zblah zblah baz toto bar toto", 3), [("bar", 2), ("baz", 2), ("zblah", 2)])

    def test_not_enough_words(self):
        self.assertEqual(word_frequencies("baz bar foo foo zblah zblah zblah baz toto bar", 10), [("zblah", 3), ("bar", 2), ("baz", 2), ("foo", 2), ("toto", 1)])

    def test_empty_sentence(self):
        self.assertEqual(word_frequencies("", 5), [])
if __name__ == '__main__':
    unittest.main()