a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find indices of even numbers
even_indices = [i for i, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indices)

# Sort the array
sorted_array = sorted(a)
print("Sorted array:", sorted_array)

# Slice elements from index 3 to the end of the array
slice1 = a[3:]
print("Elements from index 3 to end:", slice1)

# Slice elements from index 0 to index 4
slice2 = a[0:5]
print("Elements from index 0 to index 4:", slice2)

# Print [32, 15, 67] using negative slicing
negative_slice = a[-5:-2]
print("Negative slicing [32, 15, 67]:", negative_slice)