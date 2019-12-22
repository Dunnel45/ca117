#!/usr/bin/env python

import sys

def main():
    for lines in sys.stdin:
        words = lines.strip().title()
        print(words)    

if __name__ == '__main__':
    main()