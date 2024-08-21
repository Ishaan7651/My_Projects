n = int(input("Enter the number of variables you want to create: "))

variables = {}  # Create an empty dictionary to store variables

for i in range(n):
    var_name = input("Enter variable name {}: ".format(i+1))
    var_value = input("Enter value for {}: ".format(var_name))
    variables[var_name] = var_value  # Add variable name and value to the dictionary

# Accessing variables
for var_name, var_value in variables.items():
    print("{} = {}".format(var_name, var_value))
