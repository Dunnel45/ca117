#!/usr/bin/env python

import sys

def main():
    h1 = 'POS'
    h2 = 'CLUB'
    h3 = 'P'
    h4 = 'W'
    h5 = 'D'
    h6 = 'L'
    h7 = 'GF'
    h8 = 'GA'
    h9 = 'GD'
    h10 = 'PTS'

    pos = []
    clubs = []
    formatted_rows = []

    for line in sys.stdin:
        pos.append(line.rstrip('\n'))
    for i in range(len(pos)):
        pos[i] = pos[i].split()
        club = " ".join(pos[i][1:-8])
        pos[i][1] = club
        del pos[i][2:-8]
        clubs.append(club)
        longestword = len(max(clubs, key = len))
        print('{:>3s} {:>3s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

    for i in pos:
        sys.stdout.write('{:>3} {:<{}} {:>2}'.format(i[0], i[1], longestword, i[2]))
        for j in range(3, len(i)):
            sys.stdout.write('{:>4}'.format(i[j]))
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
