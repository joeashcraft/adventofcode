import unittest
from day2 import checksum, letterCount, part2

"""For example, if you see the following box IDs:

* abcdef contains no letters that appear exactly two or three times.
* bababc contains two a and three b, so it counts for both.
* abbcde contains two b, but no letter appears exactly three times.
* abcccd contains three c, but no letter appears exactly two times.
* aabcdd contains two a and two d, but it only counts once.
* abcdee contains two e.
* ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.

Multiplying these together produces a checksum of 4 * 3 = 12.
"""


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
