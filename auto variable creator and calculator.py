
variables = {}
def create_variables():
    n = int(input("Enter the number of variables you want to create:- "))
    global variables
    for i in range(n):  
        name = input(f"Enter the name of the variable {i+1} ")
        value = int(input(f"Enter the value of the variable {i+1} "))
        variables[name] = value


def show_variables():
    for name,value in variables.items():
        print(f"{name} = {value}")



create_variables()

show_variables()