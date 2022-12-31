import unittest
import day7


class MyFirstTests(unittest.TestCase):

    test_input_raw = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day7.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day7.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(day7.part1(self.test_input_raw), 95437)

    def test_part1_solved(self):
        with open(f"day7-input.txt", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day7.part1(puzzle_input), 1743217)

    def test_part2(self):
        self.assertEqual(day7.part2(self.test_input_raw), 24933642)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
