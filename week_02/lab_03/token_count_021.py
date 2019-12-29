#!/usr/bin/env python

import sys

def main():
    lines = []
    for words in sys.stdin:
        spaces = words.split()
        for chars in spaces:
            lines.append(chars)

    print(len(lines))

if __name__ == '__main__':
    main()
