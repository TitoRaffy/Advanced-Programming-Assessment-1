# lets the user input the length of their choice on 3 sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# this is to calculate the triangle of its inequality 
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # the "if" statement is whether to determine if the triangle is Equilateral, Isosceles, or a Scalene Triangle
    if side1 == side2 == side3:
        print("This is an Equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")

else: # and if the user inputs an invalid text or character, it'll cause an error which it can not be printed
    print("These side lengths cannot form a triangle.") 