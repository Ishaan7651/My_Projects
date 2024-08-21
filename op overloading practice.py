class person():
    def __init__(self, name, age,credits):
        self.name = name
        self.age = age
        self.credits = credits
        

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nCredits: {self.credits}"
    
    def __add__(self, other):
        return f"Name: {self.name}\nAge: {self.age}\nCredits: {self.credits + other.credits}"
    

class new_person():
    def __init__(self,credits):
        self.credits = credits


v1 = person("Ishaan",19,20)
v2 = new_person(30)
v3 = new_person(50)
print(v1+v2)
print(v1+v3)