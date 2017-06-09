import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getPerimeter(self):
        return 2*self.radius*math.pi
    def getArea(self):
        return self.radius**2*math.pi
    def getRadius(self):
        return self.radius