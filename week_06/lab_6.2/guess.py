from random import randint
from guess_062 import find
top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

def find():
    top = 1000000
    bottom = 0
    while top > bottom:
        middle = int((top + bottom) / 2)
        estimate = guess(middle)
        if estimate == 1:
            top = middle
        elif estimate == -1:
            bottom = middle
        else:
            return middle

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
