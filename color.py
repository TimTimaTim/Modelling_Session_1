from Economic_Modeling_1 import Point

class Color_Point(Point):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        return f"{self.color}: cp<{self.x},{self.y}>"

p1 = Color_Point(1,2, "red")
p2 = Color_Point(2,3, "blue")

print(p1.x, p1.y, p1.color)
print(p2)
print(p2.distance_to_origin())
points = [p1, p2]
print(points)

points.append(Point(2,0))
points.sort()
print(points)
