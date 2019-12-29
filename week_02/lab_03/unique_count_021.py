#!/usr/bin/env python

import sys
from string import punctuation

def main():
    word = sys.stdin.readlines

    uni = []
    for chars in word:
        if chars in punctuation:
            word = word.replace(chars, '')

    no_case = word.strip().casefold()
    for i in range(len(no_case)):
        if no_case[i].isalnum() and no_case[i] not in uni:
            uni.append(no_case)
    print(len(uni))
if __name__ == '__main__':
    main()
