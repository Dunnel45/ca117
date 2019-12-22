#!usr/bin/env python

import sys

def allvowels(w):
    return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w

def anagram(w):
    return 'a' in w and 'n' in w and 'g' in w and 'l' in w and 'e' in w and len(w) == 5 and w != 'angle'

def main():
    words = [line.strip() for line in sys.stdin]
    w17 = [l for l in words if len(l) == 17]
    w18 = [l for l in words if len(l) >= 18]
    vw = [l for l in words if allvowels(l.lower())]
    mini = min(vw, key=len)

    fouras = [l for l in words if l.lower().count('a') == 4]
    q2 = [l for l in words if l.lower().count('q') >= 2]
    cie = [l for l in words if 'cie' in l]
    angle = [l for l in words if anagram(l.lower())]
    end_iary = [l for l in words if l.endswith('iary')]
    es = [l for l in words if all(l.lower().count('e') >= prev.lower().count('e') for prev in words)]

    print('Words containing 17 letters:', w17)
    print('Words containing 18+ letters:', w18)
    print('Shortest word containing all vowels:', mini)
    print("Words with 4 a's:", fouras)
    print("Words with 2+ q's:", q2)
    print("Words containing cie:", cie)
    print("Anagrams of angle:", angle)
    print("Words ending in iary:", str(len(end_iary)))
    print("Words with most e's:", es)

if __name__ == '__main__':
    main()
