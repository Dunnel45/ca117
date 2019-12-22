#!usr/bin/env pyth
import sys

file = sys.argv[1]
pass_fail = None
try:
    with open(file, 'r') as f:
        for line in f:
            line = line.split()
            mark = line[-1]
            student = ' '.join(line[1:-1])
            try:
                if int(mark) >= 40:
                    pass_fail = 'Passed'
                else:
                    pass_fail = 'Failed'
                print('{} {} with a mark of {}'.format(student, pass_fail, mark))

            except ValueError:
                print('Invalid mark encountered: {}'.format(mark))
except FileNotFoundError:
    print('No file')
