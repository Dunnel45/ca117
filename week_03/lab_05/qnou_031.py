#!usr/bin/env python

import sys

def q_no_u(w):
    w = w.replace('qu', '--')
    return 'q' in w

def main():
    l = []
    for lines in sys.stdin:
        if q_no_u(lines.casefold()):
            l.append(lines.strip())
    print('Words with q but no u:', l)

if __name__ == '__main__':
    main()
