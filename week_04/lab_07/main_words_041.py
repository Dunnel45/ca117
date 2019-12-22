#!usr/bin/env python

import sys
from string import punctuation

def no_punc(s):
    for chars in s:
        if chars in punctuation and chars != "'":
            s = s.replace(chars, '')
    return s

def main():
    count = {}
    lines = sys.stdin.read().strip().lower().split()
    clean = [no_punc(l) for l in lines]

    for i in range(len(clean)):
        if clean[i] in count:
            count[clean[i]] += 1
        else:
            count[clean[i]] = 1

    words = {}
    for (k, v) in sorted(count.items()):
        if len(k) > 3 and int(v) >= 3:
            words[k] = v

    biggest = len(max(words, key=len))
    for (key, value) in sorted(words.items()):
        print('{:>{}} : {:>2}'.format(key, biggest, value))

if __name__ == '__main__':
    main()
