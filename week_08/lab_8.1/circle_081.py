class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return 'Point: ({}, {})'.format(self.x, self.y)

    def midpoint(self, other):
        return (self.x + other.x) / 2, (self.y + other.y) / 2


class Circle(object):

    def __init__(self, Centre=Point(0, 0), radius=0):
        self.radius = int(radius)
        self.Centre = Centre

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})\nRadius: {}'.format(self.Centre.x, self.Centre.y, self.radius)

    def __add__(self, other):
        r = self.radius + other.radius
        tx, ty = Point.midpoint(self.Centre, other.Centre)

        return Circle(Point(tx, ty), r)
