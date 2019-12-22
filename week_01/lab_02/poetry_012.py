#!/usr/bin/env python

import sys

def main():
    maxi = 0
    poem = []
    for lines in sys.stdin:
        l = lines.strip()
        poem.append(l)

        if len(l) > maxi:
            maxi = len(l)

    for l in poem:
        print('{:^{}}'.format(l, maxi))

if __name__ == '__main__':
    main()
