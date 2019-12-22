#!usr/bin/env python

import sys
d = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}

def get_irish(file):
    irish = {}
    with open(file, 'r') as f:
        for lines in f:
            chars = lines.split()
            irish[chars[0]] = chars[1]
        return irish
def main():
    irish = get_irish(sys.argv[1])
    for lines in sys.stdin:
        line = lines.strip().split()
        translation = []
        for numbers in line:
            try:
                translation.append(irish[d[(numbers)]])
            except (KeyError, ValueError):
                translation.append('unknown')
        print(' '.join(translation))
if __name__ == '__main__':
    main()
