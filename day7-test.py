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
    real_raw_input_A = [
        'Step G must be finished before step N can begin.',
        'Step N must be finished before step B can begin.'
    ]
    real_raw_input_B = [
        'Step G must be finished before step N can begin.',
        'Step N must be finished before step B can begin.',
        'Step P must be finished before step Q can begin.',
        'Step F must be finished before step U can begin.',
    ]
    real_raw_input_C = [
        'Step G must be finished before step N can begin.',
        'Step N must be finished before step B can begin.',
        'Step P must be finished before step Q can begin.',
        'Step F must be finished before step U can begin.',
        'Step H must be finished before step A can begin.',
        'Step C must be finished before step S can begin.',
        'Step A must be finished before step K can begin.',
        'Step M must be finished before step O can begin.',
        'Step V must be finished before step L can begin.',
        'Step E must be finished before step L can begin.',
    ]

    file = open('day7-input.txt', 'r')
    raw_instructions: list = file.readlines()
    file.close()


    def test_part1_helpers(self):
        self.assertIsInstance(day7.parse_instructions(self.test_input), list)

    def test_part1(self):
        self.assertEqual(day7.part1(self.test_input), 'CABDFE')
        self.assertNotEqual(day7.part1(self.raw_instructions), 'FGHANBCEMRDPIWQUZJYTKVLOSX')

    # def test_part1_extra_tests(self):
    #     self.assertEqual(day7.part1(self.real_raw_input_A), 'GNB')
    #     self.assertEqual(day7.part1(self.real_raw_input_B), 'GNBFPQU')
    #     self.assertEqual(day7.part1(self.real_raw_input_C), 'CEFHMPVAGKLNBOQSU')



if __name__ == '__main__':
    unittest.main(verbosity=2)
