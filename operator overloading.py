class Vector():
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        
        return f"{self.x}x + {self.y}y + {self.z}z"
    
    def __add__(self, next):
        return f"{self.x + next.x}x + {self.y + next.y}y + {self.z + next.z}z"
    

v1 = Vector(2,5,9)
print(v1)

v2 = Vector(3,6,10)
print(v2)
print(v1 + v2)