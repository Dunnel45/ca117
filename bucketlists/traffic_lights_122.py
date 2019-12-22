#!usr/bin/env python

import sys
def main():
    dist = sys.stdin.readline()
    dist = int(dist)

    d = 0
    mins = 0
    dif = 0
    for lines in sys.stdin:
        line = lines.strip().split()
        d, r, g = int(line[0]), int(line[1]), int(line[2])
        mins = mins + (d - dif)
        wait_time = mins - (r + g) * (mins // (r + g))
        if wait_time < r:
            oth = (r - wait_time)
            mins = mins + oth
        dif = d
    mins = mins + (dist - d)
    print(mins)

if __name__ == '__main__':
    main()
