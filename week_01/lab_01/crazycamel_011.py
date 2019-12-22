#!/usr/bin/env python

import sys

def case(s):
    rev = s[::-1].title()
    nor = rev[::-1]
    return nor

def main():
    for lines in sys.stdin:
        words = case(lines.strip())
        print(words)

if __name__ == '__main__':
    main()