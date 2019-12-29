#!/usr/bin/env python

import sys

def main():
    counter = 0
    for lines in sys.stdin:
        for words in lines:
            if words.endswith(' '):
                counter = counter + 1
    print(counter)

if __name__ == '__main__':
    main()
