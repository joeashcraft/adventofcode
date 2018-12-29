#!env python


def part1(s):
    """What remains after fully reacting the polymer?
    The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed.

    INPUT: string
    RETURN: string
    """
    wip_input = list(s)
#     if len(s) < 2:
#         print("done")
#         return s
    # print("Reacting {}".format(''.join(wip_input)))
    for c, v in enumerate(wip_input):
        if c > len(wip_input) - 2:
            print("done 1")
            break
        test_pair = wip_input[c:c + 2]
        # print("Considering Pair {}: {}".format(c, ''.join(test_pair)))
        if test_pair[0].lower() == test_pair[1].lower():
            # print("Pair {} {} is a candidate".format(c, ''.join(test_pair)))
            if (test_pair[0].isupper() and test_pair[1].islower()) or (test_pair[0].islower() and test_pair[1].isupper()):
                # print("Pair {} {} have reacted".format(c, ''.join(test_pair)))
                wip_input.pop(c)
                wip_input.pop(c)
                # print("After a Reaction: {}".format(''.join(wip_input)))
                return part1(''.join(wip_input))
            # else:
                # print("Pair {} {} have NOT reacted".format(c, ''.join(test_pair)))
        elif c + 2 == len(wip_input):
            # print("done 2")
            return s


def part2(s):
    """What is the length of the shortest polymer you can produce by removing
    all units of exactly one type and fully reacting the result?

    INPUT: string
    OUTPUT: int
    """
    pass


if __name__ == '__main__':
    file = open('day5-input.txt', 'r')
    linesin = file.read()
    file.close()

    input = linesin.splitlines()[0]

    print("{} units remain after fully reacting the polymer.".format(
        len(part1(input))))
