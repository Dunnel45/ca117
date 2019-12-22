#!/usr/bin/env python

import sys

def main():
    for lines in sys.stdin:
        words = lines.strip()
        chop = words[1:-1]
        if chop:
            print(chop)
if __name__ == '__main__':
    main()
