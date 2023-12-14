for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: # this prints out "fizzbuzz" for both the multiples of 5 and 3
        print("FizzBuzz")
    elif i % 3 == 0: # on the other hand, "fizz" prints out every number that is the multiples of 3
        print("Fizz")
    elif i % 5 == 0: # while "buzz" prints out the multiples of 5
        print("Buzz")
    else:
        print(i)