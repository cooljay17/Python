#Extend Car into an ElectricCar subclass with battery capacity
from Car import Car

class ElectricCar(Car):    
     def __init__(self, name, color,capacity):  
        super().__init__(name,color)
        self.capacity = capacity        

     def display(self): 
        print(f"The {self.name} car is a {self.color} beauty and has {self.capacity} !!!")

# Creating an instance of car
ecarObj1 = ElectricCar("BMW", "Black","2979 cc")
ecarObj1.display()
ecarObj2 = ElectricCar("Rolls Royce", "Silver","6749 cc")
ecarObj2.display()   