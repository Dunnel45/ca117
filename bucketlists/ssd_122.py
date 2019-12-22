#!usr/bin/env python

import sys

def index(d):
    num = int(d[0])
    b = int(d[1])
    i = 0
    while b ** i < num:
        i = i + 1
    return i - 1

def dig(n, s):
    num = int(s[0])
    b = int(s[1])
    l = []
    i = 0
    while i <= n:
        number = (num // (b ** (n - i)))
        l.append(int(number))
        num = (num - ((b ** (n - i)) * number))
        i = i + 1
    return l

def ans(i):
    fig = 0
    for tokens in i:
        fig = fig + tokens ** 2
    return fig

def main():
    lines = sys.stdin.readlines()
    try:
        l = []
        i = 0
        for words in lines:
            try:
                words = lines[i].strip().split()
                power = index(words)
                figlist = dig(power, words)
                print(ans(figlist))

            except ValueError:
                l.append(i)
            i = i + 1
    finally:
        if len(l) > 0:
            a = []
            i = 0
            while i < len(l):
                a.append(str(l[i] + 1))
                i = i + 1
            print('Failed to convert line(s): ' + ', '.join(a) + ' ')

if __name__ == '__main__':
    main()
