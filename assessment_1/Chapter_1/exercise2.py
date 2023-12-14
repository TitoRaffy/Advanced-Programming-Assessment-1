# input 2 numbers you want to calculate
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))


sum = n1 + n2
diff = n1 - n2     # this shows all the results of the 2 numbers you calculated 
prod = n1 * n2
quot = n1 / n2
rem = n1 % n2

# prints out the results to the console
print(f"Sum: {n1} + {n2} = {sum}")
print(f"Difference: {n1} - {n2} = {diff}")
print(f"Product: {n1} * {n2} = {prod}")
print(f"Quotient: {n1} / {n2} = {quot}")
print(f"Remainder: {n1} % {n2} = {rem}")