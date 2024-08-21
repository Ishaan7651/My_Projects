
class Employee():
    def __init__(self, name):
        self.name = name
        

    def __len__(self):
        i = 0 
        for c in self.name:
            i = i+1
        return i

    def __call__(self):
        print("I was called")

    def __str__(self):
        return ("This Class stores your name and then returns the length of your name using the len operator")
        




