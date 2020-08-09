#!env python3.7
import logging

def part1_calc_taxi_dist(a, b):
    """sum of the absolute differences of their Cartesian coordinates

    INPUT: two tuples, like (1, 1), (1, 4)
    RETURN: positive integer, like 3
    """
    try:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    except (TypeError):
        raise TypeError


def part1_parse_input(l_input) -> dict:
    """
    INPUT: list of strings, like ['1, 1', '1, 4']
    RETURN: list of dicts, like [ {loc: (1, 2), count_nearest: 42}, {}... ]
        INDEX: arbitrary "name" of coord
        VALUE: dictionary with two items:
            K1: "loc"
            V1: the location as tuple([x,y])
            K2: "count_nearest"
            V2: count of nearest coords as integer, or -1 for infinite
    """
    ret = dict()

    for ii in l_input:
        # breakpoint()
        # x=ii.split(', ')[0]
        # y=ii.split(', ')[1]
        ret[tuple(map(int, ii.split(', ')))] = 0
        # ret[tuple(map(int, ii.split(', ')))]=0
    # todo shortcut: ignore named corners and points on the same X or Y! maybe count_nearest==-1
    return ret
    # return [tuple(map(int, ii.split(', '))) for ii in l_input]


def part1_determine_grid_size(named_coords: dict) -> dict:
    """
    INPUT: all named coords, like {(300, 90): 0, (300, 60): 0, (176, 327): 0, ...}
    RETURN: dict of coords as tuples, like { min_x_y: (?,?), max_x_y: (?,?)}
    """
    ret = dict()

    # min_x = min([coord[0] for coord in named_coords])
    # min_y = min([coord[1] for coord in named_coords])
    ret['min_x_y'] = (0, 0)

    max_x = max([coord[0] for coord in named_coords])
    max_y = max([coord[1] for coord in named_coords])
    ret['max_x_y'] = (max_x, max_y)

    return ret


def part1_ignore_infinite_areas(named_coords: dict, named_grid_size: dict) -> dict:
    """
    INPUT1: the dict of named coords, like {(1, 2): 42, ... }
    INPUT2: dict describing named point boundaries, like { min_x_y: (?,?), max_x_y: (?,?)}
    RETURN: the dict of named coords, with "count_nearest"=-1 if it is on a boundary
    """

    for x,y in named_coords:
        if (x == named_grid_size['min_x_y'][0]  # test min_X
            or x == named_grid_size['max_x_y'][0]  # test max_X
            or y == named_grid_size['min_x_y'][1]  # test min_Y
                or y == named_grid_size['max_x_y'][1]):  # test max_Y
            named_coords[(x, y)] = -1
    return named_coords


def part1_populate_grid(min_max: dict) -> dict:
    """
    INPUT: dict of grid size
    RETURN: dict of all grid points and their nearest named coord initialized to 0, like
        { (0,0): 0, (1,0): 0 }
    """
    ret = dict()
    for x in range(min_max['min_x_y'][0], min_max['max_x_y'][0]+1):  # for x from min_x to max_x inclusive
        for y in range(min_max['min_x_y'][1], min_max['max_x_y'][1]+1):  # for y from min_y to max_y inclusive
            ret[(x, y)] = 0

    return ret


def part1_check_if_ignored(s) -> bool:
    return False


