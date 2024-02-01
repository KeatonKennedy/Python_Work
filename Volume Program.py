import math
print("This program calculates the volume of:")
print("Cube, Rectangular Prism, Triangular Prism, Sphere, Cylinder\n")
shape = str(input("Enter your shape: "))

def cubeCal():
    length = float(input("Length of cube: "))
    volume = length ** 3
    print(volume)
    
def sphereCal():
    radius = float(input("Radius of sphere: "))
    volume = 4/3 * math.pi * radius ** 3
    print(volume)

def recprismCal():
    length = float(input("Length of Rectangular Prism: "))
    width = float(input("Width of Rectangular Prism: "))
    height = float(input("Height of Rectangular Prism: "))
    volume = length * width * height
    print(volume)

def cylinderCal():
    radius = float(input("Radius of cylinder: "))
    height = float(input("Height of cylinder: "))
    volume = math.pi * radius ** 2 * height
    print(volume)
    
def triprismCal():
    a = float(input("Side A of Triangular Prism: "))
    b = float(input("Side B of Rectangular Prism: "))
    c = float(input("Side C of Triangular Prism: "))
    h = float(input("Height of Rectangular Prism: "))
    volume = 1/4*h*math.sqrt(-a**4+2*(a*b)**2+2*(a*c)**2-b**4+2*(b*c)**2-c**4)
    print(volume)

if shape == "cube":
    cubeCal()
elif shape == "sphere":
    sphereCal()
elif shape == "rectangular prism":
    recprismCal()
elif shape == "cylinder":
    cylinderCal()
elif shape == "triangular prism":
    triprismCal()
else:
    print("Error... Try Again")
