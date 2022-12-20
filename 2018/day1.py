#!env python

def part1(list):
    return sum(list)

def part2(list):
    run_tot = 0
    results = set([run_tot])

    while True:
        #for int in list,
        for ii in list:
        #add to running
            run_tot += ii
            #if new total is in set, then DONE
            if run_tot in results:
                #print("WINNER: " + str(run_tot))
                return run_tot
            else:
                #otherwise, append to set
                results.add(run_tot)
        #else:
        #    print("no dup result found")


if __name__ == '__main__':
    file = open('day1-input.txt', 'r')
    linesin = file.read()
    file.close()

    freqs = []
    [ freqs.append(int(ii)) for ii in linesin.splitlines() ]

    print(part1(freqs))
    print(part2(freqs))

