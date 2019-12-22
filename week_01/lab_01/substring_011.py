#!/usr/bin/env python

import sys

def main():
    for lines in sys.stdin:
        sub, word = lines.strip().casefold().split()
        test = word.find(sub)
        if test != -1:
            print('True')
        else:
            print('False')
if __name__ == '__main__':
    main()
