import unittest
from day4 import part1, part1_sleep_tots, part1_sleepiest_guard, part1_sleepiest_minute
from day4 import part2, part2_sleep_tots, part2_sleepiest_guard, part2_sleepiest_minute


class MyFirstTests(unittest.TestCase):
    raw_test_input = """[1518-11-03 00:24] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-05 00:55] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-01 00:55] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-01 00:05] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-04 00:36] falls asleep
[1518-11-02 00:40] falls asleep"""

    test_input = sorted([ii for ii in raw_test_input.splitlines()])

    test_dict = {
        "10": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        "99": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    }

    def test_part1_myHelpers(self):
        self.assertEqual(part1_sleep_tots(self.test_dict),
                         [('10', 50), ('99', 30)])
        self.assertEqual(part1_sleepiest_guard(self.test_dict), '10')
        self.assertEqual(part1_sleepiest_minute(self.test_dict), 24)

    def test_part1(self):
        self.assertEqual(part1(self.test_input), 240)

    def test_part2_myHelpers(self):
        self.assertEqual(part2_sleep_tots(self.test_dict),
                         [('10', 2), ('99', 3)])
        self.assertEqual(part2_sleepiest_guard(self.test_dict), '99')
        self.assertEqual(part2_sleepiest_minute(self.test_dict), 45)

    def test_part2(self):
        self.assertEqual(part2(self.test_input), 4455)


if __name__ == '__main__':
    unittest.main()
