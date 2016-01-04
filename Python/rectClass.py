import vectors
from vectors import *

class rect(object):
	def __init__(self, nX, nY, nH, nW, nN):
		self.x = nX
		self.y = nY
		self.h = nH
		self.w = nW
		self.n = nN
		self.min = {self.x - (self.w / 2), self.y - (self.h / 2)}
		self.max = {self.x + (self.w / 2), self.y + (self.h / 2)}