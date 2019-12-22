#!/usr/bin/env python

import sys

def foo(x, l=0):
    p = []
    if l == 0:
        p.append(x)
        return p
    else:
        l.append(x)
        return l

def main():
    print(foo('bee'))
    print(foo('fox', ['hen']))
    print(foo('ant'))

if __name__ == '__main__':
    main()
