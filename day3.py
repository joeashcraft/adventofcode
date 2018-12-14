#!env python
"""Day 3, Part 1: No Matter How You Slice It

How many square inches of fabric are within two or more claims?
INPUT: list of claims.
RETURN: integer amount of square inches which are within 2+ claims.

Each claim's rectangle is defined as follows:
* The number of inches between the left edge of the fabric and
    the left edge of the rectangle.
* The number of inches between the top edge of the fabric and
    the top edge of the rectangle.
* The width of the rectangle in inches.
* The height of the rectangle in inches.

Sample Claim: #1 @ 53,238: 26x24
where
    claimId is 1.
    claim begins
        53-inches from left, and
        238-inches from top.
    claim is
        26-inches wide, and
        24-inches tall.
"""


def part1_parse_claims_list(claims_list):
    """INPUT: list of strings. e.g. [ '#1 @ 53,238: 26x24', ... ]
    RETURN: list of dicts. e.g. [ {id: 1, x: 53, y: 238, w: 26, h: 24}, ... ]
    """
    claims = list()  # [ {id: 1, x: 53, y: 238, w: 26, h: 24}, ... ]

    for claim in claims_list:
        this_claim = dict()

        this_claim['id'] = int(claim.split()[0].split('#')[1])
        this_claim['x'] = int(claim.split()[2].split(',')[0])
        this_claim['y'] = int(claim.split()[2].split(',')[1].split(':')[0])
        this_claim['w'] = int(claim.split()[3].split('x')[0])
        this_claim['h'] = int(claim.split()[3].split('x')[1])
        claims.append(this_claim)

    return claims


def part1_claim_to_coords(claim_dict):
    """Take a list of claims and list all the X,Y coords included.

    INPUT: dicts (parsed claims list).
           e.g. {'id': 123, 'x': 3, 'y': 2, 'w': 5, 'h': 4}
    RETURN: list of lists of tuples
            e.g. [ (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                   (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                   (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                   (4, 6), (5, 6), (6, 6), (7, 6), (8, 6) ]
    """
    coords = list()

    # for claim in claims_dicts:  # e.g. {id: 1, x: 53, y: 238, w: 26, h: 24}
    for yy in range(claim_dict['y'], claim_dict['y'] + claim_dict['h']):
        for xx in range(claim_dict['x'], claim_dict['x'] + claim_dict['w']):
            coords.append(tuple([xx + 1, yy + 1]))

    return coords


def part1(claims_list):
    """INPUT: list of strings. e.g. [ '#1 @ 53,238: 26x24', ... ]
    RETURN: int amt of overlap."""
    amt_of_overlap = 0
    claims_coords = list()
    unique_coords = set()

    claims_dicts = part1_parse_claims_list(claims_list)

    for claim in claims_dicts:
        claims_coords.extend(part1_claim_to_coords(claim))

    for coord in claims_coords:
        if coord in unique_coords:
            amt_of_overlap += 1
        else:
            unique_coords.add(coord)
    return amt_of_overlap


if __name__ == '__main__':
    file = open('day3-input.txt', 'r')
    linesin = file.read()
    file.close()

    claims_list = [ii for ii in linesin.splitlines()]

    print("{} square inches are claimed by 2 or more elves".format(
        part1(claims_list)))
