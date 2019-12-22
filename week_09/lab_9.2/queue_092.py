class Queue(object):

    def __init__(self):
        self.l = []

    def enqueue(self, num):
        self.l.append(num)

    def dequeue(self):
        a = []
        a.append(self.l[0])
        del self.l[0]
        for o in a:
            return o

    def first(self):
        return self.l[0]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
