#!/usr/bin/env python

import sys

def conv(num):
    dig = num[0]
    base = num[1]
    dec = int(dig, int(base))
    return dec

def main():
    for lines in sys.stdin:
        num = lines.strip().split()
        print(conv(num))
if __name__ == '__main__':
    main()
