#!usr/bin/env python

import sys
def main():
    lights = []
    numbers = sys.stdin.readlines()
    road_distance = int(numbers[0].strip())
    n = numbers[1:]
    
    try:
        for i in range(n):
            [d, r, g] = n[i].strip().split()
            rem = int(r) - int(d)
            ans = road_distance + rem
        print(ans)
    except IndexError:
        print(road_distance)
if __name__ == '__main__':
    main()
