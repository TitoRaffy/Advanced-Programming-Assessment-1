lanes = int(input("Type down how many rows you wanna put down!: "))

for r in range(lanes): # create a for loop and use "r" to represent the number of rows
    for i in range(r+1): # and in this next loop we print the numbers according to the inputed number
        print(i+1, end=" ") # prints the ending result
    print("\n")