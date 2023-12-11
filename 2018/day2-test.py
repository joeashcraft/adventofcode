import unittest
from day2 import checksum, letterCount, part2, part2_find_diffs, part2_find_common


class MyFirstTests(unittest.TestCase):
    def test_part1_myHelpers(self):
        self.assertEqual(letterCount('bababc'), {'a': 2, 'b': 3, 'c': 1})

    def test_part1(self):
        box_list = ['abcdef', 'bababc', 'abbcde',
                    'abcccd', 'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(checksum(box_list), 12)

    def test_part2_helpers(self):
        self.assertEqual(part2_find_diffs('abcde', 'axcye'), [2, 4])
        self.assertEqual(part2_find_diffs('fghij', 'fguij'), [3])
        self.assertEqual(part2_find_common('fghij', 'fguij'), 'fgij')

    def test_part2(self):
        box_list = ['abcde', 'fghij', 'klmno',
                    'pqrst', 'fguij', 'axcye', 'wvxyz']
        self.assertEqual(part2(box_list), 'fgij')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
