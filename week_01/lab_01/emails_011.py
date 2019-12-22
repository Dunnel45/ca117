#!/usr/bin/env python

import sys

def email(s):
    i = 0
    while i < len(s) and s[i] < "0" or "9" < s[i]:
        i = i + 1

    if i < len(s):
        n = s[:i].strip().split(".")
        forename = n[0]
        surname = n[1]

        return forename.title() + " " + surname.title()

def main():
    for lines in sys.stdin:
        print(email(lines.strip()))

if __name__ == '__main__':
    main()
