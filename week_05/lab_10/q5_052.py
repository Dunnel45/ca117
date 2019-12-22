#!usr/bin/env python

import sys

def main():
    students = {}
    skipped = []
    for lines in sys.stdin:
        try:
            chars = lines.strip().split(':')
            names, marks = chars[0], chars[1]
            marks = marks.strip().split(',')
            total = 0
            for num in marks:
                total += int(num)
            students[names] = total
        except ValueError:
            skipped.append(names)
            continue
    for (k, v) in sorted(students.items(), key=lambda x: x[1], reverse=True):
        print('{} : {}'.format(k, v))
    print('Skipped:')
    for s in skipped:
        print(s)
if __name__ == '__main__':
    main()
