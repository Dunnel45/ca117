#!usr/bin/env python

import sys

def main():
    vowels = 'aeiou'
    lines = sys.stdin.read().strip().lower()
    total = [lines.count(l) for l in vowels]

    d = {}
    for i in range(len(total)):
        d[vowels[i]] = total[i]

    longest = len(str(max(total)))
    for (k, v) in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print('{} : {:>{}}'.format(k, v, longest))

if __name__ == '__main__':
    main()
