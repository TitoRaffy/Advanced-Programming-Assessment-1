year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# access the value at index -3
negative_3 = year[-3]
print("Value at index -3:", negative_3)

# reverse the tuple and print the original tuple and reversed tuple
reversed_year = tuple(reversed(year))
print("Original Tuple:", year)
print("Reversed Tuple:", reversed_year)

# count number of times 2009 is in the tuple
count_2009 = year.count(2009)
print("Number of times 2009 appears in the tuple:", count_2009)

# get the index value of 2018
index_2018 = year.index(2018)
print("Index of 2018:", index_2018)

# find the length of the given tuple
length = len(year)
print("Length of the tuple:", length)