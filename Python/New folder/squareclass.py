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
