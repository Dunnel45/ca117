#!/usr/bin/env python

import sys
import math

def main():
    dec = int(sys.argv[1])
    print('{:.{}f}'.format(math.pi, dec))

if __name__ == '__main__':
    main()
