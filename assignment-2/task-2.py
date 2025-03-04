# utility functions
def CalculateCircleArea(radius):
    return PI * (radius**2)


def CalculateRectangleArea(height, width):
    return height * width


def CalculateTriangleArea(base, height):
    return 0.5 * base * height


# defining constants
PI = 3.14

# Input Menu
print(f"1. Calculate the area of circle.")
print(f"2. Calculate the area of rectangle.")
print(f"3. Calculate the area of square.")
print(f"4. Calculate the area of triangle.")
print(f"5. Exit.")

while True:
    print(f"Enter your choice:-")
    # reading user choice
    choice = int(input())
    if choice == 1:
        radius = int(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {CalculateCircleArea(radius)}")
        
    elif choice == 2:
        height = int(input("Enter the height of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {CalculateRectangleArea(height, width)}")
        
    elif choice == 3:
        height = int(input("Enter the height of the square: "))
        print(f"The area of the rectangle is: {CalculateRectangleArea(height, height)}")
        
    elif choice == 4:
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        print(f"The area of the rectangle is: {CalculateTriangleArea(base, height)}")
        
    elif choice == 5:
        print(f"Exiting!")
        break;
        
    else:
        print(f"Please enter valid choice")