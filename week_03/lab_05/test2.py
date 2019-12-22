#!usr/bin/env pyth
import sys

def rmax(l):
    if len(l) == 1:
        return l[0]

    max_l = rmax(l[:-1])
    if l[-1] > max_l:
        return l[-1]
    else:
        return max_l

def main():
    print(rmax([4,1,3,9,7]))

if __name__ == '__main__':
    main()
