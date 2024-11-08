# Riley Green
# UWYO COSC 1010
# Submission Date: 11/07/24
# Lab 10
# Lab Section: 13
# Sources, people worked with, help given to: Nolan Hottell, Bradley Ekstrom
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def num_convert(num):
    isNeg = False 
    if "-" in num:
        isNeg = True
        num = num.replace("-", " ")
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit:
            if isNeg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg: 
            return -1 * int(num)
        else:
            return int(num)
    else: 
        return False 

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, a, z):
    if not isinstance(a, int) or not isinstance(z, int):
        return False
    if a > z:
        return False
    y_values = []
    for x in range(a, z + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

import math
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def safe_sqrt(x):
    if x < 0:
        return None
    return math.sqrt(x)

def quadratic_function(a, b, c):
    x = b**2 - 4 * a * c
    sqrt_x = safe_sqrt(x)
    if sqrt_x is None:
        return None
    
    root_1 = (-b + sqrt_x) / (2 * a)
    root_2 = (-b - sqrt_x) / (2 * a)
    return root_1, root_2

while True:
    a = input("Enter coefficient a, or 'exit' to quit: ")
    if a.lower() == 'exit':
        break
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")

    a = num_convert(a)
    b = num_convert(b)
    c = num_convert(c)

    if a is not False and b is not False and c is not False:
        result = quadratic_function(a, b, c)
        if result is None:
            print("No real roots")
        else:
            print(f"The roots are: {result}")
    else:
        print("Invalid input. Please other numbers.")

print("*" * 75)