import vectors
from vectors import *

print "Vector 2D maths:"
a = Vec2D(6,6)
b = Vec2D(12,12)

print "Vectors A and B:"
a.info()
b.info()
print " "
c = a + b
print "addition:"
c.info()
print " "

c = a - b
print "subtraction:"
c.info()
print " "

