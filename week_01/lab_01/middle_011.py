#!/usr/bin/env python

import sys

def mid(s):
    if len(s) % 2 != 0:
        return(s[len(s)//2])
    else:
        return('No middle character!')

def main():
    for lines in sys.stdin:
        words = mid(lines.strip())
        print(words)
if __name__ == '__main__':
    main()
