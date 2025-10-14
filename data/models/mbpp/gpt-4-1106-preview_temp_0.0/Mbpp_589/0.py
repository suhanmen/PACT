"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

import math

def perfect_squares(start, end):
    squares = []
    for number in range(start, end + 1):
        root = math.sqrt(number)
        if root.is_integer():
            squares.append(number)
    return squares

# Example usage:
# perfect_squares_list = perfect_squares(1, 30)
# print(perfect_squares_list)
