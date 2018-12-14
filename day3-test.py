import unittest
from day3 import part1, part1_parse_claims_list, part1_claim_to_coords


class MyFirstTests(unittest.TestCase):
    claims_list = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]

    claim_test = {'id': 123, 'x': 3, 'y': 2, 'w': 5, 'h': 4}  # '#123 @ 3,2: 5x4'
    # ...........
    # ...........
    # ...#####...
    # ...#####...
    # ...#####...
    # ...#####...
    # ...........
    # ...........
    # ...........

    def test_part1_myHelpers(self):
        self.assertEqual(part1_parse_claims_list(self.claims_list), [
                         {'id': 1, 'x': 1, 'y': 3, 'w': 4, 'h': 4},
                         {'id': 2, 'x': 3, 'y': 1, 'w': 4, 'h': 4},
                         {'id': 3, 'x': 5, 'y': 5, 'w': 2, 'h': 2}])
        self.assertEqual(part1_claim_to_coords(self.claim_test), [
            (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
            (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
            (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
            (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)
        ]

        )

    def test_part1(self):
        self.assertEqual(part1(self.claims_list), 4)

    # def test_part2_helpers(self):
    #     self.assertEqual(part2_find_diffs('abcde', 'axcye'), [2, 4])
    #     self.assertEqual(part2_find_diffs('fghij', 'fguij'), [3])
    #     self.assertEqual(part2_find_common('fghij', 'fguij'), 'fgij')
    #
    # def test_part2(self):
    #     box_list = ['abcde', 'fghij', 'klmno',
    #                 'pqrst', 'fguij', 'axcye', 'wvxyz']
    #     self.assertEqual(part2(box_list), 'fgij')


if __name__ == '__main__':
    unittest.main()
