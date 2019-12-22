class Point(object):

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distance(self, other):
        x_distance = (self.x - other.x) ** 2
        y_distance = (self.y - other.y) ** 2

        distance = (x_distance + y_distance) ** (1 / 2)
        return(float(distance))

class Shape(object):

    def __init__(self, p):
        self.points = p

    def sides(self):
        l = []

        for i in range(0, len(self.points) - 1):
            l.append(self.points[i].distance(self.points[i + 1]))
            i += 1

        l.append(self.points[-1].distance(self.points[0]))
        return l

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):

    def area(self):
        sides = self.sides()
        s = (sum(sides)) / 2
        return (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** (1 / 2)

class Square(Shape):

    def area(self):
        sides = self.sides()[0]
        return sides ** 2
