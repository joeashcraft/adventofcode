import unittest
import logging
import day4


class MyFirstTests(unittest.TestCase):

    test_input_raw = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day4.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day4.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(day4.part1(self.test_input_raw), 2)

    def test_part2(self):
        self.assertEqual(day4.part2(self.test_input_raw), 4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
