import unittest
from day2 import checksum, letterCount, part2

class MyFirstTests(unittest.TestCase):
    def test_myHelpers(self):
        self.assertEqual(letterCount('bababc'), {'a': 2, 'b': 3, 'c': 1})

    def test_part1(self):
        box_list = ['abcdef', 'bababc', 'abbcde',
                    'abcccd', 'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(checksum(box_list), 12)

    def test_part2(self):
        box_list = ['abcde', 'fghij', 'klmno',
                    'pqrst', 'fguij', 'axcye', 'wvxyz']
        self.assertEqual(part2(box_list), 'fgij')


if __name__ == '__main__':
    unittest.main()
