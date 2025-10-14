"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""


import math

def last_Digit_Factorial(n):
    # Since the last digit of factorial for n >= 5 is always 0
    if n >= 5:
        return 0
    else:
        # Calculate factorial for n < 5
        factorial = math.factorial(n)
        # Return the last digit
        return factorial % 10

# Example usage
# last_Digit_Factorial(4) should return 4
assert last_Digit_Factorial(4) == 4
