# here you will be entering your name in this input box
name = input("Hello, user!\nWhat is your name? ").title()

# and in this, you will be entering your age
age = int(input("What is your age? "))

# your name will then be printed
print(f"It is good to meet you, {name}")

# the length of the entered name weill be calculated
length = len(name)
print("The length of your name is:")
print(length)

# calculates the age you added, and it will be added by one
one_yr = age + 1
print(f"You will be {one_yr} in a year.")