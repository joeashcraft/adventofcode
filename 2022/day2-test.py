import unittest
import day2

class MyFirstTests(unittest.TestCase):

    test_input_raw = '''A Y
B X
C Z'''
    test_input_split = test_input_raw.splitlines()

    def test_part1(self):
        self.assertEqual(
            day2.part1(self.test_input_raw),
            15
        )

    def test_part2(self):
        self.assertEqual(
            day2.part2(self.test_input_raw),
            12
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
