from stack_092 import Stack

un = "nr"
bi = "+-*/"

uniops = {
    "n": lambda x: -x,
    "r": lambda x: x ** 0.5
}

binops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}


def is_num(s):
    try:
        x = float(s)
        return True
    except ValueError:
        return False


def calculator(line):
    chars = line.split()

    s = Stack()

    for c in chars:
        if is_num(c):
            s.push(float(c))
        elif c in un:
            s.push(float(uniops[c](s.pop())))
        elif c in binops:
            b = s.pop()
            s.push(float(binops[c](s.pop(), b)))

    return s.top()
