import unittest
import day5


class MyFirstTests(unittest.TestCase):

    test_input_raw = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    test_input_split = test_input_raw.splitlines()

    expected_split_input = [
        # fmt: off
        [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ],
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ],
    ]  # fmt: on

    def test_helpers(self):
        # test result
        # self.assertEqual(
        #     day5.split_puzzle_input(self.test_input_split),
        #     self.expected_split_input,
        # )
        # test length of result
        self.assertEqual(len(day5.split_puzzle_input(self.test_input_split)), 2)

    def test_part1(self):
        self.assertEqual(day5.part1(self.test_input_raw), "CMZ")

    def test_part2(self):
        self.assertEqual(day5.part2(self.test_input_raw), "MCD")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
