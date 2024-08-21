class Person:
    name = "Ishaan"
    Age = 19
    Designation = "Director"
    def info(self):
        print(f"The name of the candidate is {self.name} and he/she is working as a {self.Designation}")
a = Person()

a.name = "Radhe"
a.age = 19
a.Designation = "Head of Marketing"
a.info()


b = Person()
b.name = input("Enter the name of the employee ")
b.Age = input("Enter the age of the employee ")
b.Designation = input("Enter the designation of the employee ")
b.info()


