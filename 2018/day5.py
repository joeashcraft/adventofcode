#!env python


def part1_test_if_pair(x, y):
    if (x.lower() == y.lower()) and \
        (
            (x.isupper() and y.islower()) or
            (x.islower() and y.isupper())
    ):
        return True
    else:
        return False

def react(line):
    buf = []
    # print("BEGIN")
    for c in line:
        # print("  for loop: {} of {}".format(c, len(line)-1))
        # print(buf)
        if buf and part1_test_if_pair(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return buf

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
    for c in range(len(wip_input)):
        print("for loop: {} of {} for {}".format(c+1, len(wip_input)-1, wip_input))
        test_pair = wip_input[c:c + 2]
        if len(test_pair) < 2:
            print("    done 1")
            return wip_input
        print("  Considering Pair {}: {}".format(c+1, ''.join(test_pair)))
        if part1_test_if_pair(*test_pair):
            print("    Pair {} {} have reacted".format(c+1, ''.join(test_pair)))
            wip_input.pop(c)
            wip_input.pop(c)
            print("    After a Reaction: {}".format(''.join(wip_input)))
            # return part1(''.join(wip_input))
            continue
        else:
            print("    Pair {} {} have NOT reacted".format(c+1, ''.join(test_pair)))
            if c+2 >= len(wip_input):
                print("    done - reached end")
                return wip_input
            else:
                print("    done - catch all")
            # print('.', end='')
        # else:
        #     return part1(''.join(wip_input))
    # else:
        # return wip_input


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
        len(react(input))))
    # print("{} units remain after fully reacting the polymer.".format(
        # len(part1(input))))
    # print("{} is the shortest polymer if all of one type is removed.".format(
    #     part2(input)))
