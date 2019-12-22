
def find():
    top = 1000000
    bottom = 0
    while top > bottom:
        middle = int((top + bottom) / 2)
        g = guess(middle)

        if g == 1:
            top = middle

        elif g == -1:
            bottom = middle

        else:
            return middle