def part1_brute_force(grid: dict, named_coords: dict, named_grid_size: dict) -> (dict, list):
    for coord, nearest_named_coord in grid.items():  # grid={ (0,0): 0, (1,0): 0 }
        logging.debug(f'coord {coord}')
        x=coord[0]
        y=coord[1]
        # for every Grid Coordinate
        # breakpoint()
        _distances_to_named = dict()

        # if coord has the same location as a NAMED, then SKIP
        if coord in [c for c in named_coords]:
            grid[coord] = 'self'
            named_coords[(coord)] += 1
            continue

        # named_coords={(1, 2): 42}, ... }
        # breakpoint()
        for c in named_coords:
            # compute distance to all named coords.
            _distances_to_named[c] = part1_calc_taxi_dist(coord, c)
            # NOPE if named['count_nearest']==-1:  # for each named not ignored
            # NOPE    continue  # next named coordinate

        # maybe... get min dist, if dupe, then delete all dupes and start over
        # while _distances_to_named:
            # ii = _distances_to_named.popitem()
            # breakpoint()
            # _named_coord = ii[0]
            # _dist = ii[1]

        # _distances_to_named={(1, 1): 1, (1, 6): 5, (8, 3): 9, (3, 4): 5, (5, 5): 8, (8, 9): 15}
        sv = sorted(_distances_to_named.values())
        min_dist = min(sv)
        if sv[0] == sv[1]:  # if the at least 2 nearest named coords are at same distance,
            # it's a tie for nearest named coord
            logging.debug(f'coord {coord} is equidistant--{min_dist}--between named coords')
            grid[coord] = '.'  # record nearest as dot
            continue  # finish early, go to next GRID COORD

        # this is dangerous IFF dupe values for min(sv), but we checked for that
        flipped = {v: k for k, v in _distances_to_named.items()}
        min_coord = flipped[min_dist]
        grid[coord] = min_coord  # record nearest as (x,y)
        logging.debug(f'grid coord {coord} is nearest to named coord {min_coord}')

        # if COORD is on boundary, then mark NEAREST NAMED as infinite
        if named_coords[(min_coord)] == -1:
            logging.debug(f'coord {coord} is in infinite space')
            continue
        elif (x == named_grid_size['min_x_y'][0]  # test min_X
            or x == named_grid_size['max_x_y'][0]  # test max_X
            or y == named_grid_size['min_x_y'][1]  # test min_Y
            or y == named_grid_size['max_x_y'][1]):  # test max_Y
            logging.debug(f'coord {coord} is on a boundary, mark area of {min_coord} as infinite')
            named_coords[(min_coord)] = -1
        else:
            logging.debug(f'coord {coord} is not in infinite space')
            named_coords[(min_coord)] += 1

        # try:
        #     if _dist == min(_distances_to_named.values()):
        #         break
        # except ValueError:  # no remaining distances to compare
        #     pass
        # if min_dist is None or _dist < min_dist:
        #     min_dist = _dist
        #     # todo figure out how to increment count_nearest ONCE at the end of this WHILE loop=
        #     #   record the GRID POINTS' nearest named coord, and
        #     grid[coord] = _named_coord
        #     #   increment named.x.count_nearest.
        #     for jj, named in enumerate(named_coords):  # todo terrible
        #         if named['loc'] == _named_coord:
        #             named_coords[jj]['count_nearest'] += 1  # BUG increments too many times
        #     # jq .named_coords[].loc[coord] #todo

        # or if the single nearest is an ignored named coord, then
        # record the GRID POINTS' nearest named coord as None
        # otherwise,
    return grid, named_coords


def part1(input):
    """What is the size of the largest area that isn't infinite?

    OUTPUT: int
    """
    _input = input  # EXPECTS: ['300, 90', '300, 60', '176, 327', ...]
    named_coords = part1_parse_input(_input)  # RETURNS: {(300, 90): 0, (300, 60): 0, (176, 327): 0, ... }
    named_grid_size = part1_determine_grid_size(named_coords)  # RETURNS: {'min_x_y': (53, 42), 'max_x_y': (358, 353)}
    grid = part1_populate_grid(named_grid_size)  # RETURNS: {(53, 42): 0, (358, 352): 0, (358, 353): 0, ...}
    grid, named_coords = part1_brute_force(grid, named_coords, named_grid_size)
    # named_coords = part1_ignore_infinite_areas(named_coords, named_grid_size)
    # breakpoint()

    # named_coords_without_inf=[]
    # for l in named_coords:
    #     if (l['loc'][0] == max_grid_size['min_x_y'][0]
    #         or l['loc'][0] == max_grid_size['max_x_y'][0]
    #         or l['loc'][1] == max_grid_size['min_x_y'][1]
    #         or l['loc'][1] == max_grid_size['max_x_y'][1]):
    #         continue
    #     else:
    #         named_coords_without_inf.append(l)

    # return max([ l['count_nearest'] for l in named_coords_without_inf ])
    breakpoint()
    logging.info(named_coords)
    return max(named_coords.values())


def part2(s):
    """
    """
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    file = open('day6-input.txt', 'r')
    linesin = file.read()
    file.close()

    input = linesin.splitlines()
    result1 = part1(input)

    print(f"{result1} is the size of the largest area that isn't infinite.")
    # tried and failed: 95263 (too high!)
    # 2020-08-08 try 3630 FAIL (too high!)
    # 2020-08-08 try 3629 FAIL (too high!)
    # 2020-08-08 try 3314 FAIL (unknown)
    # 2020-08-09 try 3260 SUCCESS! (228, 221)
    #todo  my shrinking of the GRID SIZE was a logic fail. I cut off large areas _and_ did not detect enough infinites.
    #see file:///Users/joe6623/Pictures/Screenshots/Screen%20Shot%202020-08-09%20at%2000.17.12.png
    #on detecting infinite areas... use a grid size from (-1,-1) and
        # mark as infinite any area that includes (-1,*) or (*,-1) or (*,max_y+1) or (max_x+1,*)

    # print("{} is the shortest polymer if all of one type is removed.".format(
    #     part2(input)))
