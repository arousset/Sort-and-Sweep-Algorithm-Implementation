import math
from math import *

class Vec2D(ibject):
	def __init__(self, nX, nY):
		self.x = nX
		self.y = nY
		
	def info(self):
		print self.x, ",", self.y
		
	def __add__(self, other):
		result = Vec2D(0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		return result
		
	def __sub__(self, other):
		result = Vec2D(0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		return result
		
	def magnitude(self):
		result = Vec2D(0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		nResult = sqrt(result.x + result.y)
		return nResult
		
	def normalize(self):
		result = Vec2D(0,0)
		if (self.x >= self.y):
			div = self.x
		else:
			div = self.y
		result.x = self.x / div
		result.y = self.y / div
		return result
		
	def __mul__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return x + y
		
	def lerp(self, other, per):
		result = Vec2D(0,0)
		result.x = self.x + (per * (other.x - self.x))
		result.y = self.y + (per * (other.y - self.y))
		return result
		
	def angle(self, other):
		opp = self.magnitude()
		base = other.magnitude()
		hyp = sqrt((base * base) + (opp * opp))
		tri = Vec3D(base, opp, hyp)
		tri = tri.normalize()
		angle = acos(base / hyp)
		result = (angle / 3.14) * 180
		return result
		
