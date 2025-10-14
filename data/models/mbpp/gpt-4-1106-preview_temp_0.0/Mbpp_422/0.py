"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""


import json

def find_Average_Of_Cube(n):
    # Calculate the sum of cubes of first n natural numbers
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    # Calculate the average
    average = sum_of_cubes / n
    return average

# Test the function
assert find_Average_Of_Cube(2) == 4.5
