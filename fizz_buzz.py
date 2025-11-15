
for i in range(1, 21):  # Loop from 1 to 20
    if i % 3 == 0 and i % 5 == 0:  # Check for multiples of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Check for multiples of 3
        print("Fizz")
    elif i % 5 == 0:  # Check for multiples of 5
        print("Buzz")
    else:
        print(i) # Print the number if it's neither a multiple of 3 nor 5
