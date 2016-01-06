class Vector2D:
    def __init__(self, a, b):
        self.x = a + 0.0
        self.y = b + 0.0
        self.magnitude = 0.0
    def __add__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp
    def __sub__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        return temp
    def __mul__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x * other.x
        temp.y = self.y * other.y
        return temp
    def div(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x / other.x
        temp.y = self.y / other.y
        return temp
    def mag(self):
        temp = self * self
        self.magnitude = (temp.x + temp.y)**(0.5)
        return self.magnitude
    def norm(self):
        temp = Vector2D(0,0)
        temp.x = self.x / self.magnitude
        temp.y = self.y / self.magnitude
        temp.magnitude = self.magnitude / self.magnitude
        return temp
    def dotProd(self, other):
        temp = ((self.x*other.x)+(self.y*other.y))
        return temp
    def interp(self, a, b, t):
        L = a + t * (b - a)
        return L
#------------------------------------------------------------------
class Vector3D:
    def __init__(self, a, b, c):
        self.x = a + 0.0
        self.y = b + 0.0
        self.z = c + 0.0
        self.magnitude = 0.0
    def __add__(self, other):
        temp = Vector3D(0,0,0)
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z = self.z + other.z
        return temp
    def __sub__(self, other):
        temp = Vector3D(0,0,0)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        temp.z = self.z - other.z
        return temp
    def __mul__(self, other):
        temp = Vector3D(0,0,0)
        temp.x = self.x * other.x
        temp.y = self.y * other.y
        temp.z = self.z * other.z
        return temp
    def div(self, other):
        temp = Vector3D(0,0,0)
        temp.x = self.x / other.x
        temp.y = self.y / other.y
        temp.z = self.z / other.z
        return temp
    def mag(self):
        temp = self * self
        self.magnitude = (temp.x+temp.y+temp.z)**(0.5)
        return self.magnitude
    def norm(self):
        temp = Vector3D(0,0,0)
        temp.x = self.x / self.magnitude
        temp.y = self.y / self.magnitude
        temp.z = self.z / self.magnitude
        temp.magnitude = self.magnitude / self.magnitude
        return temp
    def dotProd(self, other):
        temp = ((self.x*other.x)+(self.y*other.y)+(self.z*other.z))
        return temp
    def crsProd(self, other):
        temp = Vector3D(0,0,0)
        temp.x = ((self.y*other.z)-(self.z*other.y))
        temp.y = ((self.z*other.x)-(self.x*other.z))
        temp.z = ((self.x*other.y)-(self.y*other.x))
        return temp
    def interp(self, a, b, t):
        L = a + t * (b - a)
        return L
#------------------------------------------------------------------
class Vector4D:
    def __init__(self, a, b, c, d):
        self.x = a + 0.0
        self.y = b + 0.0
        self.z = c + 0.0
        self.w = d + 0.0
        self.magnitude = 0.0
    def __add__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z = self.z + other.z
        temp.w = self.w + other.w
        return temp
    def __sub__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        temp.z = self.z - other.z
        temp.w = self.w - other.w
        return temp
    def __mul__(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x * other.x
        temp.y = self.y * other.y
        temp.z = self.z * other.z
        temp.w = self.w * other.w
        return temp
    def div(self, other):
        temp = Vector2D(0,0)
        temp.x = self.x / other.x
        temp.y = self.y / other.y
        temp.z = self.z / other.z
        temp.w = self.w / other.w
        return temp
    def mag(self):
        temp = self * self
        self.magnitude = (temp.x+temp.y+temp.z+temp.w)**(0.5)
        return self.magnitude
    def norm(self):
        temp = Vector2D(0,0)
        temp.x = self.x / self.magnitude
        temp.y = self.y / self.magnitude
        temp.z = self.z / self.magnitude
        temp.w = self.w / self.magnitude
        temp.magnitude = self.magnitude / self.magnitude
        return temp
    def dotProd(self, other):
        temp = ((self.x*other.x)+(self.y*other.y)+(self.z*other.z)+(self.w*other.w))
        return temp
    def interp(self, a, b, t):
        L = a + t * (b - a)
        return L