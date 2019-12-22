from stack_092 import Stack

def matcher(line):
    d = {')': '(',
         '}': '{',
         ']': '['}

    s = Stack()

    for c in line:
        if c in d.values():
            s.push(c)

        elif c in d.keys():
            if s.is_empty():
                return False
            if s.top() != d[c]:
                return False
            s.pop()

    return s.is_empty()
