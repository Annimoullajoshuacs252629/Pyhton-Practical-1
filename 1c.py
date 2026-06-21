import math

for i in range(3): 
    try:
        num = float(input("Enter a number: "))

        if num < 0:
            print("Square root of a negative number is not possible.")
        else:
            print("Square root =", math.sqrt(num))

    except ValueError:
        print("Invalid input! Please enter a number.")
