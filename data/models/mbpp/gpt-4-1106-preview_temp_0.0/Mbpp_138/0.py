"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""


import math

def is_Sum_Of_Powers_Of_Two(n):
    # If n is less than or equal to 0, it cannot be represented as a sum of non-zero powers of 2
    if n <= 0:
        return False

    # Keep subtracting the largest power of 2 less than or equal to n
    while n > 0:
        # Find the largest power of 2 less than or equal to n
        power = int(math.log(n, 2))
        # Subtract that power of 2 from n
        n -= 2 ** power

    # If we have subtracted all powers of 2 and reached 0, n can be represented as a sum of non-zero powers of 2
    return n == 0

# Example usage
assert is_Sum_Of_Powers_Of_Two(10) == True
