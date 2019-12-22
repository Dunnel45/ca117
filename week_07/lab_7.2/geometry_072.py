
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def distance(self, other):
        x_distance = (self.x - other.x) ** 2
        y_distance = (self.y - other.y) ** 2

        distance = (x_distance + y_distance) ** (1 / 2)
        return(distance)

    def __str__(self):
        return('({:.1f}, {:.1f})'.format(self.x, self.y))


class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        s = self.p1
        e = self.p2

        x_distance = (s.x + e.x) / 2
        y_distance = (s.y + e.y) / 2

        return('({:.1f}, {:.1f})'.format(x_distance, y_distance))

    def length(self):
        return((self.p1).distance(self.p2))


class Circle(object):

    def __init__(self, point, radius):
        self.radius = int(radius)
        self.centre = point

    def overlaps(self, other):
        total_radius = self.radius + other.radius

        distance = ((self.centre).distance(other.centre))

        return(total_radius > distance)
