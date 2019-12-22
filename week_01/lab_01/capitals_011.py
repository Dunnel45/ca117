#!/usr/bin/env python

import sys

def main():
    for lines in sys.stdin:
        words = lines.strip().upper()
        for chars in words:
            if chars != words[0] or words[-1]:
                words = chars.lower()
        if len(words) >= 2:
            print(words)
if __name__ == '__main__':
    main()
