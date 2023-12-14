def prod (lst):
    product = 1
    for num in lst:
        product *= num
    return product

# the number list
num = [9, 10, 11, 12]

# Calculating product by passing the list to the function
result = prod (num)

print(f"The product of the values in the list is: {result}")