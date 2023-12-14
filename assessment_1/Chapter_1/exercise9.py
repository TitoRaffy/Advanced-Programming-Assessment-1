# Create an int list with 10 values
num_list = [200, 56, 34, 69, 3, 10, 567, 23]

# Output the list using a for loop
print("List using a for loop:")
for num in num_list:
    print(num, end=" ")
print("\n")

# Output the highest and lowest value
print("Highest value:", max(num_list))
print("Lowest value:", min(num_list))
print()

# Sort the elements in ascending order
ascending = sorted(num_list)
print("Numbers in ascending order:", ascending)
print()

# Sort the elements in descending order
descending = sorted(num_list, reverse=True)
print("Numbers in descending order:", descending)
print()

# Append two elements
num_list.append(450)
num_list.append(6)
print("List after appending two elements:", num_list)