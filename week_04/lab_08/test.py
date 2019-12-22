#!usr/bin/env python

import sys
import swap_v2_042 as swap

def main():
    my_dict = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
    new_dict = swap.swap_unique_keys_values(my_dict)
    print(new_dict)

if __name__ == '__main__':
    main()
