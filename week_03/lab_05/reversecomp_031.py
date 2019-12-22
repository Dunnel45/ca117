#!usr/bin/env python

import sys

def b_search(n, s):
    low = 0
    high = len(n)

    while high > low + 1:
        middle = (high + low) // 2

        if n[middle] > s:
            high = middle
        elif n[middle] < s:
            low = middle
        else:
            return n[middle] == s

def main():
    words = [line.strip() for line in sys.stdin]
    nocase = [w.lower() for w in words]
    print([c for c in words if len(c) >= 5 and b_search(nocase, c.lower()[::-1])])
if __name__ == '__main__':
    main()
