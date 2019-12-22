#!usr/bin/env python

import sys

def sec(s):
    chars = s.split(':')
    mins, secs = chars[0], chars[1]
    con = int(mins) * 60
    total = con + int(secs)
    return total

def main():
    times = {}
    for lines in sys.stdin:
        try:
            words = lines.split()
            times[words[0]] = min(words[1:], key=sec)
        except ValueError:
            continue
        mi = min(times.items(), key=lambda x: sec(x[1]))
    print(mi[0] + ' : ' + mi[1])

if __name__ == '__main__':
    main()
