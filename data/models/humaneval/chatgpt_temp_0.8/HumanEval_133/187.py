import math

def sum_squares(lst):
    # initialize the sum of squared numbers to zero
    sum_squares = 0
    # loop through each element in the list
    for num in lst:
        # round the element to the nearest integer using the ceiling function from the math library
        num_rounded = math.ceil(num)
        # square the rounded number and add it to the sum of squared numbers
        sum_squares += num_rounded ** 2
    # return the final sum of squared numbers
    return sum_squares
