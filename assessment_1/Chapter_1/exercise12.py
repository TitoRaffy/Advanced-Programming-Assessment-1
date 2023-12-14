import math

# the user will choose to enter a specific measurement depending on the shape
# then the result will be printed
def square_area():
    side = float(input("Enter the length of the side of the square: "))
    area = side * side
    print(f"The area of the square is: {area}")

def circle_area ():
    radius = float(input("Enter the radius of the circle: "))                 
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area}")

def triangle_area ():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

while True: # allows the user to choose which shape the user wants to calculate
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        square_area()
    elif choice == '2':
        circle_area ()
    elif choice == '3':
        triangle_area ()
    elif choice == '4':
        print("Exiting the program.")
        break
    else: # if the user enters an unknown character or number, it will be an invalid output
        print("Invalid choice. Please enter a number from 1 to 4.")