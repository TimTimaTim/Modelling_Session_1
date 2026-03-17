# class - needs to start with letter or underscore (capital first letter to indicate it is a class)
class Point:
    def __init__(self, x, y):
        # __xxxx__ is a magic operator: We are not specifically calling them.
        # Is called automatically when some precondition happens.
        """
        Initialize the Point with X,Y coordinates
        :param x: X coordinate
        :param y: Y coordinate
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        String representation of the Point
        :return: p<x,y>
        """
        return f"p<{self.x},{self.y}>"
    def __repr__(self):
        return self.__str__()
    def distance_to_origin(self):
        """
        Calculate the distance between this Point and origin
        :return: float
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def distance_to_other(self, other):
        """
        Calculate the distance between this Point and another Point
        :param other: another Point
        :return: the distance from the other point to the point
        """
        return ((self.x-other.x) ** 2 + (self.y-other.y) ** 2) ** 0.5
    def __lt__(self, other):
        """
        Compare two points Objects
        :param other: the other point object
        :return: bool True or False
        """
        if isinstance(other, int):
            return self.x < other
        return self.distance_to_origin() < other.distance_to_origin()
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.x == other
    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other) # returns a new Point
        raise TypeError("Can only multiply by integers")

if __name__ == "__main__":
    # instantiate the point class
    p1 = Point(1,2)
    print(p1.x, p1.y)
    p2 = Point(3,4)
    print(p2.x, p2.y)
    print(p1) #
    p3 = Point(3,4)
    print(p3.distance_to_origin())
    p4 = Point(12,5)
    print(p4.distance_to_origin())
    points = [p1, p2, p3, p4, Point(-2,6)]
    points.append(Point(-5,-5))
    print(points[4].x)
    print(points)
    points.sort()
    print(points)
    print(Point(7,11).distance_to_other(Point(7,15)))
    print(p2*4)

