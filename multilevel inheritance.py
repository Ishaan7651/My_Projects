class car():
    def __init__(self,name):
        self.name = name
        print(f"The name of the car is {self.name}")


class Segment(car):
    
    def __init__(self,name,segment):
        self.segment = segment
        car.__init__(self,name)
        print(f"The segment of the car is {self.segment}")

class Price(Segment):
    
    def __init__(self,name,segment,price):
        self.price = price
        Segment.__init__(self,name,segment)
        print(f"The price of the car is {self.price}")


a = Price("Aventador","Super Car","5.01 Cr") 
print(Price.mro())
    
