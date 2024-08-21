class employee():
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        print(self.name, self.age, self.designation)


    @classmethod
    def add_name(cls,name,age,designation):
        cls.name = name
        cls.age = age
        cls.designation = designation


string = [("Ishaan-19-CEO"),("Japman-18-COO")]
a_data = string[0].split("-")
b_data = string[1].split("-")

a = employee(a_data[0],a_data[1],a_data[2])
b = employee(b_data[0],b_data[1],b_data[2])
