#!env python3.7

import unittest
from day6 import part1, part1_parse_input, part1_calc_taxi_dist, part1_determine_grid_size, part1_populate_grid, part1_ignore_named_corners


class MyFirstTests(unittest.TestCase):
    test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    my_input = test_input.splitlines()

    expected_named_coords=[
        {'loc': (1, 1), 'count_nearest': 0},
        {'loc': (1, 6), 'count_nearest': 0},
        {'loc': (8, 3), 'count_nearest': 0},
        {'loc': (3, 4), 'count_nearest': 0},
        {'loc': (5, 5), 'count_nearest': 0},
        {'loc': (8, 9), 'count_nearest': 0},
    ]
    expected_grid_size={
      'min_x_y': (1,1),
      'max_x_y': (8,9)
    }
    expected_small_grid_size={
        'min_x_y': (0,0),
        'max_x_y': (1,2)
    }
    expected_small_grid={
        (0, 0): 0,
        (0, 1): 0,
        (0, 2): 0,
        (0, 3): 0
    }

    def test_part1_helpers(self):
        self.assertEqual(
            part1_parse_input(self.my_input),
            self.expected_named_coords
        )
        self.assertEqual(
            part1_calc_taxi_dist((-3, 1), (2, 3)), 7)
        self.assertEqual(
              part1_calc_taxi_dist((1, 1), (1, 4)),
            3)
        self.assertIsInstance(
            part1_determine_grid_size(self.expected_named_coords),
            dict
        )
        self.assertEqual(
            part1_determine_grid_size(self.expected_named_coords),
            self.expected_grid_size
        )

        self.assertEqual(
            part1_populate_grid(
                {
                  'min_x_y': (0,0),
                  'max_x_y': (1,2)
                }
            ),
            {
                (0, 0): 0, (0, 1): 0, (0, 2): 0,
                (1, 0): 0, (1, 1): 0, (1, 2): 0
            }
        )
        self.assertEqual(
            part1_ignore_named_corners(
                self.expected_named_coords,
                self.expected_grid_size
            ),
            [
                {'loc': (1, 1), 'count_nearest': -1},
                {'loc': (1, 6), 'count_nearest': -1},
                {'loc': (8, 3), 'count_nearest': -1},
                {'loc': (3, 4), 'count_nearest': 0},
                {'loc': (5, 5), 'count_nearest': 0},
                {'loc': (8, 9), 'count_nearest': -1},
            ]
        )

    def test_part1(self):
        self.assertEqual(part1(self.test_input.splitlines()), 17)

    # def test_part2(self):
    #     self.assertEqual(part2(self.test_input), 4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
