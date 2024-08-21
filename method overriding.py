class shape():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

class Cuboid(shape):
    def __init__(self,z):
        self.z = z
        super().__init__(z,z)

    def area(self):
        return (self.x*self.y + self.y*self.z + self.z*self.x)

c=Cuboid(5)

print(c.area())