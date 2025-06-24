#find the faults in your code (or some opensource code), improve it by applying clean code principles and make it readable (create a PR if doing it for any opensource project). 
# Badly written Python code for area calculations

s = 5 # side of square
_area_of_square_ = s*s
print ("Bad code::area of a square is: ", _area_of_square_)

Radius = 10
areaofcircle = 3.14 * Radius * Radius
print ("Bad code::area of circle: ", areaofcircle)

length = 4
WIDTH = 6
AreaOfRectangle = length * WIDTH
print ("Bad code::AREA OF RECTANGLE: ", AreaOfRectangle)

#Good Python code for area calculations
def area_of_square(side):
    """Calculate the area of a square."""
    return side * side  

def area_of_circle(radius):
    """Calculate the area of a circle."""
    return 3.14 * radius * radius

def area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def main():
    side = 5
    radius = 10
    length = 4
    width = 6
    
    print("Good code::Area of a square is:", area_of_square(side))
    print("Good code::Area of circle:", area_of_circle(radius))
    print("Good code::Area Of Rectangle:", area_of_rectangle(length, width))

main()    