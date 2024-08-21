class parent_class():
    def parent_method(self):
        print("This is the parent class")

class child_class(parent_class):
    def child_method(self):
        print("This is the child class")
        super().parent_method()


a = parent_class()
b = child_class()

b.child_method()
b.parent_method
