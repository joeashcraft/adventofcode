import unittest
import day7


class MyFirstTests(unittest.TestCase):
    test_input = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
    ]

    def test_part1_helpers(self):
        self.assertIsInstance(day7.parse_instructions(self.test_input), list)

    def test_part1(self):
        self.assertEqual(day7.part1(self.test_input), 'CABDFE')


if __name__ == '__main__':
    unittest.main()
