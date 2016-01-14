import Vector_Class
from Vector_Class import *
class Rectangle:
    def __init__(self, a1, b1, a2, b2, t):
        self.title = t
        self.minX = a1
        self.minY = b1
        self.maxX = a2
        self.maxY = b2
        self.W = self.maxX - self.minX
        self.H = self.maxY - self.minY
        self.mid = Vector2D (self.minX+(self.W / 2), self.minY+(self.H/2))

'''bob = Rectangle(1, 1, 4, 4)
print ("p0 = (",bob.minX,",",bob.minY,")")
print ("p1 = (",bob.minX,",",bob.maxY,")")
print ("p2 = (",bob.maxX,",",bob.maxY,")")
print ("p3 = (",bob.maxX,",",bob.minY,")")
print ("Width =",bob.W)
print ("Height =",bob.H)
print ("Middle point =(",bob.mid.x,",",bob.mid.y,")")'''