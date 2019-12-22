#!usr/bin/env python

def swap_unique_keys_values(d):
    s = {}
    for k in d:
        if d[k] in s:
            del(s[d[k]])
        else:
            s[d[k]] = k
    return s
