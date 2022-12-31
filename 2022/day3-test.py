import unittest
import day3


class MyFirstTests(unittest.TestCase):

    test_input_raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(day3.find_the_duplicate(self.test_input_split[0]), "p")

    def test_part1(self):
        self.assertEqual(day3.part1(self.test_input_raw), 157)

    def test_part2(self):
        self.assertEqual(day3.part2(self.test_input_raw), 70)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
