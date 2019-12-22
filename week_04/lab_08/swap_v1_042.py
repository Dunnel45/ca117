#!usr/bin/env python

def swap_keys_values(d):
    s = {}
    for (k, v) in d.items():
        s[v] = k
    return s
