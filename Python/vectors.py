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
		
class Vec3D(object):
	def __init__(self, nX, nY, nZ):
		self.x = nX
		self.y = nY
		self.z = nZ
		
	def info(self):
		print self.x, ",", self.y, ",", self.z
		
	def __add__(self, other):
		result = Vec3D(0,0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		result.z = self.z + other.z
		return result
		
	def __sub__(self, other):
		result = Vec3D(0,0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		result.z = self.z - other.z
		return result
		
	def magnitude(self):
		result = Vec3D(0,0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		result.z = self.z ^ 2
		nResult = sqrt(result.x + result.y + result.z)
		return result
		
	def normalize(self):
		result = Vec3D(0,0,0)
		if (self.x >= self.y and self.x >= self.z):
			div = self.x
		elif (self.y >= self.x and self.y >= self.z):
			div = self.y
		else:
			div = self.z
		result.x = self.x / div
		result.y = self.y / div
		result.z = self.z / div
		return result
		
	def __mul__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return x + y + z
		
	def cross(self, other):
		result = Vec3D(0,0,0)
		result.x = (self.y * other.z) - (other.y + self.z)
		result.y = (self.z * other.x) - (other.z + self.x)
		result.z = (self.x * other.y) - (other.x + self.y)
		return result
		
	def lerp(self, other, per):
		result = Vec3D(0,0,0)
		result.x = self.x + (per * (other.x - self.x))
		result.y = self.y + (per * (other.y - self.y))
		result.z = self.z + (per * (other.z - self.z))
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
		
