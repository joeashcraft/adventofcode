import unittest
import day1

class MyFirstTests(unittest.TestCase):

    test_input_raw = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(
            6000,
            day1.totals(self.test_input_split)[0],
        )
        self.assertEqual(len(day1.totals(self.test_input_split)), 5)


    def test_part1(self):
        self.assertEqual(day1.part1(self.test_input_raw), 24000)

    def test_part2(self):
        self.assertEqual(day1.part2(self.test_input_raw), 45000)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
