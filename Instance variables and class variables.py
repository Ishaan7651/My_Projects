class employee():
    company_name = "Apple"
    emp_count = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.3
        employee.emp_count+=1
        
    def display(self):
        print(f"{self.name} working in {self.company_name} and is getting a raise of {self.raise_amount} percent")


a = employee("Ishaan")
b = employee("Bob")
c = employee("Lols")

a.display()