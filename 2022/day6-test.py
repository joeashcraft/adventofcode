import unittest
import day6


class MyFirstTests(unittest.TestCase):

    test_input_raw = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    test_input_raw2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    test_input_raw3 = "nppdvjthqldpwncqszvftbrmjlhg"
    test_input_raw4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    test_input_raw5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day6.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day6.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(day6.part1(self.test_input_raw), 7)
        self.assertEqual(day6.part1(self.test_input_raw2), 5)
        self.assertEqual(day6.part1(self.test_input_raw3), 6)
        self.assertEqual(day6.part1(self.test_input_raw4), 10)
        self.assertEqual(day6.part1(self.test_input_raw5), 11)

    # def test_part2(self):
    #     self.assertEqual(day6.part2(self.test_input_raw), 45000)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
