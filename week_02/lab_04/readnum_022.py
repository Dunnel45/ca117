#!/usr/bin/env python

import sys

for lines in sys.stdin:
    try:
        char = int(lines.strip())
        if str(char).isdecimal():
            print('Thank you for', lines.strip())
            break

    except ValueError:
        print(lines.strip(), 'is not a number')
