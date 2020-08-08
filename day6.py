#!env python3.7


def part1_calc_taxi_dist(a, b):
    """sum of the absolute differences of their Cartesian coordinates

    INPUT: two tuples, like (1, 1), (1, 4)
    RETURN: positive integer, like 3
    """
    try:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    except (TypeError):
        raise TypeError


def part1_parse_input(l_input) -> list:
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
    ret = list()
    for ii in l_input:
        ret.append(
            {
                'loc': tuple(map(int, ii.split(', '))),
                'count_nearest': int(0)
            }
        )
    # todo shortcut: ignore named corners and points on the same X or Y! maybe count_nearest==-1
    return ret
    # return [tuple(map(int, ii.split(', '))) for ii in l_input]


def part1_determine_grid_size(list_of_coords: list) -> dict:
    """
    INPUT: all named coords, like [ {loc: (1, 2), count_nearest: 42}, {}... ]
    RETURN: dict of coords as tuples, like { min_x_y: (?,?), max_x_y: (?,?)}
    """
    ret = dict()

    min_x = min([coord['loc'][0] for coord in list_of_coords])
    min_y = min([coord['loc'][1] for coord in list_of_coords])
    ret['min_x_y'] = (min_x, min_y)

    max_x = max([coord['loc'][0] for coord in list_of_coords])
    max_y = max([coord['loc'][1] for coord in list_of_coords])
    ret['max_x_y'] = (max_x, max_y)

    return ret


def part1_ignore_named_corners(named_coords: list, named_grid_size: dict) -> list:  # todo
    """
    INPUT1: the list of named coords, like [ {loc: (1, 2), count_nearest: 42}, {}... ]
    INPUT2: dict describng named point boundaries, like { min_x_y: (?,?), max_x_y: (?,?)}
    RETURN: the list of named coords, with "count_nearest"=-1 if it is on a boundary
    """
    for ii, named in enumerate(named_coords):
        if (named['loc'][0] == named_grid_size['min_x_y'][0]  # test min_X
            or named['loc'][0] == named_grid_size['max_x_y'][0]  # test max_X
            or named['loc'][1] == named_grid_size['min_x_y'][1]  # test min_Y
                or named['loc'][1] == named_grid_size['max_x_y'][1]):  # test max_Y
            named['count_nearest'] = -1  # assign in loop
            named_coords[ii] = named  # assign in function
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


def part1_brute_force(grid: dict, named_coords: list) -> (dict, list):
    for coord, nearest_named_coord in grid.items():  # grid={ (0,0): 0, (1,0): 0 }
        # breakpoint()
        _distances_to_named = dict()

        # if coord has the same location as a NAMED, then SKIP
        if coord in [named['loc'] for named in named_coords]:
            grid[coord] = -1
            continue

        # named_coords=[ {loc: (1, 2), count_nearest: 42}, {}... ]
        for ii, named in enumerate(named_coords):
            # breakpoint()
            # compute distance to all named coords.
            _distances_to_named[named['loc']] = part1_calc_taxi_dist(coord, named['loc'])
            # NOPE if named['count_nearest']==-1:  # for each named not ignored
            # NOPE    continue  # next named coordinate

        min_dist = None
        # _distances_to_named={(1, 1): 1, (1, 6): 5, (8, 3): 9, (3, 4): 5, (5, 5): 8, (8, 9): 15}
        while _distances_to_named:
            # _distances_to_named is acting as a queue
            ii = _distances_to_named.popitem()
            breakpoint()
            _named_coord = ii[0]
            _dist = ii[1]
            try:
                # if the at least 2 nearest named coords are at same distance,
                if _dist == min(_distances_to_named.values()):  # it's a tie for nearest named coord
                    break  # finish early, do not record a nearest named coord for this GRID POINT
            except ValueError:  # no remaining distances to compare
                pass
            if min_dist is None or _dist < min_dist:
                min_dist = _dist
                # todo figure out how to increment count_nearest ONCE at the end of this WHILE loop=
                #   record the GRID POINTS' nearest named coord, and
                grid[coord] = _named_coord
                #   increment named.x.count_nearest.
                for jj, named in enumerate(named_coords):  # todo terrible
                    if named['loc'] == _named_coord:
                        named_coords[jj]['count_nearest'] += 1  # BUG increments too many times
                # jq .named_coords[].loc[coord] #todo

        # or if the single nearest is an ignored named coord, then
            # record the GRID POINTS' nearest named coord as None
        # otherwise,
    return grid, named_coords


def part1(input):
    """What is the size of the largest area that isn't infinite?

    OUTPUT: int
    """
    _input = input
    named_coords = part1_parse_input(_input)
    named_grid_size = part1_determine_grid_size(named_coords)
    grid = part1_populate_grid(named_grid_size)
    grid, named_coords = part1_brute_force(grid, named_coords)
    named_coords = part1_ignore_named_corners(named_coords, named_grid_size)
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
    return max([l['count_nearest'] for l in named_coords])


def part2(s):
    """
    """
    pass


if __name__ == '__main__':
    file = open('day6-input.txt', 'r')
    linesin = file.read()
    file.close()

    input = linesin.splitlines()
    result1 = part1(input)

    print(f"{result1} is the size of the largest area that isn't infinite.")
    # tried and failed: 95263
    # print("{} is the shortest polymer if all of one type is removed.".format(
    #     part2(input)))
