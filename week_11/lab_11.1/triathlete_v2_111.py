class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def __str__(self):
        l = []
        l.append('Name: {}'.format(self.name))
        l.append('ID: {}'.format(self.tid))
        l.append('Race time: {}'.format(self.total()))
        return '\n'.join(l)

    def add_time(self, sport, time):
        self.d[sport] = int(time)

    def get_time(self, sport):
        return self.d[sport]

    def total(self):
        total = 0
        for v in self.d.values():
            total += int(v)
        return total
