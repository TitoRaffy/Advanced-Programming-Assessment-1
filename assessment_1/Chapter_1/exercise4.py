# the user gets to input 3 numbers of their choice
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# this if else statement will calculate what the largest number is
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# then this prints out the result of the largest number
print(f"The largest number is: {largest}")