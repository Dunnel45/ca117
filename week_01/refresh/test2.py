#!/usr/bin/env python

import sys

def main():
    for lines in sys.stdin:
        lines = lines.strip().split()
        for numbers in lines:
            if int(numbers) % 2 != 0:
                print(numbers)

if __name__ == '__main__':
    main()
