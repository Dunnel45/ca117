#!usr/bin/env python

import sys

def main():
    people = {}
    cal_count = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            chars = line.split()
            foods, calories = ' '.join(chars[:-1]), chars[-1]
            cal_count[foods] = calories
    for lines in sys.stdin:
        l = lines.strip().split(',')
        names, eaten = l[0], l[1:]
        cals = 0
        for foods in eaten:
            if foods in cal_count:
                cals = int(cal_count[foods]) + cals
            else:
                cals = cals + 100
        people[names] = cals

    max_k = len(max(people, key=len))
    values = []
    for v in people.values():
        v = str(v)
        values.append(v)
    max_v = len(max(values, key=len))
    for (k, v) in sorted(people.items(), key=lambda x: x[1]):
        print('{:>{}} : {:>{}}'.format(k, max_k, v, max_v))

if __name__ == '__main__':
    main()
