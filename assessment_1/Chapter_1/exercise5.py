# starts up a counter keep track of the numbers
count = 0

# the loop the will continue until the user decides to stop the loop by typing any letter other than Y
while True:
    user = input("Would you like to continue? (Y/N): ")
    count += 1  # increment the counter for each loop iteration
    
    if user.upper() != 'Y':
        break  # exit the loop if the user doesn't input 'Y'

# prints the number of loops executed
print(f"The loop executed {count} times.")