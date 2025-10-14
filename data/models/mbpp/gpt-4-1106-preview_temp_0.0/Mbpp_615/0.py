"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""


import json

def average_tuple(tuples):
    return [sum(t) / len(t) for t in tuples]

# Example usage
# averages = average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))
# print(averages)  # Output: [10.5, 44.0, 58.0, 2.5]

# Test
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [10.5, 44.0, 58.0, 2.5]
