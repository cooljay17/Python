#Create a Car class with attributes and a display method
class Car:
    def __init__(self, name, color):  
        self.name = name 
        self.color = color

    def display(self): 
        print(f"The {self.name} car is a {self.color} beauty!!!")

# Creating an instance of car
carObj1 = Car("BMW", "Black")
#carObj1.display()
carObj2 = Car("Rolls Royce", "Silver")
#carObj2.display()